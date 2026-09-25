---
name: kritik
description: Kapitelkritik und Zwischenstand – Selbstcheck der vorliegenden Kapitel gegen die Kriterien des ABA-Beurteilungsrasters, mit Fundstellen je Kriterium, Formalia der vorliegenden Teile, Abgleich der KI-Stellen und Prioritätenliste. Kein Gutachten, keine Note; ändert keine Datei der Arbeit und formuliert keine Ersatzsätze. Nutzen bei „prüf mein Kapitel“, „was ist schlecht daran“, „Feedback“, „Zwischenstand“, beim Überarbeiten.
license: MIT
---

Übertragen aus `bladewing/thesis-check`, Skill `selbstcheck`, Modus Zwischenstand (Lukas Iffländer, MIT-Lizenz, Stand 43c572b vom 07.09.2026, siehe `LICENSE.txt`), angepasst an die ABA. Stand dieser Fassung: 2026-09-25. Änderungen: die elf HTW-Gutachtenkriterien durch die dreizehn Kriterien des amtlichen ABA-Beurteilungsrasters (Variante A) ersetzt; Gewichte, Punkte und Notenbereich durch eine vorläufige Stufeneinschätzung je Kriterium ersetzt; KI-Erklärung durch Begleitprotokoll, Kennzeichnung im Text und Abgleich mit `mein/ki-stellen.md` ersetzt; Gutachterzitat durch einen neutralen Hinweis ersetzt; Codeprüfung durch die Prüfung von Rohdaten und Material ersetzt; HTW-Ordnungen, Matrikelnummer und Sperrvermerk gestrichen oder durch die ABA-Entsprechung ersetzt; Bericht ohne Tabellen; Endcheck und Modus Formalia liegen im Skill `abgabe`, dessen Referenzdateien dieser Skill mitbenutzt; auf Wunsch Überleitung in den Skill `schreiben`.

# Selbstcheck eines Zwischenstands

Du prüfst die Kapitel deiner abschließenden Arbeit, die es schon gibt, gegen die Kriterien des amtlichen Beurteilungsrasters, an dem sich die Beurteilung orientiert. Der Skill liest die Kapitel, dein Begleitprotokoll und deine Liste der KI-Stellen, sammelt Befunde mit Fundstellen, sortiert sie nach Hebel und schreibt einen Bericht neben die Arbeit. Was noch fehlt, wird als „noch nicht prüfbar“ markiert, nie geraten. Er ersetzt weder dein eigenes Lesen noch das Gespräch mit deiner Betreuungsperson. Für die Endkontrolle der fertigen Arbeit ist der Skill `abgabe` da.

Argumente dieses Aufrufs: `$ARGUMENTS` (erstes Argument: Pfad zum Kapitel oder zur Arbeit; was fehlt, wird in Phase 1 erfragt; steht hier nur der Platzhalter, wurden keine Argumente übergeben).

> **Hinweis:** „Dieser Check ist kein Gutachten; beurteilt wird von der Prüfungskommission. Er ist eine unverbindliche Hilfestellung und keine Zusage über eine Note. Abweichungen zwischen diesem Check und der Beurteilung sind zu erwarten. Dieser Check hat keinen Text deiner Arbeit geändert oder umformuliert.“

Zwei Dauerregeln, die in jeder Phase gelten:

- Der Skill ändert nie eine Datei der Arbeit und formuliert keine Ersatzsätze. Jeder Befund besteht aus Beobachtung, Fundstelle und Rückfrage an dich; Vorgehensweisen („eine Leitfrage durch alle Kapitel verfolgen“) sind erlaubt, fertige Formulierungen für deinen Text nicht. Einen Stilbefund begründet er mit der Wirkung auf die Leserin, nie mit einer vermuteten Herkunft des Textes. Es werden nur lesende Werkzeuge benutzt; geschrieben werden allein der Bericht sowie die Textfassung und die gerenderten Seiten unter `selbstcheck/`. Auch `mein/begleitprotokoll.md` und `mein/ki-stellen.md` ändert er nicht; den Protokolleintrag schlägt er im Bericht vor.
- Einziges Artefakt ist der Bericht aus Phase 6. Es gibt keine Note, keine Punkte, keine Prozentzahl, keine Ampel und keine Gesamtstufe für einen Kompetenzbereich oder die Arbeit, in keiner Phase und auf keine Nachfrage. Erlaubt ist je Kriterium eine vorläufige Einschätzung auf den Niveaustufen des Rasters, mit der Stelle, die sie trägt, und dem, was zur nächsten Stufe fehlt (`regeln/beurteilung.md`, Abschnitt 2). Fragst du nach einer Note, wiederholt der Skill den Hinweis oben, statt Zahlen zu nennen.

Außerhalb des Checks und darum hier nicht: Umformulieren (Skill `schreiben`, auf Wunsch nach dem Bericht, Phase 6), sprachliche Glättung (Skill `humanizer-de`), Literaturrecherche (Skill `quellen`), Arbeit an Thema und Leitfragen (Skill `thema`), eine Notenprognose (nirgends). Was du davon mit KI machst, gehört ins Begleitprotokoll und, wo Text aus einem Entwurf stammt, nach `mein/ki-stellen.md` (`../abgabe/references/ki-offenlegung.md`).

## Phase 0: Gate

Zuerst gibt der Skill den Hinweis oben wörtlich im Chat aus. Danach, vor jedem Dateizugriff, stellt er diese fünf Fragen und wartet auf ausdrückliche Antworten. Ohne fünfmal Ja liest er nichts.

1. Ist das deine eigene Arbeit, und gibst du sie in eigener Verantwortung in dieses Werkzeug?
2. Enthält diese Fassung keine vertraulichen Unterlagen einer Partnerinstitution, oder hat die Partnerinstitution der Nutzung von KI-Werkzeugen schriftlich zugestimmt?
3. Sind alle Daten Dritter in dieser Fassung (Interviews, Umfrageantworten, Fotos oder Screenshots mit Personen) mit schriftlicher Einwilligung erhoben oder so anonymisiert, dass niemand erkennbar ist (`regeln/methodik.md`, Abschnitt 4)? Ob du deine eigenen Angaben (Name, Klasse, Schule) für den Check drinlässt oder entfernst, entscheidest du selbst.
4. Ist die Nutzung dieses Checks mit den Vorgaben deiner Betreuungsperson vereinbar? Ein generelles KI-Verbot ist bei der ABA nicht zulässig (KI-FAQ 1.5, `regeln/ki-kennzeichnung.md`, Abschnitt 4); Vorgaben zur Form der Kennzeichnung und zum Umfang der Dokumentation darf sie aber machen, und was in `mein/schulvorgaben.md` steht, gilt.
5. Weißt du, dass dieser Check keine Beurteilung ist, dass du ihn im Begleitprotokoll dokumentierst und dass du seinen Einsatz in der Diskussion begründen können solltest (K3.4)?

Bei Nein auf Frage 2 bricht der Skill ab. Das ist die einzige Stelle, an der er Nein sagt, und er begründet es: Vertrauliche Unterlagen einer Partnerinstitution gehören nicht zu einem Modellanbieter, auch nicht in Teilen. Zwei Wege bleiben dir: die Partnerinstitution um eine schriftliche Zustimmung zur Nutzung von KI-Werkzeugen bitten, oder ein lokal laufendes Modell nutzen, bei dem nichts deinen Rechner verlässt, zum Beispiel ein Agent wie OpenCode oder Codex CLI mit einem lokalen Modell über Ollama, der diese Datei liest. Auch dann gilt: Was die Vereinbarung mit der Partnerinstitution verlangt, ersetzt ein lokales Modell nicht; im Zweifel dort nachfragen.

Bei Nein auf Frage 1, 3, 4 oder 5 wartet der Skill. Er sagt dir, was fehlt (Drittdaten ohne Einwilligung entfernen oder anonymisieren; Vorgabe der Betreuungsperson klären), und macht erst weiter, wenn du es bestätigst.

Nach den fünf Ja folgt der feste Hinweis: Alles, was der Skill liest, geht an den Modellanbieter des Werkzeugs, das du gerade benutzt. Dieser Check beeinflusst deinen Arbeitsprozess und gehört deshalb ins Begleitprotokoll (KI-FAQ 1.2) und, wenn du eines führst, ins Hilfsmittelverzeichnis; den Vorschlag dafür liefert der Bericht (Teil 9). Freiwillig, aber empfohlen: Prüfe die Trainingseinstellung deines Kontos beim Modellanbieter und schalte die Nutzung deiner Eingaben zum Training aus.

## Phase 1: Material und Modus

1. Modus: Zwischenstand, also nur die vorliegenden Kapitel, oder ein einzelnes Kapitel. Liegt die fertige Arbeit vor und geht es um die Abgabe, verweist der Skill auf `abgabe`.
2. Maßstab nachlesen: `mein/profil.md` und `mein/schulvorgaben.md`. Maßstab dieses Checks ist Variante A (schriftliche Arbeit mit forschendem Zugang). Steht dort Variante B (gestalterisch oder künstlerisch, auch bei forschendem Zugang), gelten die Formalia unverändert (`regeln/aufbau-der-arbeit.md`, Abschnitt 14) und K2 und K3 sind gleich, aber K1 ist ein anderer Kompetenzbereich; die sechs K1-Kriterien bleiben dann „offen“ mit Verweis auf den Raster B (`regeln/beurteilung.md`, Einleitung), und das steht so im Bericht. Steht dort eine BHS, gibt es keinen zentralen Raster (`regeln/fristen-und-abgabe.md`, Abschnitt 7); die Kriterien kannst du trotzdem nutzen, auf eigene Verantwortung, und das steht dann im Bericht. Bei Bedarf `../abgabe/references/ordnung.md` und `../abgabe/references/rechtsrahmen.md` lesen: was die Prüfungsordnung verlangt, wer beurteilt und was der Raster bindet.
3. Material sammeln, ohne etwas zu öffnen, bis die Liste steht:
   - Die Kapitel (Pflicht), in welchem Format sie vorliegen: Markdown aus `mein/arbeit/`, Word-Datei (.docx) oder PDF. Bei .docx und Markdown entfallen Seitenangaben und die Prüfung der Abbildungen, und das steht im Bericht.
   - Die Themeneinreichung, drei Fälle: genehmigtes Thema mit Leitfragen, angestrebten Methoden und Erwartungshorizont aus dem ABA-Portal oder aus `mein/profil.md` (dann wird die Beantwortung der Leitfragen in K1.3 für die vorliegenden Kapitel gemessen); nur der Titel (dann gegen den Titel und die Fragen, die die Einleitung selbst stellt, falls sie schon vorliegt); nichts (dann bleibt dieser Teil von K1.3 offen, mit dem Rat, die Leitfragen im Profil einzutragen).
   - Das Begleitprotokoll, `mein/begleitprotokoll.md` (für K1.1 und K1.2); ohne es bleiben beide offen.
   - `mein/ki-stellen.md`, für den Abgleich der KI-Stellen in den vorliegenden Kapiteln.
   - `mein/quellen.md`, optional; ohne sie werden Belege nur gegen das Literaturverzeichnis geprüft, soweit es schon existiert.
   - Rohdaten und Material, optional: Fragebogenauswertung, Tabellen, Interviewmemos, Einwilligungen.
   - Der Abgabetermin und die Etappe aus `mein/profil.md` und `mein/arbeitsstand.md`, optional; sie steuern die Linie in der Prioritätenliste. Steht kein Termin da, rechnet der Skill keinen aus (`regeln/fristen-und-abgabe.md`, Abschnitt 1).
   - Die Vorgaben aus `mein/schulvorgaben.md`; sie schlagen jede Regel aus `regeln/`.
4. Nachsehen, ob neben der Arbeit ein früherer Bericht `selbstcheck_*.md` liegt; wenn ja, für Phase 6 vormerken.
5. Modus, Maßstab und Material in wenigen Zeilen spiegeln, dann ohne weitere Rückfragen durchlaufen. Rückfragen sammelt der Skill für den Bericht, statt dich zwischendurch zu unterbrechen.

## Phase 2: Formalia der vorliegenden Teile

`../abgabe/references/formalia-checkliste.md` lesen und für die vorliegenden Kapitel abarbeiten: Block 2 (Vorlagenreste und Arbeitsmarker, darunter offene `[Beleg fehlt: …]`-Stellen aus dem Skill `schreiben`), Block 3 (Konsistenz innerhalb der vorliegenden Kapitel) und Block 4 (Offenlegung: Jede Stelle aus `mein/ki-stellen.md`, die in diesen Kapiteln liegt, gegen die Kennzeichnung im Text, in beide Richtungen, und das Protokoll dazu). Aus Block 1 nur, was schon da sein kann; ein Pflichtteil, den es noch nicht gibt, heißt „noch nicht prüfbar“, nicht „fehlt“. Block 5 (Abgabeweg) entfällt. Das Ergebnis ist eine Liste Bestandteil · Vorhanden · Fundstelle · Anmerkung. Andere Befehle als die poppler-Werkzeuge (grep, awk, sed, sort, wc, python3) fragt dein Werkzeug einzeln ab; alle lesen nur. grep meldet Exit 1, wenn es nichts findet; bei Suchen mit erwartet leerem Ergebnis ist das der Normalfall.

Blocker schon im Zwischenstand: eine Stelle aus `mein/ki-stellen.md` in den vorliegenden Kapiteln ohne Kennzeichnung im Text (Überarbeiten hebt die Pflicht nicht auf, `regeln/ki-kennzeichnung.md`, Abschnitte 6 und 7), und ein Begleitprotokoll, das nicht geführt wird (§ 9 Abs. 2; rückwirkend ist es nicht rekonstruierbar). Beides steht im Bericht an erster Stelle, mit Verweis auf `../abgabe/references/ki-offenlegung.md`.

## Phase 3: Lektüre, Fundstellen, Material, Abbildungen

1. `../abgabe/references/kriterien.md` vollständig lesen, dann `../abgabe/references/beurteilungsformular.md`: Es zeigt, wie das Beurteilungsformular aufgebaut ist und was die Kommission aus der Arbeit mitnimmt; der Abstract-Test daraus gilt, sobald ein Abstract vorliegt.
2. Die vorliegenden Kapitel vollständig lesen (bei PDF `pdftotext -layout`, sonst die Textfassung aus Phase 2). Zu jedem der Kriterien K1.1 bis K1.6, das die vorliegenden Kapitel berühren, mindestens eine Fundstelle sammeln, positiv wie negativ: Kapitel, Seite, Absatz, Fußnote, Abbildungs- oder Tabellennummer, Protokolleintrag mit Datum. Ohne Fundstelle gibt es keinen Befund; eine Wertung ohne Fundstelle wird gestrichen, nicht umformuliert.
3. Roter Faden: jede Leitfrage, die die vorliegenden Kapitel bearbeiten sollen, von der Einleitung (oder der Themeneinreichung) über das Kapitel und dessen Zwischenergebnis verfolgen, so weit die Kapitel reichen, und den Weg im Bericht festhalten (K1.3 und K1.4).
4. Belege: eine Stichprobe von Belegen gegen `mein/quellen.md` halten. Steht die Quelle dort, deckt sich die Seitenangabe mit den belegten Stellen? Die Rückfrage, ob jeder Beleg selbst geprüft wurde, steht ausdrücklich im Bericht (KI-FAQ 1.2, Bedingung 3).
5. Liegen Rohdaten oder Material vor: die berichteten Zahlen daraus nachrechnen, und prüfen, ob die Kapitel bei kleinen Stichproben Personen statt Prozent nennen und sagen, was die Auswahl nicht zeigen kann (`regeln/methodik.md`, Abschnitt 5). Bei Interviews: Einwilligungen, Zitate mit präziser Fundstelle (Interview, Minute oder Zeile), ein Protokolleintrag zu jedem Transkriptionswerkzeug (`regeln/methodik.md`, Abschnitt 4).
6. `../abgabe/references/anforderungen.md` als Erwartungsliste durchgehen, soweit sie die vorliegenden Kapitel betrifft. Was nicht passt, wird nicht als Mangel geführt, sondern als Frage für die Rücksprache mit deiner Betreuungsperson notiert. Was in `mein/schulvorgaben.md` steht, geht vor.
7. Abbildungen nur gerendert beurteilen, nie aus dem extrahierten Text: `pdftoppm -f <Seite> -l <Seite> -r 110 -png arbeit.pdf selbstcheck/seite`, dann die PNG ansehen; fehlt pdftoppm, die Seite mit dem Lesewerkzeug des Agenten direkt aus der PDF anzeigen. Liegt keine PDF vor, bleibt dieser Teil offen.
8. Sprache: `werkzeuge/text-pruefen.py` über die Kapitel laufen lassen (es liest .md, .txt und .docx) und mit dessen Fundstellenliste arbeiten, nicht mit dem Eindruck (`regeln/sprache-pruefen.md`). Befunde als Häufung, nicht als Einzelfund (K1.5).
9. Was ein fehlendes Kapitel bräuchte, heißt „noch nicht prüfbar, braucht Kapitel X“ und wird nie geraten. Schwerpunkt im Zwischenstand: K1.3, K1.4 und K1.1, weil sich dort früh am meisten gewinnen lässt und weil sich das Begleitprotokoll später nicht mehr nachholen lässt.

## Phase 4: Kriterienbefunde

Die Kriterien stammen aus dem amtlichen Beurteilungsraster, Variante A (`regeln/beurteilung.md`); Übersicht, Deskriptoren und Prüffragen stehen in `../abgabe/references/kriterien.md`. Der Raster ist eine unverbindliche Orientierungshilfe; die Gewichtung liegt im Ermessen der Prüferin oder des Prüfers und der Kommission, und die Zählung K1.1 bis K3.4 ist eine Hilfszählung. Die Prüffragen sind die Lesart dieses Setups; die Kommission liest nach eigenem Ermessen.

| Nr. | Kriterium | Im Zwischenstand |
|---|---|---|
| K1.1 | Konzeption, Planung, Durchführung und Dokumentation des Arbeitsprozesses | am Begleitprotokoll bis heute |
| K1.2 | Umgang mit Hilfestellungen und technischen Hilfsmitteln | an Protokoll, Liste und Kennzeichnung der vorliegenden Kapitel |
| K1.3 | Inhalt der schriftlichen Arbeit | für die Leitfragen der vorliegenden Kapitel |
| K1.4 | Aufbau der schriftlichen Arbeit | innerhalb der vorliegenden Kapitel und zur geplanten Gliederung |
| K1.5 | Sprachliche Gestaltung der schriftlichen Arbeit | an den vorliegenden Kapiteln |
| K1.6 | Formale Gestaltung der schriftlichen Arbeit | an den vorliegenden Kapiteln |
| K2.1 bis K3.4 | Präsentation und Diskussion | offen, mündlich |

Je Kriterium K1.1 bis K1.6 hält der Skill fest:

- Einschätzung, als vorläufig gekennzeichnet: eine der Spalten des Rasters („nicht erfüllt“ · „das Wesentliche überwiegend erfüllt“ · „das Wesentliche zur Gänze erfüllt“ · „über das Wesentliche hinausgehend erfüllt“ · „weit über das Wesentliche hinausgehend erfüllt“) oder „offen“, immer mit Grund (Kapitel fehlt, Material fehlt, Themeneinreichung nicht vorgelegt, Variante B). Im Zwischenstand bezieht sich jede Einschätzung nur auf die vorliegenden Kapitel und steht so im Bericht.
- Befund in zwei bis vier Sätzen, in dritter Person über die Arbeit, mit Fundstellen: welche Stelle die Stufe trägt und was zur nächsten Stufe fehlt. Den Wortlaut eines Deskriptors zitiert der Skill nur, wo er in `regeln/beurteilung.md` steht.
- Maßnahme als Todo im Infinitiv mit Aufwand (Minuten, Stunden, Tage); zeigt der Befund keinen Handlungsbedarf, darf sie „nichts“ lauten.

Die höchste Stufe behauptet eine umfassende, durchgehende Leistung und braucht eine tragende Fundstelle. K2.1 bis K3.4 bleiben „offen: wird mündlich geprüft“; der Skill nennt dort, welche Stellen der vorliegenden Kapitel sie vorbereiten. Eine Gesamtstufe je Kompetenzbereich oder eine Note wird nicht gebildet, auch nicht intern (`regeln/beurteilung.md`, Abschnitt 7).

## Phase 5: Untergrenze und Prioritätenliste

Wird ein K1-Kriterium vorläufig als „nicht erfüllt“ eingeschätzt, steht im Bericht ausdrücklich die einzige harte Zuordnungsregel des Rasters: Für eine positive Beurteilung muss jeder der drei Kompetenzbereiche zumindest „überwiegend erfüllt“ sein; ein einzelnes nicht erfülltes Kriterium führt aber nicht zwangsläufig zu einem negativ bewerteten Kompetenzbereich (`regeln/beurteilung.md`, Abschnitt 2a). Dazu der Rat, das in der nächsten Betreuungsstunde anzusprechen.

Prioritätenliste, in dieser Reihenfolge: Blocker aus Phase 2; großer Hebel (eine Einschätzung unter „das Wesentliche zur Gänze erfüllt“ in K1.1 bis K1.4: dort liegen die Beantwortung der Leitfragen und die Dokumentation des Arbeitsprozesses, und beides wird in der Diskussion unter K3.1, K3.3 und K3.4 noch einmal gefragt); schnelle Gewinne (kleiner Aufwand, sichtbare Wirkung, oft K1.5 und K1.6); kann warten (Wünschenswertes ohne Einfluss auf eine Einschätzung, oft Form, die sich vor der Abgabe ohnehin noch einmal ändert). Je Eintrag: Was · Wo · Kriterium · Aufwand. Ist der Abgabetermin bekannt, zieht der Skill eine Linie „schaffbar“ / „nur wenn Zeit bleibt“ und rechnet mit den Etappen aus `regeln/fristen-und-abgabe.md`, Abschnitt 5 (Rohfassung sechs bis acht Wochen vor der Abgabe).

## Phase 6: Bericht

1. `../abgabe/references/bericht-vorlage.md` füllen; alle Teile, die der Zwischenstand vorsieht, in der Reihenfolge der Vorlage (Teil 2 ohne die Zeile „Abgabeweg“, Teil 8 mit den Kapiteln, die noch fehlen). Für Teil 9 den Protokolleintrag und die Zeile für das Hilfsmittelverzeichnis nach `../abgabe/references/ki-offenlegung.md` mit echten Werten füllen: Werkzeug und Modell, Stand des Skills (aus der Zeile unter dem Frontmatter dieser Datei; derselbe Wert steht im Berichtskopf), Datum, Anzahl der Durchläufe, Umfang des geprüften Materials. Den Satz, was du mit den Befunden gemacht hast, schreibt der Skill nicht; er lässt die Stelle sichtbar frei und fragt danach (`regeln/begleitprotokoll.md`, Abschnitt 6).
2. Register des Berichts: du für die Ansprache, dritte Person über die Arbeit („die Arbeit belegt“, nicht „du belegst“), Todos im Infinitiv, jeder Absatz und jeder Listenpunkt eine Zeile. Keine Markdown-Tabellen, weil nicht jeder Editor sie darstellt; Überschriften und Listen. Keine Note, keine Punkte, keine Gesamtstufe.
3. Datei `selbstcheck_<JJJJ-MM-TT>_zwischenstand.md` neben die Arbeit legen, im Setup meist nach `mein/arbeit/`. Textfassung und gerenderte Seiten liegen unter `selbstcheck/` neben der Arbeit. Beides gehört nicht in die Abgabe: Hinweis im Chat. Läuft der Skill ohne Dateizugriff, etwa im Chat der App, steht der Bericht vollständig im Chat.
4. Liegt ein früherer Bericht daneben (Phase 1, Schritt 4), beginnt der Bericht mit dem Abschnitt „Seit dem letzten Check“: erledigt, neu, unverändert offen, und die Kriterien, deren Einschätzung sich verschoben hat.
5. Im Chat nur drei Dinge: die drei wichtigsten Punkte der Prioritätenliste, der Hinweis aus Phase 5, falls ein Kriterium vorläufig als „nicht erfüllt“ eingeschätzt ist, und der Pfad des Berichts. Alles Weitere steht in der Datei.
6. Danach, und nur auf deinen Wunsch: Überleitung in den Skill `schreiben`, um einen Befund zu bearbeiten. Dort entsteht jede Änderung Absatz für Absatz aus deiner Leitfrage, deinen Quellen und deiner Aussage; jeder Absatz aus einem Entwurf kommt nach `mein/ki-stellen.md`, und der Protokolleintrag folgt. Für Stilbefunde verweist der Skill auf `humanizer-de` im Modus Formal; ein Einsatz dort ist dokumentationspflichtig und ab substanzieller Umformulierung kennzeichnungspflichtig (`regeln/ki-kennzeichnung.md`, Stufe 5 und Abschnitt 11). Im Check selbst formuliert er keine Ersatzsätze.
7. Fragst du nach einer Note, Punkten oder einer Gesamtstufe, wiederholt der Skill den Hinweis oben.

## Referenzdateien und wann sie gelesen werden

Die Referenzdateien teilt dieser Skill mit `abgabe`; sie liegen dort. Die Pfade `../abgabe/references/…` sind relativ zu diesem Skill-Ordner; vom Setup-Ordner aus liegen dieselben Dateien unter `.claude/skills/abgabe/references/`. In der App (Cowork) liest er sie dort aus dem freigegebenen Setup-Ordner. Findet er sie nicht, sagt er das, statt ihren Inhalt zu raten, und verweist darauf, den ganzen Setup-Ordner freizugeben (`fuer-die-app/ANLEITUNG.md`). Die Regelwerke in `regeln/` lädt der Skill nur an den Stellen, an denen diese Datei oder eine Referenzdatei auf sie verweist, nicht alle auf einmal.

| Datei | Wann | Wofür |
|---|---|---|
| `../abgabe/references/ordnung.md` | Phase 1, bei Bedarf | Pflichtteile, Begleitprotokoll, Abgabe, Beurteilung nach der Prüfungsordnung AHS; Begriffe |
| `../abgabe/references/rechtsrahmen.md` | Phase 1, bei Bedarf | wer beurteilt, was der Raster bindet, Variante A und B, KI-Nutzung, Vertraulichkeit |
| `../abgabe/references/formalia-checkliste.md` | Phase 2 | Blöcke 2 bis 4 für die vorliegenden Kapitel, je Punkt der Prüfschritt |
| `../abgabe/references/kriterien.md` | Phase 3, Beginn | die dreizehn Kriterien, Stufen, Prüffragen, Fundstellenpflicht |
| `../abgabe/references/beurteilungsformular.md` | Phase 3, nach kriterien.md | Aufbau des Formulars, Abstract-Test, warum Selbstbegrenzung zählt |
| `../abgabe/references/anforderungen.md` | Phase 3 | Erwartungen aus der Handreichung als Basis für die Rücksprache mit der Betreuungsperson |
| `../abgabe/references/bericht-vorlage.md` | Phase 6 | Aufbau und Register des Berichts |
| `../abgabe/references/ki-offenlegung.md` | Phase 6 und bei jeder Frage zu Protokoll, Kennzeichnung oder Hilfsmittelverzeichnis | Protokolleintrag, Zeile für das Hilfsmittelverzeichnis, Abgleich der KI-Stellen |
