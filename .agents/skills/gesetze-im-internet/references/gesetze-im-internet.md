# Gesetze im Internet

## Offizielle Einstiegsseiten

- Startseite: <https://www.gesetze-im-internet.de/>
- Titelsuche: <https://www.gesetze-im-internet.de/titelsuche.html>
- Volltextsuche: <https://www.gesetze-im-internet.de/volltextsuche.html>
- Hinweise zu Download und Weiterverwertung: <https://www.gesetze-im-internet.de/hinweise.html>
- Tagesaktuelles Inhaltsverzeichnis: <https://www.gesetze-im-internet.de/gii-toc.xml>

## Suche

### Titelsuche

- Formular-Endpoint: `/cgi-bin/htsearch`
- `config=Titel_bmjhome2005`
- `method=and|or`
- `words=<Suchbegriffe>`

### Volltextsuche

- Formular-Endpoint: `/cgi-bin/htsearch`
- `config=Gesamt_bmjhome2005`
- `method=and|or`
- `words=<Suchbegriffe>`

## Download

Das Portal stellt die konsolidierten Normen in mehreren Formaten bereit:

- HTML
- PDF
- EPUB
- XML

Für Codex ist die XML-Fassung die bevorzugte Quelle, weil sie sich
maschinenlesbar verarbeiten lässt.

### XML-Zip

Für jede Normfamilie gibt es ein Zip-Archiv:

```text
https://www.gesetze-im-internet.de/<slug>/xml.zip
```

Im Archiv liegt die normierte XML-Fassung der Gesamtvorschrift. Das Archiv kann
direkt heruntergeladen und für Markdown-Export, Normauszug oder Textanalyse
verwendet werden.

### Einzelnormen

Einzelne Normen sind als HTML-Seiten abrufbar. Je nach Rechtsquelle kann die
Pfadform variieren. Häufige Muster sind:

- `https://www.gesetze-im-internet.de/<slug>/__<nummer>.html`
- `https://www.gesetze-im-internet.de/gg/art_<nummer>.html`

Wenn der exakte Normlink unklar ist, zuerst die Suche oder die XML-Fassung
verwenden.

## Empfohlener Workflow

1. Thema oder Normbegriff mit Titelsuche oder Volltextsuche eingrenzen.
2. Passenden `slug` aus dem Treffer ableiten.
3. `xml.zip` laden.
4. Aus dem XML einen Markdown-Ingest oder einen Normstand erzeugen.
5. Die erzeugte Datei mit `source_urls` und `ingest_refs` in die Repo-Struktur
   einhängen.

## Repo-Zuordnung

- Ingests: `ingest/links/` oder `ingest/dokumente/`
- Normstände: `gesetzbuecher/`
- Beispiel-Ingests:
  - `ingest/links/2026-06-04-gesetze-im-internet-sgb-vi.md`
  - `ingest/links/2026-06-07-gesetze-im-internet-bho.md`
- Beispiel-Normstände:
  - `gesetzbuecher/sgb/sgb-vi-paragraf-213-stand-2026-06-05.md`
  - `gesetzbuecher/grundgesetz/gg-artikel-3-stand-2026-06-05.md`

## Hinweise

- Die XML-Fassung ist für maschinelle Verarbeitung die beste Basis.
- Für reine Browserprüfung genügt die HTML-Seite; für Faktenarbeit und lokale
  Markdown-Dateien die XML-Fassung.
- Immer die amtliche Portal-URL als `source_urls` erhalten.
