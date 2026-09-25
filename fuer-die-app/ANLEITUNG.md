# Einrichtung ohne Installation – Claude oder ChatGPT

Für alle, die im Browser oder in der normalen App arbeiten: claude.ai oder
chatgpt.com. Einmal einrichten, danach kennt jedes Gespräch im Projekt die
Regeln. Dauer: etwa fünf Minuten.

Du brauchst aus diesem Ordner nur zwei Dinge:

- **`projektanweisung.md`** – der Text, der die KI zur Begleitung macht
- **den Ordner `wissen/`** – fünf Dateien: vier Pakete mit allen Regelwerken
  und `5-meine-unterlagen.md` für dein Profil, deine Schulvorgaben, dein
  Begleitprotokoll und deine Quellen

Fünf Dateien, weil ChatGPT im Gratis-Tarif genau fünf pro Projekt annimmt. In
Claude geht es genauso.

---

## Schritt 1: Ein Projekt anlegen

- **Claude:** links **Projekte** → **Neues Projekt**.
- **ChatGPT:** in der Seitenleiste **Neues Projekt**.

Name: zum Beispiel „Meine ABA“. Ein Projekt merkt sich Anweisungen und Dateien
über alle Gespräche hinweg – deshalb dieser Weg und nicht ein einzelner Chat.

## Schritt 2: Die Anweisung einfügen

Öffne `projektanweisung.md`, kopiere **alles unterhalb der Trennlinie** und füge
es ein:

- **Claude:** im Projekt bei **Projektanweisungen** („Anweisungen festlegen“).
- **ChatGPT:** im Projekt über das Menü oben → **Anweisungen**.

Das ist der wichtigste Schritt. Der Text passt in die 8.000 Zeichen, die ChatGPT
erlaubt.

## Schritt 3: Die fünf Dateien hochladen

Alle fünf Dateien aus `wissen/` ins Projekt ziehen – bei Claude ins
**Projektwissen**, bei ChatGPT zu den **Dateien** des Projekts.

## Schritt 4: Anfangen

Neues Gespräch im Projekt, erste Nachricht:

> Lass uns starten.

Du bekommst drei kurze Fragen, danach den ausgefüllten Profiltext zum Kopieren –
und gleich einen ersten echten Schritt an deiner Arbeit.

---

## Der eine Unterschied zu Claude Code

**In der App kann die KI deine Dateien lesen, aber nicht speichern.** Profil und
Begleitprotokoll bekommst du deshalb als Text, den du selbst einfügst.

1. Am Ende einer Sitzung bekommst du den Protokolleintrag. Kopier ihn in deine
   eigene Fassung von `5-meine-unterlagen.md` (oder in Word, Notion, wo du magst).
2. Ändert sich etwas am Profil – Zitierstil, Termine, Forschungsfrage –, lade die
   aktualisierte `5-meine-unterlagen.md` neu hoch und **lösch die alte vorher**.
   Sonst liegen zwei Fassungen im Projekt, und die KI weiß nicht, welche gilt.

**Führ das Begleitprotokoll wirklich mit.** Es ist Pflicht, es ist ein
Beurteilungskriterium, und es lässt sich rückwirkend nicht rekonstruieren. Der
Kopierschritt ist lästig – ein leeres Protokoll im Februar ist teurer.

## Was in der App fehlt

- **Die Kurzbefehle** (`thema`, `kritik`, `abgabe` …). Schreib stattdessen in
  normalen Sätzen, was du willst: „Ich will an meiner Forschungsfrage arbeiten“
  oder „Prüf bitte mein Kapitel 3.“
- **Das Prüfwerkzeug** `werkzeuge/text-pruefen.py`. Die KI prüft den eingefügten
  Text dann selbst – Muster findet sie, genau zählen kann sie nicht. Zahlen wie
  Satzlängen sind dort nur Schätzungen.

## Wenn du später umsteigst

Der Wechsel zu Claude Code kostet nichts. Du überträgst deine Einträge aus
`5-meine-unterlagen.md` zurück in die einzelnen Dateien in `mein/` und arbeitest
weiter.
