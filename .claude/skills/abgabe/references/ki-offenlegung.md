# Offenlegung: Protokolleintrag, Hilfsmittelverzeichnis, Kennzeichnung

Übertragen aus `bladewing/thesis-check`, Datei references/ki-erklaerung.md (Lukas Iffländer, MIT-Lizenz, siehe `LICENSE.txt` im Skill-Ordner); die HTW-KI-Erklärung im Verzeichnis weiterer Hilfsmittel ist durch die drei ABA-Pflichten ersetzt: Dokumentation im Begleitprotokoll, Kennzeichnung im Text, Hilfsmittelverzeichnis. Die englische Fassung und die LaTeX-Zeile sind gestrichen.

## Warum der Eintrag Pflicht ist

Nach § 9 Abs. 2 Prüfungsordnung AHS dokumentiert das Begleitprotokoll den Arbeitsablauf und die verwendeten Hilfsmittel, und genutzte KI-Anwendungen sind darin kenntlich zu machen. Die KI-FAQ verlangt die Dokumentation, sobald KI-generierte Inhalte einfließen oder den Arbeitsprozess inhaltlich, strukturell oder formal beeinflussen (KI-FAQ 1.2 und 3.1). Ein Check, dessen Befunde du in deine Überarbeitung aufnimmst, beeinflusst den Arbeitsprozess; er gehört also ins Protokoll. Ohne Nennung verstößt du gegen die rechtliche Erklärung, die du bei der Themeneinreichung unterschrieben hast, und bewusst verschwiegene KI-Nutzung gilt als vorgetäuschte Leistung (KI-FAQ 3.9).

Die Kennzeichnung an der Textstelle (KI-FAQ 4.2) greift bei einem reinen Check nicht, weil er keinen Text der Arbeit erzeugt oder umformuliert hat. Sie greift sehr wohl, sobald du ein Werkzeug zum Formulieren, Umschreiben oder Übersetzen einsetzt, im Skill `schreiben`, im Skill `humanizer-de` oder anderswo; dann kommt die Stelle nach `mein/ki-stellen.md` und bekommt im Text Werkzeug und Datum.

Genau das wird bewertet: K1.2 fragt nach dem „transparenten Einsatz technischer Hilfsmittel“, K3.4 nach der Begründung dieses Einsatzes in der Diskussion (`regeln/beurteilung.md`).

## Der Protokolleintrag

Arbeitsteilung wie im Skill `protokoll`: Der Skill liefert die Tatsachen, Datum, Umfang, was getan wurde, welches Werkzeug in welcher Version. Den entscheidenden Satz, was du mit den Befunden gemacht hast, übernommen, verworfen, verändert, und warum, schreibst du selbst; der Skill lässt die Lücke sichtbar und fragt danach (`regeln/begleitprotokoll.md`, Abschnitt 6). Ein Protokoll, das ein Sprachmodell über sich selbst schreibt, ist als Nachweis wertlos.

Die Werte setzt der Skill in Teil 9 des Berichts ein: Werkzeug und Modell, Stand des Skills (aus der Kopfzeile unter dem Frontmatter der SKILL.md; im Berichtskopf steht derselbe Wert), Datum, Anzahl der Durchläufe, Umfang des geprüften Materials (zum Beispiel „Kapitel 1 bis 5 mit Anhang, ohne Titelblatt“). Trag sie so ein, wie sie waren; die Zahl der Durchläufe ist keine Peinlichkeit, sondern ein Beleg dafür, dass du gearbeitet hast.

```
### <TT.MM.JJJJ> – Selbstcheck <vor der Abgabe | des Zwischenstands> (Skill <abgabe | kritik>)

Ich habe <Umfang> mit <Werkzeug> (<Anbieter>, Modell <Modell>) und dem Skill
<abgabe | kritik> aus dem ABA-Setup, Stand <Stand>, gegen die Kriterien des
Beurteilungsrasters, die Formalia und die Offenlegung prüfen lassen; es war der
<n>. Durchlauf. Das Werkzeug lieferte Befunde mit Fundstellen und Rückfragen; es
hat keinen Text meiner Arbeit erzeugt oder umformuliert.
[→ Diesen Satz ergänzt die Person: welche Befunde übernommen, welche verworfen
wurden und warum.]
```

Hast du bei einem früheren Durchlauf schon einen Eintrag geschrieben, kommt ein neuer mit neuem Datum dazu; alte Einträge werden nicht umgeschrieben.

## Die Zeile für das Hilfsmittelverzeichnis

Format wie die amtliche Vorlage `ABA_Hilfsmittelverzeichnis.docx`: drei Spalten „Hilfsmittel/Tool (ggf. inkl. URL)“, „Einsatzbereich & Zweck“ und „Relevanter Prompt (falls zutreffend)“, am Ende der Bestätigungssatz der Vorlage (`regeln/begleitprotokoll.md`, Abschnitt 5.4). Das Hilfsmittelverzeichnis ist offiziell optional, bei KI-Nutzung aber faktisch der saubere Weg; es steht nach dem Literatur- und Quellenverzeichnis und ersetzt weder das Protokoll noch die Kennzeichnung im Text.

- Hilfsmittel/Tool: <Werkzeug> (<Anbieter>, Modell <Modell>), <Adresse>, mit dem Skill <abgabe | kritik> aus dem ABA-Setup, Stand <Stand>
- Einsatzbereich & Zweck: Selbstkontrolle <vor der Abgabe | des Zwischenstands>: <Umfang> wurde am <Datum> <n>-mal gegen die Kriterien des Beurteilungsrasters, die Formalia und die Offenlegung geprüft. Das Werkzeug lieferte Befunde und Rückfragen; es hat keinen Text der Arbeit erzeugt oder umformuliert.
- Relevanter Prompt: nicht zutreffend; der Check lief als Skill, ohne Textauftrag.

Bei mehreren Durchläufen steht in „Einsatzbereich & Zweck“ ein Zeitraum statt eines Datums. Hast du den Skill in einem anderen Werkzeug ausgeführt, etwa in der Claude-App, in ChatGPT oder mit einem lokalen Modell über Ollama, bleibt die Zeile gleich; nur die erste Spalte ändert sich. Bei einem lokalen Modell nennst du Modell und Laufzeitumgebung (zum Beispiel „Ollama, lokal“); dass nichts den eigenen Rechner verlassen hat, gehört als Halbsatz in die zweite Spalte.

## Der Abgleich der KI-Stellen

In `mein/ki-stellen.md` steht jeder Absatz, der aus einem KI-Entwurf stammt, auch wenn er danach überarbeitet wurde. Vor der Abgabe gleicht der Skill `abgabe` diese Liste mit der Kennzeichnung im Text ab, in beide Richtungen (Block 4 in `formalia-checkliste.md`):

- Liste → Text: Jede Stelle der Liste trägt im Text Werkzeug und Datum, im Fließtext oder in der Fußnote. Fehlt die Kennzeichnung, ist das ein Blocker: Überarbeiten hebt die Pflicht nicht auf, und genau dieses Weglassen ist der Täuschungstatbestand (`regeln/ki-kennzeichnung.md`, Abschnitte 6 und 7).
- Text → Liste: Jede Kennzeichnung im Text hat einen Eintrag in der Liste und einen Protokolleintrag mit demselben Datum. Fehlt der Eintrag, ist die Liste unvollständig; das ist kein Blocker, aber vor der Abgabe nachzutragen, denn zu jeder Stelle kann die Kommission fragen.

Der Skill trägt nichts selbst in die Liste oder ins Protokoll ein; er nennt die Stellen, und du ergänzt sie.

## Drei Sätze dazu

1. Sprachliche Überarbeitung ist erlaubt. Nutz die Werkzeuge, wenn sie dir helfen, aber außerhalb dieses Checks, mit eigenem Protokolleintrag und, ab substanzieller Umformulierung, mit Kennzeichnung im Text; der Check bleibt ein getrennter Eintrag, weil er keinen Text angefasst hat.
2. Fachliche Aussagen verantwortest du selbst. Was in der Arbeit steht, musst du erklären können, spätestens in der Diskussion; Inhalte, die mit KI erstellt wurden, prüfst du auf fachliche Richtigkeit und verifizierst sie an Quellen (KI-FAQ 1.2 und 3.10). Das gilt auch für Befunde aus diesem Check: Übernimm nur, was du nach eigenem Lesen für richtig hältst.
3. Vertraulichkeit gilt auch gegenüber KI-Werkzeugen. Unterlagen einer Partnerinstitution oder personenbezogene Daten aus Interviews in ein Cloud-Werkzeug zu geben, ist kein Formfehler, sondern kann gegen eine Vereinbarung oder gegen die Einwilligung verstoßen, die du eingeholt hast. Im Zweifel vorher fragen; genau dafür stehen die Gate-Fragen 2 und 3 am Anfang des Skills.
