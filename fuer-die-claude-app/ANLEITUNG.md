# Einrichtung in der Claude-App (ohne Terminal)

Für alle, die Claude im Browser oder in der normalen Claude-App benutzen –
claude.ai. Einmal einrichten, danach arbeitest du genauso wie mit Claude Code.

Dauer: etwa fünf Minuten.

---

## Schritt 1: Ein Projekt anlegen

In der Claude-App links auf **Projekte**, dann **Neues Projekt**.

Name: zum Beispiel „Meine ABA" oder der Titel deiner Arbeit.

Ein Projekt ist ein eigener Arbeitsbereich, der sich Anweisungen und Dateien
merkt. Alle Gespräche darin kennen dieselben Regeln – deshalb dieser Weg und
nicht ein einzelner Chat.

## Schritt 2: Die Anweisung einfügen

Im Projekt gibt es ein Feld für **Projektanweisungen** (je nach Version auch
„Anweisungen anpassen" oder „Custom instructions").

Öffne die Datei **`projektanweisung.md`** in diesem Ordner, kopiere den
**gesamten** Text und füge ihn dort ein. Speichern.

Das ist der wichtigste Schritt. Der Text enthält die Regeln, an die Claude sich
in diesem Projekt hält.

## Schritt 3: Die Regelwerke hochladen

Im Projekt gibt es einen Bereich für **Projektwissen** (oder „Dateien").

Lade dort **alle Dateien aus dem Ordner `regeln/`** hoch – es sind vierzehn
Markdown-Dateien. Du kannst sie in einem Zug markieren und gemeinsam
hineinziehen.

Diese Dateien enthalten das Fachwissen: Aufbau, Zitieren, Fristen,
Beurteilungsraster, KI-Kennzeichnung. Claude sucht sich daraus, was zur Frage
gehört.

## Schritt 4: Deine eigenen Dateien anlegen

Lade zusätzlich diese vier Dateien aus dem Ordner `mein/` hoch:

- `profil.md`
- `schulvorgaben.md`
- `begleitprotokoll.md`
- `quellen.md`

Sie sind noch leer beziehungsweise mit Platzhaltern gefüllt. Das ist richtig so.

## Schritt 5: Anfangen

Neues Gespräch im Projekt, erste Nachricht:

> Lass uns starten.

Claude stellt dir drei Fragen und schreibt dir den ausgefüllten Profiltext.

---

## Der eine Unterschied, den du kennen musst

**Claude kann in der App deine Dateien nicht selbst ändern.** Es kann sie lesen,
aber nicht speichern. In Claude Code schreibt Claude das Begleitprotokoll direkt
in die Datei – hier bekommst du den Text und musst ihn selbst einfügen.

Praktisch heißt das:

1. Claude gibt dir am Ende einer Sitzung den fertigen Protokolleintrag.
2. Du kopierst ihn in deine eigene Datei – im Texteditor, in Word, in Notion,
   wo du magst.
3. Wenn sich am Profil etwas ändert (Zitierstil, Termine, Forschungsfrage), lädst
   du die aktualisierte Datei neu ins Projektwissen hoch. Die alte vorher löschen,
   sonst stehen zwei Fassungen darin und Claude weiß nicht, welche gilt.

**Führe das Begleitprotokoll wirklich mit.** Es ist Pflicht, es ist ein
Beurteilungskriterium, und es lässt sich rückwirkend nicht rekonstruieren. Der
zusätzliche Kopierschritt ist lästig – ein leeres Protokoll im Februar ist
teurer.

## Was in der App fehlt

- **Die Kurzbefehle** (`thema`, `kritik`, `abgabe` …) sind in der App nicht
  eingerichtet. Schreib stattdessen in normalen Sätzen, was du willst: „Ich will
  an meiner Forschungsfrage arbeiten" oder „Prüf bitte mein Kapitel 3." Die
  Projektanweisung sagt Claude, wie es dann vorgeht.
- **Das Prüfwerkzeug** `werkzeuge/text-pruefen.py` läuft nicht. Claude kann die
  Prüfung stattdessen selbst durchführen, wenn du den Text einfügst – es zählt
  dann nicht ganz so genau nach, findet aber dieselben Muster.

Alles Übrige funktioniert gleich.

---

## Wenn du später doch umsteigst

Der Wechsel zu Claude Code kostet nichts: Der Ordner ist derselbe. Du kopierst
deine ausgefüllten Dateien nach `mein/` zurück und arbeitest weiter.
