# Agenten

Dieses Repo nutzt mehrere unabhängige Rollen für Quellenarbeit, Analyse,
Reformarbeit und Prüfung.

## Analyse

Die Analyse-Rolle arbeitet ein Thema quellenbasiert auf. Sie sucht relevante
Quellen, erfasst externe Quellen zuerst im Ingest und erstellt strukturierte
Faktenüberblicke unter `analysen/`. Sie entwirft noch keine Reform und vergibt
keine Freigabe.

Skill: `.agents/skills/analyse/`

## Reformer

Der Reformer arbeitet Reformvorhaben aus. Er recherchiert Rechtsgrundlagen,
sammelt aktuelle Zahlen, beschreibt Maßnahmen und berechnet finanzielle
Wirkungen. Seine Artefakte sind Vorschläge, keine Freigaben.

Skill: `.agents/skills/reformer/`

## Prüfer

Der Prüfer arbeitet unabhängig im Red-Team-Stil. Er prüft Quellen,
rekonstruiert Rechnungen, sucht Gegenargumente und dokumentiert Blocker oder
Freigabe in einem separaten Prüfbericht.

Skill: `.agents/skills/pruefer/`

## Workflow

1. Analyse erstellt bei Bedarf einen quellenbasierten Faktenüberblick unter
   `analysen/`.
2. Reformer erstellt daraus oder daneben ein Reformvorhaben mit
   `publish: false`.
3. Prüfer erstellt einen separaten Prüfbericht im passenden Projekt unter
   `projekte/<projekt>/pruefberichte/`.
4. Der Prüfbericht erhält genau einen Status:
   - `freigegeben`
   - `blockiert`
   - `offen`
5. `publish: true` ist erst zulässig, wenn ein verlinkter Prüfbericht
   `freigegeben` ist.

## Rechenstandard

Jede wesentliche Berechnung braucht:

- Datenquelle
- Stichtag
- Formel
- Annahmen
- Ergebnis
- Sensitivität oder Gegenannahme

Der Prüfer muss zentrale Rechnungen unabhängig nachrechnen oder begründet
verwerfen.
