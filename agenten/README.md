# Agenten

Dieses Repo nutzt zwei unabhängige Rollen für Reformarbeit.

## Reformer

Der Reformer arbeitet Reformvorhaben aus. Er recherchiert Rechtsgrundlagen,
sammelt aktuelle Zahlen, beschreibt Maßnahmen und berechnet finanzielle
Wirkungen. Seine Artefakte sind Vorschläge, keine Freigaben.

Skill: `skills/reformer/`

## Prüfer

Der Prüfer arbeitet unabhängig im Red-Team-Stil. Er prüft Quellen,
rekonstruiert Rechnungen, sucht Gegenargumente und dokumentiert Blocker oder
Freigabe in einem separaten Prüfbericht.

Skill: `skills/pruefer/`

## Workflow

1. Reformer erstellt ein Reformvorhaben mit `publish: false`.
2. Prüfer erstellt einen separaten Prüfbericht in `pruefberichte/`.
3. Der Prüfbericht erhält genau einen Status:
   - `freigegeben`
   - `blockiert`
   - `offen`
4. `publish: true` ist erst zulässig, wenn ein verlinkter Prüfbericht
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
