# Einrichtung ohne Terminal – Cowork, ChatGPT oder Browser

Du schreibst in Word, und daneben ist die KI offen. Damit sie deine Dateien lesen
und alles, was entsteht, direkt in deinem Ordner speichern kann, gibt es drei Wege.
**Weg 1 ist der beste**, Weg 3 der Notbehelf.

Für alle drei gilt: Lade diesen Ordner herunter (auf GitHub **Code → Download ZIP**),
entpacke ihn und leg ihn dorthin, wo du ihn wiederfindest – nicht in „Downloads“.
Das ist ab jetzt dein **ABA-Ordner**. Deine Word-Dateien legst du in `mein/arbeit/`.

---

## Weg 1: Claude Cowork (empfohlen)

Cowork ist Claude in der Desktop-App mit Zugriff auf einen Ordner auf deinem
Rechner. Claude liest dort deine Word-Dateien, legt neue an und speichert Stand,
Quellen, Recherche und Protokoll direkt bei dir.

1. **Skills hochladen.** Cowork lädt Skills aus deinem Claude-Konto, nicht aus dem
   Ordner. In Claude unter **Einstellungen → Fähigkeiten** „Code-Ausführung und
   Dateierstellung“ einschalten, dann unter **Skills** jede ZIP-Datei aus
   `fuer-die-app/skills/` hochladen. Das ist einmalig.
2. **Ordner freigeben.** In der Claude-Desktop-App Cowork öffnen und deinen
   ABA-Ordner auswählen – den ganzen Ordner, nicht nur `mein/`, weil die Skills die
   Regelwerke in `regeln/` lesen.
3. **Anfangen.** Erste Nachricht:

   > Lies CLAUDE.md und lass uns starten.

## Weg 2: ChatGPT Work (ChatGPT-Desktop-App)

ChatGPT Work kann in der Desktop-App auf einen lokalen Ordner zugreifen.

1. In der ChatGPT-Desktop-App ein **Projekt** anlegen und den Text aus
   `projektanweisung.md` (alles unterhalb der Trennlinie) in die **Anweisungen**
   des Projekts kopieren.
2. Deinem Projekt oder Gespräch den **ABA-Ordner freigeben**.
3. Erste Nachricht:

   > Lies CLAUDE.md in meinem Ordner und lass uns starten.

ChatGPT kennt die Skills nicht als Skills, liest sie aber als Anleitungen in
`.claude/skills/`, wenn du darauf hinweist („Arbeite nach
`.claude/skills/schreiben/SKILL.md`“).

## Weg 3: Im Browser (claude.ai oder chatgpt.com) – Notbehelf

Ohne Ordnerzugriff kann die KI nichts bei dir speichern. Du bekommst alles als Text
oder Datei zum Herunterladen und legst es selbst in deinen Ordner. Geht, ist aber
mühsamer, und was du nicht ablegst, ist nach dem Gespräch weg.

1. Ein **Projekt** anlegen (Claude: links **Projekte**; ChatGPT: **Neues Projekt**).
2. Den Text aus `projektanweisung.md` (alles unterhalb der Trennlinie) in die
   **Anweisungen** des Projekts kopieren. Er passt in die 8.000 Zeichen, die
   ChatGPT erlaubt.
3. Die fünf Dateien aus `wissen/` hochladen – fünf, weil ChatGPT im Gratis-Tarif
   genau fünf pro Projekt annimmt. In Claude kannst du zusätzlich die Skills aus
   `skills/` wie in Weg 1 hochladen.
4. Erste Nachricht: „Lass uns starten.“

**Was du selbst ablegen musst:** Am Ende jeder Sitzung bekommst du einen
Protokolleintrag und eine Übergabe für die nächste Sitzung. Beides in deinen
Ordner (`mein/begleitprotokoll.md`, `mein/uebergaben/`), und die aktualisierte
`5-meine-unterlagen.md` neu hochladen – die alte vorher löschen, sonst liegen zwei
Fassungen im Projekt.

---

## Welcher Weg wofür

- **Cowork oder ChatGPT Work:** alles wird lokal gespeichert, nichts geht verloren,
  Word-Dateien werden direkt gelesen und angelegt.
- **Browser:** funktioniert überall, aber du bist das Gedächtnis.
- **Claude Code** (Terminal): für alle, die das schon nutzen – Anleitung in der
  README.

**Führ das Begleitprotokoll wirklich mit.** Es ist Pflicht, es ist ein
Beurteilungskriterium, und es lässt sich rückwirkend nicht rekonstruieren.
