# Start hier

Für alle, die noch nie mit Claude gearbeitet haben. Zehn Minuten, dann läuft es.

---

## Was du brauchst

Ein Claude-Konto und diesen Ordner. Sonst nichts.

Es gibt zwei Wege. **Weg A ist der bequemere**, wenn du dich traust, ein Programm
zu installieren. **Weg B** braucht keine Installation, nur einen Browser.

---

## Weg A: Claude Code

Claude Code ist Claude mit Zugriff auf einen Ordner auf deinem Rechner. Der
Vorteil: Es liest deine Dateien selbst, schreibt ins Begleitprotokoll und findet
die Regelwerke von allein. Es gibt Claude Code als Desktop-App und als
Terminal-Programm – beides funktioniert.

### 1. Diesen Ordner auf den Rechner holen

Auf der GitHub-Seite oben rechts auf den grünen Knopf **Code**, dann **Download
ZIP**. Entpacken, irgendwohin legen, wo du ihn wiederfindest. Nicht in den
Downloads-Ordner – da wird er irgendwann aufgeräumt.

Wer Git kennt: `git clone` tut es auch.

### 2. Claude Code öffnen und den Ordner auswählen

In der Desktop-App: Ordner öffnen, den entpackten Ordner auswählen.
Im Terminal: in den Ordner wechseln und `claude` eintippen.

### 3. Losschreiben

Erste Nachricht:

> Lass uns starten.

Claude stellt drei Fragen, füllt `mein/profil.md` aus und sagt, was als Nächstes
dran ist. Fertig.

### Was du danach tippen kannst

Es sind keine Befehle, die man auswendig lernen muss – normale Sätze
funktionieren genauso. Aber diese Wörter treffen direkt:

- `thema` – an der Forschungsfrage arbeiten
- `quellen` – eine Quelle prüfen und aufnehmen
- `gliederung` – Kapitel ordnen
- `schreiben` – an einem Kapitel arbeiten
- `kritik` – ein fertiges Kapitel prüfen lassen
- `protokoll` – Eintrag fürs Begleitprotokoll
- `abgabe` – Endkontrolle
- `pruefung` – Präsentation und Diskussion üben

---

## Weg B: Claude im Browser (claude.ai)

Funktioniert ohne Installation. Einmal einrichten, danach ist es fast dasselbe.

Die Anleitung dafür steht in **fuer-die-claude-app/ANLEITUNG.md**. Kurz: ein
Projekt anlegen, einen vorbereiteten Text in die Projektanweisungen kopieren, die
Regelwerke ins Projektwissen hochladen.

---

## Die drei Dateien, die dir gehören

Alles, was du schreibst, liegt in `mein/`:

- **`profil.md`** – wer du bist, was du schreibst, welcher Zitierstil, welche
  Termine. Claude liest das bei jedem Start. Ändert sich etwas, ändere es hier.
- **`begleitprotokoll.md`** – dein Logbuch. Pflicht, Beurteilungskriterium, und
  rückwirkend nicht zu erfinden. Nach jeder Sitzung ein Eintrag.
- **`quellen.md`** – alles, was du zitieren willst, mit der Angabe, wann du es
  selbst geprüft hast.

Dazu `arbeitsstand.md` für den Überblick und `arbeit/` für die Kapitel, falls du
den Text hier schreiben willst. Musst du nicht – wer lieber in Word schreibt,
kopiert zum Prüfen einzelne Kapitel herein oder legt die Datei daneben.

---

## Was du wissen solltest, bevor du anfängst

**Du bekommst keine fertigen Kapitel.** Das ist kein Versehen. Sieben der
dreizehn Beurteilungskriterien werden mündlich geprüft – vor einer Kommission,
die nachfragt, warum du etwas so geschrieben hast. Ein Absatz, den du nicht
selbst gedacht hast, kostet dich dort mehr, als er dir jetzt erspart.

**KI-Nutzung ist erlaubt, aber sie muss dokumentiert und gekennzeichnet werden.**
Das sind zwei verschiedene Dinge, und beide sind Pflicht. Was genau, steht in
`regeln/ki-kennzeichnung.md` – lies das einmal ganz, es ist die wichtigste Datei
hier.

**Claude erfindet hier keine Quellen.** Wenn du nach Literatur fragst, bekommst
du Suchbegriffe und Kataloge, keine Titelliste. Das ist unbequem und der Grund
dafür ist eine Zahl: In einer Untersuchung waren je nach Modell 18 bis 55 Prozent
der modellerzeugten Literaturangaben vollständig erfunden.

**Alles hier ist ein Arbeitsstand, keine Rechtsauskunft.** Wenn deine Schule oder
deine Betreuungsperson etwas anderes sagt, gilt das. Immer.

---

## Wenn etwas nicht funktioniert

**Claude kennt die Regeln nicht.** Prüfe, ob du wirklich in diesem Ordner
arbeitest. In der App: Bist du im richtigen Projekt?

**Claude schreibt dir doch ganze Absätze.** Sag: „Lies CLAUDE.md, Abschnitt 2.2."

**Claude nennt Literatur, die du nicht findest.** Frag: „Woher hast du diese
Angabe?" Wenn keine Quelle kommt, ist sie erfunden. Nicht übernehmen und Claude
darauf hinweisen.

**Du weißt nicht, was als Nächstes dran ist.** Tippe `start` oder frag „wo stehe
ich".
