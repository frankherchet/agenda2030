---
title: Gesamtstatus des Reformvorhabens Rentenversicherung (Stand 09.06.2026)
date: 2026-06-09
type: reformdokument
status: arbeitsfassung
publish: false
source_urls:
  - https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Statistiken-und-Berichte/statistikpublikationen/statistikband_rente.pdf?__blob=publicationFile&v=5
  - https://statistik-rente.de/drv/extern/rente/rentenbestand/
  - https://rentenupdate.drv-bund.de/SharedDocs/Dokumente/2025/10_Bundeszuschuesse_nbL/rentenupdate_10_Bundeszuschuesse_nbL_lang.pdf?__blob=publicationFile&v=4
  - https://www.bmas.de/SharedDocs/Downloads/DE/Rente/rentenversicherungsbericht-2025.pdf?__blob=publicationFile&v=3
  - https://www.gesetze-im-internet.de/sgb_6/__213.html
ingest_refs:
  - ingest/dokumente/2026-06-04-drv-statistikband-rente-2024.md
  - ingest/links/2026-06-04-statistik-rente-rentenbestand.md
  - ingest/dokumente/2026-06-05-drv-rentenupdate-bundeszuschuesse-nicht-beitragsgedeckte-leistungen-2025.md
  - ingest/dokumente/2026-06-05-bmas-rentenversicherungsbericht-2025.md
  - ingest/links/2026-06-04-gesetze-im-internet-sgb-vi.md
related_project:
  - projekte/rentenversicherung/reformkonzept.md
---

# Gesamtstatus des Reformvorhabens Rentenversicherung

## Kurzfassung

Der Stand vom 2026-06-09 dokumentiert Folgearbeiten nach der
Viertnachpruefung. Dazu gehoeren ein Negativbefund zur fehlenden amtlichen
Bundesmittel-Ist-Zweckzerlegung, Anfrageentwuerfe an DRV und BMF sowie eine
heuristische Arbeitsfassung fuer den Rentenzugangskorridor 67 bis 72 Jahre.
Das Reformvorhaben bleibt fachlich `offen`. Externe Freigabehindernisse
bestehen fort.

---

## 1. Stand der Folgearbeiten

### 1.1 Punkt 1: DRV-Datenanfrage (Rente 67–72)
**Status:** als Entwurf vorbereitet
**Datei:** `projekte/rentenversicherung/2026-06-09-datenanfrage-drv.md`
**Was wurde getan:**
- Formale, strukturierte Anfrage als sendefaehiger Entwurf vorbereitet
- Gefordert: altersscharfe Rentenzugänge 67–72 Jahre, Abschläge, Erwerbsminderungsrenten
- Anfragefrist: 31.07.2026
- Hinweis: Im Repo ist kein Versandnachweis dokumentiert

**Nächster Schritt:** Versand dokumentieren; nach Eingang Daten den
Szenariokorridor neu untersetzen.

---

### 1.2 Punkt 2: Bundesmittel-Ist-Zweckzerlegung 2024–2026
**Status:** als Negativbefund dokumentiert; Anfrageentwurf vorbereitet
**Dateien:** 
- `projekte/rentenversicherung/2026-06-09-bundesmittel-zweckzerlegung.md`
- `projekte/rentenversicherung/2026-06-09-datenanfrage-bundesmittel-zweckzerlegung.md`

**Was wurde getan:**
- Recherche nach öffentlich verfügbarer amtlicher Zweckzerlegung durchgeführt
- **Ergebnis:** Keine öffentliche Datenquelle verfügbar (Bundeszuschuss wird aggregiert ausgewiesen)
- Formale Anfrage an BMF und DRV als Entwurf vorbereitet
- Negativbefund dokumentiert

**Nächster Schritt:** Versand dokumentieren; Rueckmeldung auswerten; keine
eigene Ist-Zweckzerlegung behaupten.

---

### 1.3 Punkt 3: Rückgriffsmechanismus für den vorgeschlagenen Ausbau von § 213 SGB VI
**Status:** als Arbeitsfassung bearbeitet
**Datei:** `gesetzbuecher/sgb/sgb-vi-rechtsverordnung-213a-rueckgriff-stand-2026-06-09.md`  
**Was wurde getan:**
- Vollständige Rechtsverordnung entworfen, die den Rückgriff konkretisiert
- Regelungen zu:
  - Anwendungsbereich (wann Ausfallhaftung greift)
  - Voraussetzungen (Zahlungsverzug > 30 Tage)
  - Umfang (Übernahme ausstehender Rentenzahlungen)
  - Verfahren (Mitteilung, Einsprachefrist 4 Wochen)
  - Lastenverteilung (Bundeszuschuss zahlt, keine Quersubvention)
  - Inkrafttreten (rückwirkend mit Gesetz)

**Rechtliche Bewertung:** Vorlage ist arbeitsfaehig, aber noch nicht als
abschliessende Loesung freigegeben.

**Nächster Schritt:** Mit dem Prueferbericht und dem Artikelgesetz
abgleichen; Restpunkte zu Rueckgriff und Lastenverteilung offen halten.

---

### 1.4 Punkt 4: Szenariokorridor 67–72 mit Sensitivität
**Status:** als heuristische Arbeitsfassung bearbeitet
**Dateien:**
- `projekte/rentenversicherung/2026-06-09-szenariokorridor-67-72.md`
- `analysen/daten/drv_rentenzugang_67-72_final.csv` (Daten)

**Was wurde getan:**
- Drei-Szenario-Sensitivitätsanalyse als Arbeitsstand erstellt
- Datenbasis: BMAS Rentenbestandsstatistik 2025 + empirische DRV-Publikationen
- **Kernerkenntnisse:**
  - Ab 70 Jahren dominiert Erwerbsminderungsrente (56% bei 72 Jahren), nicht Altersrente
  - Altersrente-Quote sinkt von 48% (Alter 67) auf 21% (Alter 72)
  - Durchschnittliche Abschläge steigen von 4,8% auf 6,1%
  - Kostenwirkung: –6,4% bis +9,2% je nach Szenario

- **Datenmethode:** Keine echte DRV-Zugangsstatistik im Repo verfuegbar;
  die CSV ist eine heuristische Bruecke und keine amtliche Endgrundlage.
- **Status:** Arbeitsbasis fuer Diskussion; finale Validierung wartet auf
  echte DRV-Daten

**Nächster Schritt:** Nach Eingang DRV-Antwort empirische Daten einsetzen und Szenariokorridor ggf. nachjustieren.

---

## 2. Externe Abhängigkeiten

| Punkt | Blockiert | Anfrage-Status | Frist | Status |
|---|---|---|---|---|
| DRV-Rentenzugänge 67–72 | Validierung des Szenariokorridors | Entwurf vorbereitet | 31.07.2026 | offen extern |
| Bundesmittel-Ist-Zweckzerlegung | Finanzwirkungsanalyse | Entwurf vorbereitet | offen | offen extern |

**Bewertung:**
- Keine neuen internen Rechen- oder Dokumentationsblocker aus diesen
  Folgearbeiten.
- Die externe Freigabelage bleibt offen, weil DRV-Daten und amtliche
  Bundesmittel-Ist-Zweckzerlegung weiter fehlen.
- Die Anfrageentwuerfe sind brauchbar, aber nicht dasselbe wie dokumentierter
  Versand oder vorhandene Daten.

---

## 3. Reformer-Artefakte im Repository

### Arbeitsfassungen
- ✅ `gesetzbuecher/sgb/sgb-vi-artikelgesetz-213a-stand-2026-06-09.md`
- ✅ `gesetzbuecher/sgb/sgb-vi-rechtsverordnung-213a-rueckgriff-stand-2026-06-09.md`

### Reformkonzept und Maßnahmen
- ✅ `projekte/rentenversicherung/reformkonzept.md` (Hauptdokument, publish: false)
- ✅ `projekte/rentenversicherung/2026-06-09-szenariokorridor-67-72.md` (heuristische Sensitivität, publish: false)

### Datenstütze
- ✅ `analysen/daten/drv_rentenzugang_67-72_final.csv` (heuristische Arbeitsdatei)
- ✅ `scripts/calc_rentenalter_genesis_empirisch.py` (Grundlagen Szenariokorridor)

### Datenerfassungen und Anfragen
- ✅ `2026-06-09-datenanfrage-drv.md` (DRV-Anfrageentwurf)
- ✅ `2026-06-09-datenanfrage-bundesmittel-zweckzerlegung.md` (BMF-/DRV-Anfrageentwurf)
- ✅ `2026-06-09-bundesmittel-zweckzerlegung.md` (Negativbefund)
- ✅ `2026-06-09-status-offene-pruefpunkte.md` (Statusuebersicht)

### Prüfberichte
- ✅ `pruefberichte/2026-06-09-pruefbericht-rentenversicherung.md` (Aktueller Stand: offen)

---

## 4. Einordnung zum Reformer-Workflow

Nach der Reformer-SKILL.md (`.agents/skills/reformer/SKILL.md`):

| Schritt | Abgeschlossen | Dateien |
|---|---|---|
| 1. Ziel & Status quo klären | ✅ | reformkonzept.md |
| 2. Quellen nutzen | teilweise | Quellen vorhanden, Folgearbeiten mussten formal bereinigt werden |
| 3. Arbeitsfassungen sichern | ✅ | sgb-vi-artikelgesetz-213a, sgb-vi-rechtsverordnung-213a |
| 4. Reformmodell ausarbeiten | teilweise | szenariokorridor als Arbeitsfassung, nicht als Endmodell |
| 5. Rechnen | teilweise | heuristische CSV vorhanden, amtliche Validierung offen |
| 6. Artefakt erzeugen | ✅ | Folgearbeiten und Statusdokumente angelegt |
| 7. Veröffentlichung sperren | ✅ | Alle neuen Artefakte: publish: false |

**Qualitätsstatus:** Folgearbeiten angelegt, aber nicht alle Punkte sind
fachlich oder formal abgeschlossen.

---

## 5. Prüfer-Status

**Aktueller Prüfbericht:** `pruefberichte/2026-06-09-pruefbericht-rentenversicherung.md`  
**Status:** `offen`  
**Begründung (Prüfer):** Die Folgearbeiten sind sinnvoll, aber offene
Datengrundlagen und nicht dokumentierter Versand der Anfragen verhindern eine
abschliessende Freigabe.

**Empfehlung des Prüfers:** Nach Eingang der angefragten Daten Fünftnachprüfung durchführen.

---

## 6. Handlungsempfehlung

1. Anfrageentwürfe mit echten Ansprechpartnern ergänzen und Versand
   dokumentieren.
2. Nach Eingang DRV-Daten die heuristische CSV und den Szenariokorridor
   ersetzen oder validieren.
3. Nach Eingang einer amtlichen Bundesmittel-Antwort den Negativbefund
   aktualisieren.
4. Erst danach eine weitere Nachprüfung auslösen.

---

## 7. Qualitätsmerkmale dieser Reformer-Arbeit

- Die Folgearbeiten decken die offenen Themenfelder ab.
- Die Statussprache darf aber nicht ueber den dokumentierten Stand
  hinausschiessen.
- Heuristische Daten und Anfrageentwuerfe sind brauchbare Zwischenstufen,
  aber kein Ersatz fuer echte Eingangsdaten oder nachgewiesenen Versand.

---

## 8. Abschluss

## Abschluss

Die 2026-06-09-Dateien sind als Folgearbeiten sinnvoll, aber sie markieren
keinen abgeschlossenen Endzustand. Der saubere Zwischenstand lautet:

- Reformkonzept bleibt intern und offen.
- Rechts- und Haushaltsfolgen sind als Arbeitsfassungen weiter konkretisiert.
- Der Rentenzugangskorridor 67 bis 72 bleibt heuristisch.
- DRV- und BMF-Daten bleiben externe Freigabehindernisse.

---

Die konkrete Commit-Historie ist ueber `git log` nachvollziehbar und wird hier
nicht als fachlicher Statusersatz gefuehrt.
