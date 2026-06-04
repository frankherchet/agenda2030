# Arbeitsregeln

Diese Regeln gelten für jede Arbeit in diesem Repo.

## Commit-Disziplin

Nach jedem fertiggestellten Arbeitspaket muss der aktuelle Stand gesichert
werden.

Pflichtschritte:

1. Alle veränderten, entfernten und hinzugefügten Dateien stagen.
2. Eine aussagekräftige Commit Message erzeugen.
3. Commit erstellen.
4. Commit auf das Remote-Repository pushen.

Das gilt unabhängig von der Art der Arbeit: Workflows, neue Dateien,
geänderte Konzepte, Dokumentation, Skills, Strukturänderungen,
Zusammenfassungen, Gesetzesvorschläge oder sonstige Inhalte.

Ziel ist eine lückenlose, nachvollziehbare History.

## Rechen-Disziplin

Zahlenbasierte Bewertungen und Modellrechnungen sollen nachvollziehbar im Repo
reproduzierbar sein. Sobald ein Reformvorschlag mehr als einfache
Quellenzitate verwendet, werden die Berechnungen bevorzugt als Skripte unter
`scripts/` abgelegt und ihre Ergebnisse als Markdown, CSV oder JSON im
passenden Fachordner gespeichert. Reports zitieren diese Rechenartefakte statt
Ergebnisse nur im Fließtext herzuleiten.

## Quellen-Disziplin

Jede externe Quelle muss vor ihrer fachlichen Nutzung zuerst im Eingang
erfasst werden.

Pflichtschritte:

1. Quelle als kompakte Markdown-Datei unter `eingang/<typ>/` anlegen.
   Gültige Typordner sind `dokumente/`, `links/` und `ideen/`.
2. Den neuen Eingang in `eingang/index/README.md` vermerken.
3. Erst danach darf die Quelle in Reports, Prüferberichten, Auswertungen,
   Skripten, Datenartefakten, Quellenkatalogen oder Zusammenfassungen
   verarbeitet oder zitiert werden.
4. Dateien mit externen Quellen müssen zusätzlich zu `source_urls` auch
   `ingest_refs` mit repo-relativen Pfaden zu den passenden Eingang-Dateien
   führen.

Ziel ist, dass jede verwendete Quelle token-sparend, auffindbar und
nachvollziehbar vorgeschaltet ist.
