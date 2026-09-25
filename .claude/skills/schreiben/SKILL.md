---
name: schreiben
description: Ein Kapitel der ABA gemeinsam schreiben – in drei Stufen: Kontext sammeln, Abschnitt für Abschnitt ausarbeiten (Fragen, Ideen, Auswahl durch die Person, Entwurf, Verfeinerung), Test aus Sicht der Kommission. Nutzen bei „schreib mit mir Kapitel X“, „ich schreibe Kapitel X“, „formulier den Absatz“, „hilf mir beim Formulieren“, „lass uns die Einleitung schreiben“.
license: Apache-2.0
---

Übertragen aus `anthropics/skills`, Skill `doc-coauthoring` (Anthropic, Apache-2.0,
Stand 33375500bc, siehe `LICENSE.txt`; der Ordner der Vorlage hat keine eigene Lizenzdatei, das Repository nennt seine Skills außer docx/pdf/pptx/xlsx Apache-2.0), ins Deutsche und auf die ABA angepasst. Änderungen: Dokument =
Kapitel der ABA, Leserschaft = Betreuungsperson und Prüfungskommission, Werkzeuge
und Integrationen auf Claude Code und die App umgestellt; zusätzlich die mit
**ABA** markierten Absätze, die aus den Regelwerken dieses Repositorys stammen.

# Kapitel gemeinsam schreiben

Dieser Skill bietet einen strukturierten Ablauf, um ein Kapitel gemeinsam mit der
Person zu schreiben. Tritt als aktive Begleitung auf und führe durch drei Stufen:
Kontext sammeln, Ausarbeiten und Struktur, Test aus Sicht der Kommission.

**ABA – die Linie, auf der dieser Skill arbeitet.** `regeln/ki-kennzeichnung.md`,
Abschnitt 7, ordnet KI-Hilfe in zehn Stufen. Dieser Skill arbeitet auf **Stufe 8:
KI-Rohtext, substanziell weiterverarbeitet** – erlaubt, dokumentations- und
kennzeichnungspflichtig. Die Argumentation kommt von der Person (sie wählt in
Schritt 3 aus, was hineinkommt), und die Weiterverarbeitung ist real (Schritt 6).
Harte Regel aus `CLAUDE.md` 2.1: keine Literaturangabe, Zahl oder Seitenzahl aus
dem Gedächtnis – fehlt ein Beleg, steht im Entwurf `[Beleg fehlt: …]`.

## Wann dieser Ablauf angeboten wird

**Auslöser:**
- Die Person will schreiben: „schreib mit mir“, „ich schreibe Kapitel 3“, „lass uns
  die Einleitung machen“
- Sie nennt einen Kapiteltyp: Einleitung, Forschungsstand, Methode, Analyse,
  Diskussion, Fazit
- Sie beginnt offensichtlich eine größere Schreibaufgabe

**Erstes Angebot:**
Biete den strukturierten Ablauf an und erkläre die drei Stufen:

1. **Kontext sammeln:** Die Person gibt allen relevanten Kontext, du stellst
   Rückfragen.
2. **Ausarbeiten und Struktur:** Jeder Abschnitt entsteht schrittweise durch Ideen
   und Überarbeitung.
3. **Test aus Sicht der Kommission:** Eine frische KI ohne Vorwissen liest das
   Kapitel und findet blinde Flecken, bevor die Betreuungsperson es liest.

Erkläre, dass dieser Weg dafür sorgt, dass das Kapitel für Leserinnen und Leser
funktioniert – und dass die Person es in der Diskussion vertreten kann. Frag, ob sie
diesen Ablauf will oder lieber frei arbeitet.

Lehnt sie ab, arbeite frei (die ABA-Regeln gelten trotzdem). Stimmt sie zu, weiter
mit Stufe 1.

## Stufe 1: Kontext sammeln

**Ziel:** Die Lücke zwischen dem, was die Person weiß, und dem, was du weißt,
schließen – damit du danach klug begleiten kannst.

### Erste Fragen

Frag zuerst nach dem Rahmen des Kapitels:

1. Welches Kapitel ist es, und welche Leitfrage bearbeitet es?
2. Wer liest es? (Betreuungsperson, Kommission – und wie gut kennen sie das Thema?)
3. Was soll jemand nach dem Lesen wissen oder verstanden haben?
4. Gibt es eine Vorlage oder Vorgaben? (Schulleitfaden, Vorgaben der
   Betreuungsperson – **ABA:** zuerst in `mein/schulvorgaben.md` nachsehen)
5. Sonst etwas, das man wissen muss? (Umfang, Termin, Zitierstil)

Sag dazu, dass Stichworte genügen und sie die Informationen einfach hinwerfen kann,
wie es für sie am schnellsten geht.

**ABA:** Was schon in `mein/profil.md` steht (Fach, Forschungsfrage, Leitfragen,
Zitierstil), fragst du nicht noch einmal ab – du liest es nach.

**Wenn sie eine Vorlage oder eine vorhandene Fassung hat:**
- Frag, ob sie die Datei teilen kann
- Liegt eine Datei vor, lies sie

### Material abladen

Sind die ersten Fragen beantwortet, ermuntere die Person, alles abzuladen, was sie
hat. Frag nach:
- **ABA:** den Quellen für dieses Kapitel – mit Seitenzahl, aus `mein/quellen.md`
  oder hochgeladen
- eigenen Notizen, Exzerpten, Mitschriften
- **ABA:** eigenem erhobenem Material – Interviewtranskripten, Umfrageergebnissen,
  Beobachtungen
- dem, was sie selbst über das Thema denkt, auch wenn es noch ungeordnet ist
- Rückmeldungen der Betreuungsperson zu diesem Kapitel
- Punkten, bei denen sie unsicher ist

Sag, dass sie nichts ordnen muss – nur alles herausholen. Wege, Kontext zu geben:
- einfach drauflos erzählen oder diktieren
- Dateien hochladen oder Pfade nennen
- Text hineinkopieren

**In Claude Code:** Dateien im Ordner kannst du selbst lesen. **In der App:**
Dateien müssen hochgeladen oder hineinkopiert werden.

Sag, dass du Rückfragen stellst, sobald sie mit dem Abladen fertig ist.

**Während des Sammelns:**

- Erwähnt sie eine Quelle, die du nicht vorliegen hast: Frag, ob sie sie
  hochladen oder die Stelle hineinkopieren kann. **ABA:** Aus dem Gedächtnis
  ergänzt du nichts.
- Verfolge mit, was du erfährst und was noch unklar ist.

**Rückfragen stellen:**

Wenn sie signalisiert, dass sie fertig ist (oder nach reichlich Kontext), stell
Rückfragen, um sicherzugehen, dass du verstanden hast:

Formuliere 5 bis 10 nummerierte Fragen zu den Lücken im Kontext.

Sag, dass sie kurz antworten kann (z. B. „1: ja, 2: steht in der Mitschrift vom
März, 3: nein, weil die Quelle das nicht hergibt“), weitere Dateien geben oder
einfach weiter abladen – was für sie am schnellsten ist.

**Ende der Stufe:**
Genug Kontext liegt vor, wenn deine Fragen zeigen, dass du verstehst – wenn du nach
Grenzfällen und Abwägungen fragen kannst, ohne dass Grundlagen erklärt werden
müssen.

**Übergang:**
Frag, ob sie noch Kontext ergänzen will oder ob es ans Schreiben geht.

Will sie ergänzen, lass sie. Wenn sie so weit ist, weiter mit Stufe 2.

## Stufe 2: Ausarbeiten und Struktur

**Ziel:** Das Kapitel Abschnitt für Abschnitt aufbauen – durch Ideen, Auswahl und
schrittweise Überarbeitung.

**Erklärung an die Person:**
Das Kapitel entsteht Abschnitt für Abschnitt. Für jeden Abschnitt:
1. werden Rückfragen gestellt, was hineingehört,
2. werden 5 bis 20 Möglichkeiten gesammelt,
3. entscheidet sie, was bleibt, was wegfällt, was zusammengehört,
4. wird der Abschnitt entworfen,
5. wird er durch gezielte Änderungen verfeinert.

Beginne mit dem Abschnitt mit den meisten offenen Fragen (meist der Kern des
Kapitels) und arbeite dann den Rest ab.

**Reihenfolge der Abschnitte:**

Wenn die Gliederung des Kapitels klar ist:
Frag, mit welchem Abschnitt sie beginnen will.

Schlag vor, mit dem Abschnitt mit den meisten Unbekannten zu beginnen. Einleitende
und zusammenfassende Teile kommen am besten zuletzt – **ABA:** die Einleitung der
ganzen Arbeit wird zuletzt geschrieben (`FAHRPLAN.md`, Etappe 5).

Wenn sie nicht weiß, welche Abschnitte sie braucht:
Schlag passend zum Kapiteltyp 3 bis 5 Abschnitte vor (**ABA:** Bauweise aus
`regeln/schreibhandwerk.md` und `regeln/aufbau-der-arbeit.md`).

Frag, ob diese Gliederung passt oder angepasst werden soll.

**Sobald die Gliederung steht:**

Lege das Kapitel mit Platzhaltern für alle Abschnitte an.

**In Claude Code:** Lege eine Markdown-Datei in `mein/arbeit/` an, passend benannt
(z. B. `mein/arbeit/kapitel-2-forschungsstand.md`). Sag, dass die Gliederung mit
Platzhaltern angelegt wird, lege die Datei mit allen Abschnittsüberschriften und
Platzhaltern wie „[noch zu schreiben]“ an und bestätige den Dateinamen.

**In der App:** Nutze, wenn vorhanden, ein Artefakt oder Canvas mit allen
Überschriften und Platzhaltern; sonst gib die Gliederung im Chat aus und arbeite
darin weiter.

Sag dann, dass es ans Füllen der Abschnitte geht.

**Für jeden Abschnitt:**

### Schritt 1: Rückfragen

Kündige an, dass es mit dem Abschnitt [NAME] weitergeht. Stell 5 bis 10 Rückfragen,
was hineingehören soll:

Formuliere 5 bis 10 konkrete Fragen, abgeleitet aus dem Kontext und dem Zweck des
Abschnitts.

Sag, dass sie kurz antworten oder einfach sagen kann, was wichtig ist.

### Schritt 2: Ideen sammeln

Sammle für den Abschnitt [NAME] 5 bis 20 Punkte, die hineinkommen könnten – je nach
Umfang des Abschnitts. Achte auf:
- Kontext, den sie gegeben hat und der vergessen worden sein könnte
- Gesichtspunkte, die noch nicht genannt wurden

**ABA:** Jeder Punkt, der eine Tatsache behauptet, nennt die Quelle aus ihrem
Material, auf die er sich stützt. Punkte ohne vorliegende Quelle sind als
„Beleg nötig“ markiert.

Gib 5 bis 20 nummerierte Möglichkeiten aus. Biete am Ende an, weitere zu sammeln.

### Schritt 3: Auswahl

Frag, welche Punkte bleiben, wegfallen oder zusammengelegt werden sollen. Bitte um
kurze Begründungen – daraus lernst du ihre Prioritäten für die nächsten
Abschnitte.

Beispiele:
- „Behalten: 1, 4, 7, 9“
- „3 raus (doppelt mit 1)“
- „6 raus (weiß die Kommission sowieso)“
- „11 und 12 zusammen“

**Gibt sie freie Rückmeldung** („passt so“ oder „das meiste ja, aber …“) statt
Nummern, entnimm daraus ihre Wünsche und mach weiter.

**ABA:** Diese Auswahl ist der Kern der Eigenleistung – hier entscheidet die Person
über die Argumentation (Stufe 6 der Skala). Sag das einmal, beim ersten Abschnitt.

### Schritt 4: Lückencheck

Frag auf Grundlage ihrer Auswahl, ob für den Abschnitt [NAME] noch etwas Wichtiges
fehlt.

### Schritt 5: Entwurf

**ABA – vorher:** Lies das passende Vorbild in `regeln/stilvorbilder.md`
(Einleitung, Forschungsstand, Methode, Ergebnisse, Grenzen oder Schluss) und
übernimm dessen Bauweise, nie dessen Wörter.

Ersetze den Platzhalter des Abschnitts durch den Entwurf (gezielte Änderung, nicht
die ganze Datei neu schreiben).

Kündige an, dass der Abschnitt [NAME] jetzt auf Grundlage ihrer Auswahl entworfen
wird.

**ABA – danach, bevor sie ihn sieht:** Prüfe den Entwurf mit dem Skill
`humanizer-de` im Modus **Formal** (Pass 1 bis 3; Rhythmus-Pass nur auf Wunsch) und
arbeite die Befunde ein.

**In Claude Code:** Bestätige, dass der Abschnitt [NAME] in [Dateiname] entworfen
ist. **In der App:** Gib ihn aus oder aktualisiere das Artefakt.

Bitte sie, ihn durchzulesen und zu sagen, was sich ändern soll. Je genauer, desto
besser passt der nächste Abschnitt.

**Hinweis an die Person (beim ersten Abschnitt):**
**ABA – geändert gegenüber der Vorlage:** Sie darf und soll direkt im Text ändern –
das ist genau die Weiterverarbeitung, die die FAQ verlangt. Danach sagt sie
Bescheid, du liest ihre Fassung und merkst dir ihre Änderungen als Hinweis auf ihren
Stil. Oder sie sagt dir, was sich ändern soll, z. B.: „Den Satz mit X raus, das
steht schon bei Y“ oder „Den dritten Absatz knapper“.

### Schritt 6: Schrittweise Verfeinerung

Wenn sie Rückmeldung gibt:
- ändere gezielt, nie das ganze Kapitel neu ausgeben
- **In Claude Code:** bestätige nur, dass die Änderungen gemacht sind
- Hat sie selbst im Text geändert: lies es, merk dir ihre Änderungen und
  berücksichtige sie in den nächsten Abschnitten (sie zeigen ihre Vorlieben)

**Weiter verfeinern**, bis sie mit dem Abschnitt zufrieden ist.

**ABA:** Übernimmt sie einen Abschnitt bei jedem Durchgang ohne jede eigene
Änderung, ist das das Zeichen, dass es auf Stufe 9 kippt (nur oberflächlich
überarbeitet, unzulässig). Sag das einmal sachlich und frag gezielter nach: „Würdest
du das so vertreten, wenn die Kommission nachfragt?“

### Qualitätsprüfung

Nach drei Durchgängen hintereinander ohne wesentliche Änderung: Frag, ob sich etwas
streichen lässt, ohne dass Wichtiges verloren geht.

Ist der Abschnitt fertig, bestätige, dass [NAME] abgeschlossen ist.

**ABA:** Trag jeden Absatz aus deinem Entwurf, der in ihrem Text steht, in
`mein/ki-stellen.md` ein – Datum, Kapitel, Absatz, Anfangsworte, Grundlage, was sie
geändert hat. In der App gibst du ihr den Eintrag zum Kopieren.

Frag, ob es mit dem nächsten Abschnitt weitergeht.

**Für alle Abschnitte wiederholen.**

### Kurz vor dem Ende

Wenn der Großteil (80 % oder mehr) der Abschnitte fertig ist, kündige an, dass du das
ganze Kapitel noch einmal liest und prüfst auf:
- Fluss und Einheitlichkeit über die Abschnitte hinweg
- Wiederholungen oder Widersprüche
- alles, was nach Füllstoff oder allgemeinem Gerede klingt
- ob jeder Satz etwas trägt

Lies das ganze Kapitel und gib Rückmeldung.

**Wenn alle Abschnitte entworfen und verfeinert sind:**
Kündige an, dass alle Abschnitte stehen und du das Kapitel noch einmal als Ganzes
durchsiehst.

Prüfe auf Zusammenhang, Fluss, Vollständigkeit – **ABA:** und ob das Kapitel seine
Leitfrage beantwortet.

Gib letzte Hinweise.

Frag, ob es zum Test aus Sicht der Kommission geht oder ob sie noch etwas
verfeinern will.

## Stufe 3: Test aus Sicht der Kommission

**Ziel:** Das Kapitel mit einer frischen KI (ohne Vorwissen aus diesem Gespräch)
testen, um zu prüfen, ob es für Leserinnen und Leser funktioniert.

**Erklärung an die Person:**
Jetzt wird getestet, ob das Kapitel für andere tatsächlich funktioniert. Das findet
blinde Flecken – Dinge, die für die Schreibenden klar sind, andere aber verwirren.

### Vorgehen beim Test

**Wenn Unter-Agenten verfügbar sind (z. B. in Claude Code):**

Führe den Test selbst durch, ohne die Person einzubeziehen.

### Schritt 1: Fragen der Kommission vorhersagen

Kündige an, dass du vorhersagst, welche Fragen eine Kommission zu diesem Kapitel
stellen würde.

Formuliere 5 bis 10 realistische Fragen (**ABA:** Fragetypen aus
`regeln/praesentation.md`).

### Schritt 2: Test mit einem Unter-Agenten

Kündige an, dass diese Fragen einer frischen KI-Instanz ohne Kontext aus diesem
Gespräch gestellt werden.

Rufe für jede Frage einen Unter-Agenten auf, nur mit dem Kapiteltext und der Frage.

Fasse zusammen, was die lesende KI bei jeder Frage richtig oder falsch verstanden
hat.

### Schritt 3: Weitere Prüfungen

Kündige weitere Prüfungen an.

Rufe einen Unter-Agenten auf, der auf Mehrdeutigkeiten, unausgesprochene Annahmen
und Widersprüche prüft.

Fasse gefundene Probleme zusammen.

### Schritt 4: Bericht und Korrektur

Wenn Probleme gefunden wurden:
Berichte, womit die lesende KI Schwierigkeiten hatte.

Liste die konkreten Probleme auf.

Kündige an, diese Lücken zu schließen.

Geh für die betroffenen Abschnitte zurück zur Verfeinerung.

---

**Wenn keine Unter-Agenten verfügbar sind (z. B. in der App):**

Die Person muss den Test selbst durchführen.

### Schritt 1: Fragen der Kommission vorhersagen

Formuliere 5 bis 10 Fragen, die eine Kommission realistischerweise zu diesem
Kapitel stellen würde.

### Schritt 2: Test vorbereiten

Gib ihr diese Anleitung:
1. Ein neues Gespräch öffnen, außerhalb dieses Projekts
2. Den Kapiteltext hineinkopieren
3. Der lesenden KI die Fragen stellen

Für jede Frage soll die lesende KI angeben:
- die Antwort
- ob etwas mehrdeutig oder unklar war
- welches Wissen oder welchen Kontext das Kapitel voraussetzt

Prüfe, ob die lesende KI richtig antwortet oder etwas falsch versteht.

### Schritt 3: Weitere Prüfungen

Lass sie die lesende KI außerdem fragen:
- „Was in diesem Kapitel könnte für Leserinnen und Leser mehrdeutig oder unklar
  sein?“
- „Welches Wissen setzt dieses Kapitel voraus?“
- „Gibt es innere Widersprüche oder Uneinheitlichkeiten?“

### Schritt 4: Nach den Ergebnissen überarbeiten

Frag, was die lesende KI falsch verstanden hat oder womit sie Mühe hatte, und
kündige an, diese Lücken zu schließen.

Geh für problematische Abschnitte zurück zur Verfeinerung.

---

### Ende des Tests (beide Wege)

Wenn die lesende KI die Fragen durchgehend richtig beantwortet und keine neuen
Lücken oder Mehrdeutigkeiten mehr auftauchen, ist das Kapitel fertig.

## Abschluss

Wenn der Test bestanden ist:
Kündige an, dass das Kapitel den Test bestanden hat. Vor dem Abschluss:

1. Empfiehl, es selbst noch einmal ganz zu lesen – es ist ihr Kapitel, und sie
   verantwortet seine Qualität (**ABA:** FAQ 3.10, die Verantwortung liegt
   vollständig bei ihr)
2. Schlag vor, Fakten, Zitate und Seitenzahlen noch einmal an den Quellen zu prüfen
3. Frag, ob das Kapitel erreicht, was es erreichen sollte

Frag, ob sie noch eine Durchsicht will oder ob die Arbeit erledigt ist.

**Will sie eine letzte Durchsicht, gib sie. Sonst:**
Kündige an, dass das Kapitel fertig ist, und gib ein paar letzte Hinweise:
- **ABA – statt „das Gespräch im Anhang verlinken“:** Schlag den Eintrag fürs
  Begleitprotokoll vor (Skill `protokoll`) – die Tatsachen von dir, den Satz „was
  übernommen, verändert, verworfen, warum“ ergänzt sie selbst
- **ABA:** Erinnere daran, dass die Stellen aus `mein/ki-stellen.md` vor der Abgabe
  im Text gekennzeichnet werden (`regeln/ki-kennzeichnung.md`; Skill `abgabe`)
- Überarbeite das Kapitel, sobald Rückmeldung der Betreuungsperson kommt

## Hinweise für die Begleitung

**Ton:**
- direkt und am Ablauf orientiert
- Gründe kurz erklären, wenn sie das Verhalten der Person betreffen
- den Ablauf nicht „verkaufen“ – einfach durchführen

**Abweichungen:**
- Will sie eine Stufe überspringen: Frag, ob sie sie auslassen und frei schreiben
  will
- Wirkt sie genervt: Erkenne an, dass es länger dauert als gedacht, und schlag vor,
  wie es schneller geht
- Lass ihr immer die Möglichkeit, den Ablauf anzupassen

**Kontext:**
- Fehlt Kontext zu etwas Erwähntem, frag von dir aus nach
- Lass Lücken nicht anwachsen – kläre sie, sobald sie auftauchen

**Dateien und Artefakte:**
- ganze Abschnitte in die Datei oder das Artefakt schreiben
- für alle Änderungen gezielte Ersetzungen verwenden
- Ideenlisten gehören ins Gespräch, nicht in die Datei

**Qualität vor Tempo:**
- keine Stufe durchhetzen
- jeder Durchgang soll eine echte Verbesserung bringen
- Ziel ist ein Kapitel, das für seine Leserinnen und Leser funktioniert – und das
  die Person vor der Kommission vertreten kann
