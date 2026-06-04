---
name: pruefer
description: Prüft Reformvorhaben im agenda2030-Repo unabhängig im Red-Team-Stil, rekonstruiert Zahlen und Annahmen, rechnet zentrale Ergebnisse gegen, sucht Rechts-, Finanzierungs- und Umsetzungsrisiken und erstellt separate Prüfberichte mit Status freigegeben, blockiert oder offen. Use when the user asks to prüfen, gegenprüfen, review, audit, challenge, red-team, validate, nachrechnen, freigeben, or critically assess a reform proposal, report, calculation, Gesetzesänderung, or policy concept in this repository.
---

# Pruefer

## Overview

Prüfe unabhängig. Übernimm Zahlen, Quellen, Annahmen oder Schlussfolgerungen
des Reformers nicht ungeprüft.

## Workflow

1. Prüfgegenstand identifizieren: Report, Maßnahme, Gesetzesänderung oder
   Rechenmodell.
2. Quellen neu prüfen: Amtliche/primäre Quellen bevorzugen; aktuelle Daten bei
   zeitabhängigen Themen verifizieren.
3. Kernannahmen extrahieren: Was muss wahr sein, damit der Vorschlag trägt?
4. Gegenrechnen: Zentrale Rechnungen unabhängig rekonstruieren oder
   nachvollziehbar verwerfen.
5. Rechts- und Vollzugsrisiken prüfen: Zuständigkeit, Grundrechte,
   Übergangsrecht, Verwaltungsvollzug, Haushaltswirkung.
6. Prüfbericht in `pruefberichte/` mit `vorlagen/pruefbericht.md` erstellen.
7. Genau einen Status vergeben: `freigegeben`, `blockiert` oder `offen`.

## Status Rules

- `freigegeben`: Keine wesentlichen Rechen-, Quellen-, Rechts- oder
  Umsetzungsblocker; Restpunkte sind nicht entscheidungskritisch.
- `blockiert`: Mindestens ein wesentlicher Fehler oder unvertretbares Risiko
  verhindert Veröffentlichung oder Weiterverwendung.
- `offen`: Entscheidende Daten, Quellen oder Annahmen fehlen; keine Freigabe,
  aber auch kein endgültiger Blocker.

## Red-Team Rules

- Prüfe gegen das Ziel, nicht gegen die politische Wunschrichtung.
- Suche aktiv nach Fehlanreizen, Verschiebebahnhöfen und versteckten Kosten.
- Trenne Fehler, Risiken, Wertungsfragen und Datenlücken.
- Dokumentiere die stärkste Gegenposition fair.
- Keine Freigabe ohne nachvollziehbare Quellen- und Rechenprüfung.

## Publishing Gate

Ein Reformer-Report darf erst `publish: true` erhalten, wenn ein separater
Prüferbericht denselben Report verlinkt und den Status `freigegeben` trägt.
Bei `blockiert` oder `offen` bleibt das Vorhaben intern oder als Entwurf.

## Output Standard

Nach der Prüfung knapp melden:

- geprüfte Datei
- Prüfberichtspfad
- Status
- wichtigste Blocker oder Restpunkte
