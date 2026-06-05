import { useEffect, useMemo, useState } from "react";

type Metric = {
  label: string;
  value: string;
};

type SankeyEntry = {
  label: string;
  value: number;
};

type SankeyData = {
  title: string;
  unit: string;
  centerLabel: string;
  note: string;
  income: SankeyEntry[];
  spending: SankeyEntry[];
};

type Report = {
  id: string;
  title: string;
  date: string;
  type: string;
  typeLabel: string;
  tags: string[];
  sourceUrls: string[];
  relatedMinistries: string[];
  relatedLaws: string[];
  path: string;
  summary: string;
  metrics: Metric[];
  sankey: SankeyData | null;
  html: string;
};

type ContentIndex = {
  generatedAt: string;
  reports: Report[];
};

const typeLabels: Record<string, string> = {
  all: "Alle",
  analyse: "Analysen",
  bundeshaushalt: "Bundeshaushalt",
  "bundestag-drucksache": "Drucksachen",
  "reform-report": "Reformreports",
};

function getHashReportId() {
  const match = window.location.hash.match(/^#\/reports\/(.+)$/);
  return match ? decodeURIComponent(match[1]) : null;
}

function App() {
  const [content, setContent] = useState<ContentIndex | null>(null);
  const [loadError, setLoadError] = useState("");
  const [selectedType, setSelectedType] = useState("all");
  const [selectedTag, setSelectedTag] = useState("all");
  const [activeReportId, setActiveReportId] = useState<string | null>(getHashReportId());

  useEffect(() => {
    fetch(`${import.meta.env.BASE_URL}reports.json`)
      .then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
      })
      .then(setContent)
      .catch((error: unknown) => {
        setLoadError(error instanceof Error ? error.message : "Unbekannter Fehler");
      });
  }, []);

  useEffect(() => {
    const onHashChange = () => setActiveReportId(getHashReportId());
    window.addEventListener("hashchange", onHashChange);
    return () => window.removeEventListener("hashchange", onHashChange);
  }, []);

  const reports = content?.reports ?? [];
  const activeReport = reports.find((report) => report.id === activeReportId) ?? null;
  const reportTypes = useMemo(
    () => ["all", ...Array.from(new Set(reports.map((report) => report.type)))],
    [reports],
  );
  const tags = useMemo(
    () => ["all", ...Array.from(new Set(reports.flatMap((report) => report.tags))).sort()],
    [reports],
  );
  const filteredReports = useMemo(
    () =>
      reports.filter((report) => {
        const typeMatches = selectedType === "all" || report.type === selectedType;
        const tagMatches = selectedTag === "all" || report.tags.includes(selectedTag);
        return typeMatches && tagMatches;
      }),
    [reports, selectedTag, selectedType],
  );

  const metricTotals = useMemo(
    () => reports.filter((report) => report.metrics.length > 0).flatMap((report) => report.metrics),
    [reports],
  );

  if (activeReport) {
    return <ReportDetail report={activeReport} onBack={() => setRouteHome()} />;
  }

  return (
    <main className="app-shell">
      <header className="site-header">
        <div>
          <p className="eyebrow">agenda2030</p>
          <h1>Reports</h1>
          <p className="lede">
            Interaktive Auswertung freigegebener Haushalts- und
            Bundestagsdrucksachen-Zusammenfassungen.
          </p>
        </div>
        <div className="status-panel">
          <span>{reports.length}</span>
          <p>veröffentlichte Reports</p>
        </div>
      </header>

      {loadError ? (
        <section className="notice" role="alert">
          Reports konnten nicht geladen werden: {loadError}
        </section>
      ) : null}

      <section className="toolbar" aria-label="Reportfilter">
        <div className="field-group">
          <label htmlFor="type-filter">Typ</label>
          <select
            id="type-filter"
            value={selectedType}
            onChange={(event) => setSelectedType(event.target.value)}
          >
            {reportTypes.map((type) => (
              <option key={type} value={type}>
                {typeLabels[type] ?? type}
              </option>
            ))}
          </select>
        </div>
        <div className="field-group">
          <label htmlFor="tag-filter">Thema</label>
          <select
            id="tag-filter"
            value={selectedTag}
            onChange={(event) => setSelectedTag(event.target.value)}
          >
            {tags.map((tag) => (
              <option key={tag} value={tag}>
                {tag === "all" ? "Alle" : tag}
              </option>
            ))}
          </select>
        </div>
      </section>

      {metricTotals.length > 0 ? (
        <section className="metric-grid" aria-label="Haushaltskennzahlen">
          {metricTotals.slice(0, 5).map((metric) => (
            <article className="metric-card" key={`${metric.label}-${metric.value}`}>
              <p>{metric.label}</p>
              <strong>{metric.value}</strong>
            </article>
          ))}
        </section>
      ) : null}

      <section className="report-list" aria-label="Reports">
        {filteredReports.length ? (
          filteredReports.map((report) => (
            <article className="report-card" key={report.id}>
              <div className="report-card__meta">
                <span>{report.typeLabel}</span>
                {report.date ? <time dateTime={report.date}>{report.date}</time> : null}
              </div>
              <h2>{report.title}</h2>
              <p>{report.summary}</p>
              <div className="tag-row">
                {report.tags.map((tag) => (
                  <span key={tag}>{tag}</span>
                ))}
              </div>
              <button type="button" onClick={() => setRouteReport(report.id)}>
                Report öffnen
              </button>
            </article>
          ))
        ) : (
          <section className="empty-state">
            Keine Reports für diese Filter.
          </section>
        )}
      </section>
    </main>
  );
}

function ReportDetail({ report, onBack }: { report: Report; onBack: () => void }) {
  return (
    <main className="app-shell">
      <button className="back-button" type="button" onClick={onBack}>
        Zur Übersicht
      </button>

      <article className="detail-layout">
        <aside className="detail-sidebar" aria-label="Reportdaten">
          <p className="eyebrow">{report.typeLabel}</p>
          {report.date ? <time dateTime={report.date}>{report.date}</time> : null}
          <dl>
            <div>
              <dt>Repo-Pfad</dt>
              <dd>{report.path}</dd>
            </div>
            {report.relatedMinistries.length ? (
              <div>
                <dt>Ministerien</dt>
                <dd>{report.relatedMinistries.join(", ")}</dd>
              </div>
            ) : null}
            {report.relatedLaws.length ? (
              <div>
                <dt>Gesetze</dt>
                <dd>{report.relatedLaws.join(", ")}</dd>
              </div>
            ) : null}
          </dl>
          {report.sourceUrls.length ? (
            <div className="source-list">
              <h2>Quellen</h2>
              {report.sourceUrls.map((url) => (
                <a href={url} key={url} rel="noreferrer" target="_blank">
                  Quelle öffnen
                </a>
              ))}
            </div>
          ) : null}
        </aside>

        <section className="report-document">
          {report.sankey ? <BudgetSankey data={report.sankey} /> : null}

          {report.metrics.length ? (
            <div className="metric-grid metric-grid--compact">
              {report.metrics.map((metric) => (
                <article className="metric-card" key={`${metric.label}-${metric.value}`}>
                  <p>{metric.label}</p>
                  <strong>{metric.value}</strong>
                </article>
              ))}
            </div>
          ) : null}
          <div dangerouslySetInnerHTML={{ __html: report.html }} />
        </section>
      </article>
    </main>
  );
}

function BudgetSankey({ data }: { data: SankeyData }) {
  const width = 1040;
  const rowGap = 18;
  const leftX = 34;
  const centerX = 488;
  const rightX = 832;
  const barWidth = 18;
  const labelOffset = 12;
  const maxRows = Math.max(data.income.length, data.spending.length);
  const chartHeight = Math.max(560, maxRows * 72);
  const topPadding = 22;
  const flowHeight = chartHeight - 72;
  const incomeTotal = sumValues(data.income);
  const spendingTotal = sumValues(data.spending);
  const total = Math.max(incomeTotal, spendingTotal);
  const scale = flowHeight / total;
  const centerTop = topPadding;
  const centerHeight = total * scale;
  const incomeLayout = stackEntries(data.income, scale, topPadding, rowGap);
  const spendingLayout = stackEntries(data.spending, scale, topPadding, rowGap);
  const incomeCenterOffsets = cumulativeOffsets(data.income, scale, centerTop);
  const spendingCenterOffsets = cumulativeOffsets(data.spending, scale, centerTop);
  const height = chartHeight + 118;

  return (
    <section className="sankey-section" aria-labelledby="sankey-title">
      <div className="sankey-header">
        <div>
          <p className="eyebrow">Sankey</p>
          <h2 id="sankey-title">{data.title}</h2>
        </div>
        <p>{data.note}</p>
      </div>

      <div className="sankey-scroll" role="img" aria-label={data.title}>
        <svg className="sankey-svg" viewBox={`0 0 ${width} ${height}`}>
          <defs>
            <linearGradient id="income-flow" x1="0" x2="1">
              <stop offset="0%" stopColor="#176b5b" stopOpacity="0.48" />
              <stop offset="100%" stopColor="#176b5b" stopOpacity="0.18" />
            </linearGradient>
            <linearGradient id="spending-flow" x1="0" x2="1">
              <stop offset="0%" stopColor="#b36b16" stopOpacity="0.18" />
              <stop offset="100%" stopColor="#b36b16" stopOpacity="0.48" />
            </linearGradient>
          </defs>

          {incomeLayout.map((entry, index) => (
            <g key={`income-${entry.label}`}>
              <path
                className="sankey-flow"
                d={curvePath(
                  leftX + barWidth,
                  entry.y + entry.height / 2,
                  centerX,
                  incomeCenterOffsets[index] + entry.height / 2,
                )}
                stroke="url(#income-flow)"
                strokeWidth={Math.max(1.5, entry.height)}
              />
            </g>
          ))}

          {spendingLayout.map((entry, index) => (
            <g key={`spending-${entry.label}`}>
              <path
                className="sankey-flow"
                d={curvePath(
                  centerX + barWidth,
                  spendingCenterOffsets[index] + entry.height / 2,
                  rightX,
                  entry.y + entry.height / 2,
                )}
                stroke="url(#spending-flow)"
                strokeWidth={Math.max(1.5, entry.height)}
              />
            </g>
          ))}

          <SankeyNode
            x={centerX}
            y={centerTop}
            width={barWidth}
            height={centerHeight}
            label={data.centerLabel}
            value={`${formatNumber(total)} ${data.unit}`}
            align="center"
          />

          {incomeLayout.map((entry) => (
            <SankeyNode
              key={entry.label}
              x={leftX}
              y={entry.y}
              width={barWidth}
              height={entry.height}
              label={entry.label}
              value={`${formatNumber(entry.value)} ${data.unit}`}
              align="left"
              labelOffset={labelOffset}
            />
          ))}

          {spendingLayout.map((entry) => (
            <SankeyNode
              key={entry.label}
              x={rightX}
              y={entry.y}
              width={barWidth}
              height={entry.height}
              label={entry.label}
              value={`${formatNumber(entry.value)} ${data.unit}`}
              align="right"
              labelOffset={labelOffset}
            />
          ))}
        </svg>
      </div>

      <div className="sankey-tables">
        <SankeyTable title="Einnahmen" entries={data.income} unit={data.unit} />
        <SankeyTable title="Ausgaben" entries={data.spending} unit={data.unit} />
      </div>
    </section>
  );
}

function SankeyNode({
  x,
  y,
  width,
  height,
  label,
  value,
  align,
  labelOffset = 12,
}: {
  x: number;
  y: number;
  width: number;
  height: number;
  label: string;
  value: string;
  align: "left" | "center" | "right";
  labelOffset?: number;
}) {
  const labelX = align === "right" ? x + width + labelOffset : align === "left" ? x - labelOffset : x + width / 2;
  const textAnchor = align === "right" ? "start" : align === "left" ? "end" : "middle";
  const textY = y + Math.max(14, height / 2 - 3);

  return (
    <g>
      <rect className="sankey-node" x={x} y={y} width={width} height={height} rx="5" />
      <text className="sankey-label" x={labelX} y={textY} textAnchor={textAnchor}>
        {label}
      </text>
      <text className="sankey-value" x={labelX} y={textY + 18} textAnchor={textAnchor}>
        {value}
      </text>
    </g>
  );
}

function SankeyTable({
  title,
  entries,
  unit,
}: {
  title: string;
  entries: SankeyEntry[];
  unit: string;
}) {
  return (
    <table>
      <caption>{title}</caption>
      <tbody>
        {entries.map((entry) => (
          <tr key={entry.label}>
            <th scope="row">{entry.label}</th>
            <td>{`${formatNumber(entry.value)} ${unit}`}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

function stackEntries(entries: SankeyEntry[], scale: number, startY: number, gap: number) {
  let cursor = startY;
  return entries.map((entry) => {
    const height = Math.max(3, entry.value * scale);
    const item = { ...entry, y: cursor, height };
    cursor += height + gap;
    return item;
  });
}

function cumulativeOffsets(entries: SankeyEntry[], scale: number, startY: number) {
  let cursor = startY;
  return entries.map((entry) => {
    const y = cursor;
    cursor += Math.max(3, entry.value * scale);
    return y;
  });
}

function curvePath(startX: number, startY: number, endX: number, endY: number) {
  const distance = Math.max(120, (endX - startX) * 0.55);
  return `M ${startX} ${startY} C ${startX + distance} ${startY}, ${endX - distance} ${endY}, ${endX} ${endY}`;
}

function sumValues(entries: SankeyEntry[]) {
  return entries.reduce((sum, entry) => sum + entry.value, 0);
}

function formatNumber(value: number) {
  return new Intl.NumberFormat("de-DE", {
    minimumFractionDigits: value < 10 ? 3 : 1,
    maximumFractionDigits: value < 10 ? 3 : 1,
  }).format(value);
}

function setRouteHome() {
  window.location.hash = "#/";
}

function setRouteReport(reportId: string) {
  window.location.hash = `#/reports/${encodeURIComponent(reportId)}`;
}

export default App;
