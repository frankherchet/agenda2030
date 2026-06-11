---
name: gesetze-im-internet
description: Offizielle Gesetze-im-Internet-Recherche mit Titelsuche, Volltextsuche, XML-Zip-Download und Markdown-Export für agenda2030. Use when Codex needs to search, fetch, download, or convert German federal laws and regulations from gesetze-im-internet.de into ingest files or normstand Markdown files.
---

# Gesetze im Internet

## Zweck

Nutze dieses Skill, wenn du Bundesrecht auf `gesetze-im-internet.de`
effizient finden und lokal als Markdown sichern willst. Bevorzugt wird die
amtliche XML-Fassung, weil sie für automatisierte Verarbeitung und lokale
Weiterverarbeitung am besten taugt.

## Arbeitsweise

1. Wenn der Nutzer einen konkreten Titel, eine Abkürzung oder eine Norm nennt,
   zuerst die Titelsuche oder das Inhaltsverzeichnis des Portals nutzen.
2. Wenn der Nutzer nur ein Thema oder einen Suchbegriff nennt, zuerst die
   Volltextsuche nutzen und dann den Treffer auf den passenden Normbaum
   zurückführen.
3. Den Treffer nicht aus HTML abschreiben, sondern die offizielle XML-Zip
   laden und daraus Markdown erzeugen.
4. Für `agenda2030` immer zuerst den Rohfund als Ingest oder Normstand im Repo
   ablegen, dann erst daraus in Analysen oder Projekten weiterarbeiten.

## Standardwerkzeuge

- `scripts/gii_fetch.py search-title <query>`: Titel- und Abkürzungssuche über
  das offizielle Inhaltsverzeichnis `gii-toc.xml`.
- `scripts/gii_fetch.py search-text <query>`: Volltextsuche über das offizielle
  `htsearch`-Formular.
- `scripts/gii_fetch.py ingest <slug> --output <pfad>.md`: kompakten
  Ingest-Entwurf aus der amtlichen XML-Fassung schreiben.
- `scripts/gii_fetch.py norm <slug> --norm <nummer> --output <pfad>.md`:
  Normstand-Datei oder Normauszug aus der XML-Fassung schreiben.

## Repo-Ziele

- Für eine Quelle zuerst einen Ingest unter `ingest/links/` oder
  `ingest/dokumente/` erzeugen.
- Für einzelne Paragraphen oder Artikel danach eine Normstand-Datei unter
  `gesetzbuecher/` ausgeben.
- In beiden Fällen `source_urls` und passende `ingest_refs` setzen.
- Bei Rechtsanalysen die relevante Ingest-Datei und die Normstand-Datei im
  Artefakt verlinken.

## Ausgabeform

Halte die erzeugten Markdown-Dateien knapp und reproduzierbar:

- Metadaten mit Quelle, Abrufdatum, Fassungsstand und Downloadpfad
- kurz gefasste Inhaltsinventur
- ausgewählte, aktuell relevante Informationen
- offene Fragen oder Folgepunkte, wenn die Norm noch nicht vollständig
  eingeordnet ist

## Referenz

Siehe [references/gesetze-im-internet.md](references/gesetze-im-internet.md)
für die konkreten Portal-URLs, Suchparameter und Downloadpfade.
