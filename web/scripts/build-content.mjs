import { marked } from "marked";
import { mkdir, readFile, readdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(here, "../..");
const outputFile = path.join(repoRoot, "web/public/reports.json");

const contentRoots = [
  {
    type: "reform-project",
    dir: "projekte/rentenversicherung",
    label: "Reformprojekt",
  },
];

marked.use({
  gfm: true,
  breaks: false,
});

function slugify(value) {
  return value
    .toLowerCase()
    .replaceAll("ä", "ae")
    .replaceAll("ö", "oe")
    .replaceAll("ü", "ue")
    .replaceAll("ß", "ss")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

function parseScalar(rawValue) {
  const value = rawValue.trim();
  if (value === "true") return true;
  if (value === "false") return false;
  if (value.startsWith("[") && value.endsWith("]")) {
    return value
      .slice(1, -1)
      .split(",")
      .map((item) => item.trim().replace(/^["']|["']$/g, ""))
      .filter(Boolean);
  }
  return value.replace(/^["']|["']$/g, "");
}

function parseFrontmatter(markdown) {
  if (!markdown.startsWith("---\n")) {
    return { data: {}, body: markdown };
  }

  const closeIndex = markdown.indexOf("\n---", 4);
  if (closeIndex === -1) {
    return { data: {}, body: markdown };
  }

  const rawFrontmatter = markdown.slice(4, closeIndex);
  const body = markdown.slice(closeIndex + 4).trimStart();
  const data = {};
  let currentKey = null;

  for (const line of rawFrontmatter.split("\n")) {
    if (!line.trim()) continue;

    const listItem = line.match(/^\s+-\s+(.*)$/);
    if (listItem && currentKey) {
      if (!Array.isArray(data[currentKey])) data[currentKey] = [];
      data[currentKey].push(parseScalar(listItem[1]));
      continue;
    }

    const pair = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (!pair) continue;

    currentKey = pair[1];
    data[currentKey] = pair[2] ? parseScalar(pair[2]) : [];
  }

  return { data, body };
}

function extractSummary(markdown) {
  const match = markdown.match(/## Kurzfassung\s+([\s\S]*?)(?=\n## |\n# |$)/);
  if (!match) return "";
  return match[1]
    .replace(/\n+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function extractBudgetMetrics(markdown) {
  const metrics = [];
  const metricNames = [
    "Ausgaben",
    "Einnahmen ohne Nettokreditaufnahme",
    "Steuereinnahmen",
    "Nettokreditaufnahme",
    "Investitionen im Kernhaushalt",
  ];

  for (const name of metricNames) {
    const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const match = markdown.match(new RegExp(`- ${escaped}: ([^\\n]+)`));
    if (match) metrics.push({ label: name, value: match[1].trim() });
  }

  return metrics;
}

function extractSankey(markdown) {
  const match = markdown.match(/```json sankey\s+([\s\S]*?)```/);
  if (!match) return null;

  try {
    return JSON.parse(match[1]);
  } catch (error) {
    throw new Error(`Invalid sankey JSON: ${error.message}`);
  }
}

function stripDataBlocks(markdown) {
  return markdown.replace(/```json sankey\s+[\s\S]*?```/g, "").trim();
}

async function readMarkdownFiles(dir) {
  const absoluteDir = path.join(repoRoot, dir);
  let entries = [];

  try {
    entries = await readdir(absoluteDir, { withFileTypes: true });
  } catch {
    return [];
  }

  return entries
    .filter((entry) => entry.isFile() && entry.name.endsWith(".md"))
    .map((entry) => path.join(absoluteDir, entry.name));
}

async function buildReports() {
  const reports = [];

  for (const root of contentRoots) {
    const files = await readMarkdownFiles(root.dir);

    for (const file of files) {
      const markdown = await readFile(file, "utf8");
      const { data, body } = parseFrontmatter(markdown);
      if (data.publish !== true) continue;
      const sankey = extractSankey(body);
      const displayBody = stripDataBlocks(body);

      const relativePath = path.relative(repoRoot, file);
      const title =
        data.title ||
        displayBody.match(/^#\s+(.+)$/m)?.[1] ||
        path.basename(file, ".md");
      const id = data.slug || slugify(`${root.type}-${title}`);

      reports.push({
        id,
        title,
        date: data.date || "",
        type: data.type || root.type,
        typeLabel: root.label,
        tags: Array.isArray(data.tags) ? data.tags : [],
        sourceUrls: Array.isArray(data.source_urls) ? data.source_urls : [],
        relatedMinistries: Array.isArray(data.related_ministries)
          ? data.related_ministries
          : [],
        relatedLaws: Array.isArray(data.related_laws) ? data.related_laws : [],
        path: relativePath,
        summary: data.summary || extractSummary(displayBody),
        metrics: root.type === "bundeshaushalt" ? extractBudgetMetrics(displayBody) : [],
        sankey,
        html: marked.parse(displayBody),
      });
    }
  }

  reports.sort((a, b) => `${b.date}${b.title}`.localeCompare(`${a.date}${a.title}`));

  await mkdir(path.dirname(outputFile), { recursive: true });
  await writeFile(
    outputFile,
    JSON.stringify(
      {
        generatedAt: new Date().toISOString(),
        reports,
      },
      null,
      2,
    ),
  );

  console.log(`Generated ${reports.length} published report(s).`);
}

await buildReports();
