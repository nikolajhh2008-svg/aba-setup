---
name: abgabe
description: Endkontrolle vor der Abgabe – Selbstcheck der ganzen Arbeit gegen die dreizehn Kriterien des ABA-Beurteilungsrasters, Formalia, Offenlegung (Begleitprotokoll, Kennzeichnung im Text, Liste der KI-Stellen) und Abgabeweg, mit Fundstellen und Prioritätenliste. Kein Gutachten, keine Note; ändert keine Datei der Arbeit. Nutzen bei „Abgabe“, „Endkontrolle“, „bin ich fertig“, „was fehlt noch“, „prüf die Formalia“.
license: MIT
---

Übertragen aus `bladewing/thesis-check`, Skill `selbstcheck` (Lukas Iffländer, MIT-Lizenz, Stand 43c572b vom 07.09.2026, siehe `LICENSE.txt`), angepasst an die ABA. Stand dieser Fassung: 2026-09-25. Änderungen: die elf HTW-Gutachtenkriterien durch die dreizehn Kriterien des amtlichen ABA-Beurteilungsrasters (Variante A) ersetzt; Gewichte, Punkte und Notenbereich durch eine vorläufige Stufeneinschätzung je Kriterium ersetzt; Formalia nach Prüfungsordnung AHS und Handreichung, Abgabeweg nach dem ABA-Portal; KI-Erklärung durch Begleitprotokoll, Kennzeichnung im Text und Abgleich mit `mein/ki-stellen.md` ersetzt; Gutachterzitat durch einen neutralen Hinweis ersetzt; Codeprüfung durch die Prüfung von Rohdaten und Material ersetzt; HTW-Ordnungen, Matrikelnummer und Sperrvermerk gestrichen oder durch die ABA-Entsprechung ersetzt; Bericht ohne Tabellen; der Modus Zwischenstand liegt im Skill `kritik`.

# Selbstcheck vor der Abgabe

Du prüfst deine eigene abschließende Arbeit vor der Abgabe gegen die dreizehn Kriterien des amtlichen Beurteilungsrasters, an dem sich die Beurteilung orientiert. Der Skill liest deine Arbeit, dein Begleitprotokoll und deine Liste der KI-Stellen, sammelt Befunde mit Fundstellen, sortiert sie nach Hebel und schreibt einen Bericht neben die Arbeit. Er ersetzt weder dein eigenes Lesen noch das Gespräch mit deiner Betreuungsperson.

Argumente dieses Aufrufs: `$ARGUMENTS` (erstes Argument: Pfad zur Arbeit; Schalter `--formalia`; was fehlt, wird in Phase 1 erfragt; steht hier nur der Platzhalter, wurden keine Argumente übergeben).

> **Hinweis:** „Dieser Check ist kein Gutachten; beurteilt wird von der Prüfungskommission. Er ist eine unverbindliche Hilfestellung und keine Zusage über eine Note. Abweichungen zwischen diesem Check und der Beurteilung sind zu erwarten. Dieser Check hat keinen Text deiner Arbeit geändert oder umformuliert.“

Zwei Dauerregeln, die in jeder Phase gelten:

- Der Skill ändert nie eine Datei der Arbeit und formuliert keine Ersatzsätze. Jeder Befund besteht aus Beobachtung, Fundstelle und Rückfrage an dich; Vorgehensweisen („eine Leitfrage durch alle Kapitel verfolgen“) sind erlaubt, fertige Formulierungen für deinen Text nicht. Einen Stilbefund begründet er mit der Wirkung auf die Leserin, nie mit einer vermuteten Herkunft des Textes. Es werden nur lesende Werkzeuge benutzt; geschrieben werden allein der Bericht sowie die Textfassung und die gerenderten Seiten unter `selbstcheck/`. Auch `mein/begleitprotokoll.md` und `mein/ki-stellen.md` ändert er nicht; den Protokolleintrag schlägt er im Bericht vor.
- Einziges Artefakt ist der Bericht aus Phase 6. Es gibt keine Note, keine Punkte, keine Prozentzahl, keine Ampel und keine Gesamtstufe für einen Kompetenzbereich oder die Arbeit, in keiner Phase und auf keine Nachfrage. Erlaubt ist je Kriterium eine vorläufige Einschätzung auf den Niveaustufen des Rasters, mit der Stelle, die sie trägt, und dem, was zur nächsten Stufe fehlt (`regeln/beurteilung.md`, Abschnitt 2). Fragst du nach einer Note, wiederholt der Skill den Hinweis oben, statt Zahlen zu nennen.

Außerhalb des Skills und darum hier nicht: Umformulieren (Skill `schreiben`), sprachliche Glättung (Skill `humanizer-de`), Literaturrecherche (Skill `quellen`), Arbeit an Thema und Leitfragen (Skill `thema`), eine Notenprognose (nirgends). Was du davon mit KI machst, gehört ins Begleitprotokoll und, wo Text aus einem Entwurf stammt, nach `mein/ki-stellen.md` (`references/ki-offenlegung.md`).

## Phase 0: Gate

Zuerst gibt der Skill den Hinweis oben wörtlich im Chat aus. Danach, vor jedem Dateizugriff, auch im Modus Formalia, stellt er diese fünf Fragen und wartet auf ausdrückliche Antworten. Ohne fünfmal Ja liest er nichts.

1. Ist das deine eigene Arbeit, und gibst du sie in eigener Verantwortung in dieses Werkzeug?
2. Enthält diese Fassung keine vertraulichen Unterlagen einer Partnerinstitution, oder hat die Partnerinstitution der Nutzung von KI-Werkzeugen schriftlich zugestimmt?
3. Sind alle Daten Dritter in dieser Fassung (Interviews, Umfrageantworten, Fotos oder Screenshots mit Personen) mit schriftlicher Einwilligung erhoben oder so anonymisiert, dass niemand erkennbar ist (`regeln/methodik.md`, Abschnitt 4)? Ob du deine eigenen Angaben auf dem Titelblatt (Name, Klasse, Schule) für den Check drinlässt oder entfernst, entscheidest du selbst.
4. Ist die Nutzung dieses Checks mit den Vorgaben deiner Betreuungsperson vereinbar? Ein generelles KI-Verbot ist bei der ABA nicht zulässig (KI-FAQ 1.5, `regeln/ki-kennzeichnung.md`, Abschnitt 4); Vorgaben zur Form der Kennzeichnung und zum Umfang der Dokumentation darf sie aber machen, und was in `mein/schulvorgaben.md` steht, gilt.
5. Weißt du, dass dieser Check keine Beurteilung ist, dass du ihn im Begleitprotokoll dokumentierst und dass du seinen Einsatz in der Diskussion begründen können solltest (K3.4)?

Bei Nein auf Frage 2 bricht der Skill ab. Das ist die einzige Stelle, an der er Nein sagt, und er begründet es: Vertrauliche Unterlagen einer Partnerinstitution gehören nicht zu einem Modellanbieter, auch nicht in Teilen. Zwei Wege bleiben dir: die Partnerinstitution um eine schriftliche Zustimmung zur Nutzung von KI-Werkzeugen bitten, oder ein lokal laufendes Modell nutzen, bei dem nichts deinen Rechner verlässt, zum Beispiel ein Agent wie OpenCode oder Codex CLI mit einem lokalen Modell über Ollama, der diese Datei liest. Auch dann gilt: Was die Vereinbarung mit der Partnerinstitution verlangt, ersetzt ein lokales Modell nicht; im Zweifel dort nachfragen.

Bei Nein auf Frage 1, 3, 4 oder 5 wartet der Skill. Er sagt dir, was fehlt (Drittdaten ohne Einwilligung entfernen oder anonymisieren; Vorgabe der Betreuungsperson klären), und macht erst weiter, wenn du es bestätigst.

Nach den fünf Ja folgt der feste Hinweis: Alles, was der Skill liest, geht an den Modellanbieter des Werkzeugs, das du gerade benutzt. Dieser Check beeinflusst deinen Arbeitsprozess und gehört deshalb ins Begleitprotokoll (KI-FAQ 1.2) und, wenn du eines führst, ins Hilfsmittelverzeichnis; den Vorschlag dafür liefert der Bericht (Teil 9). Freiwillig, aber empfohlen: Prüfe die Trainingseinstellung deines Kontos beim Modellanbieter und schalte die Nutzung deiner Eingaben zum Training aus.

## Phase 1: Material und Modus

1. Modus aus den Argumenten: Endcheck (Standard, fertige oder fast fertige Arbeit) oder `--formalia` (Gate, Phase 1 und 2, danach direkt der Bericht aus Phase 6). Für einen Zwischenstand mit den Kapiteln, die es schon gibt, ist der Skill `kritik` da.
2. Maßstab erfragen oder nachlesen: `mein/profil.md` und `mein/schulvorgaben.md`. Maßstab dieses Checks ist Variante A (schriftliche Arbeit mit forschendem Zugang). Steht dort Variante B (gestalterisch oder künstlerisch, auch bei forschendem Zugang), gelten die Formalia unverändert (`regeln/aufbau-der-arbeit.md`, Abschnitt 14) und K2 und K3 sind gleich, aber K1 ist ein anderer Kompetenzbereich; die sechs K1-Kriterien bleiben dann „offen“ mit Verweis auf den Raster B (`regeln/beurteilung.md`, Einleitung), und das steht so im Bericht. Steht dort eine BHS, gibt es keinen zentralen Raster (`regeln/fristen-und-abgabe.md`, Abschnitt 7); die Kriterien kannst du trotzdem nutzen, auf eigene Verantwortung, und das steht dann im Bericht. Dazu `references/ordnung.md` und `references/rechtsrahmen.md` lesen: was die Prüfungsordnung für die Arbeit verlangt, wer beurteilt und was der Raster bindet.
3. Material sammeln, ohne etwas zu öffnen, bis die Liste steht:
   - Die Arbeit (Pflicht). Für den Endcheck die PDF, weil das Portal nur PDF annimmt; eine Word-Datei (.docx) oder Markdown geht auch, dann entfallen Seitenangaben und die Prüfung der Abbildungen, und das steht im Bericht. Mit oder ohne Titelblatt (Gate-Frage 3).
   - Die Themeneinreichung, drei Fälle: genehmigtes Thema mit Leitfragen, angestrebten Methoden und Erwartungshorizont aus dem ABA-Portal oder aus `mein/profil.md` (dann wird die Beantwortung der Leitfragen in K1.3 Leitfrage für Leitfrage gemessen); nur der Titel (dann gegen den Titel und die Fragen, die die Einleitung selbst stellt; frag, ob die Einreichung vorliegt); nichts (dann bleibt dieser Teil von K1.3 offen, mit dem Rat, die Einreichung aus dem Portal beizulegen).
   - Das Begleitprotokoll (Pflicht für K1.1 und K1.2): `mein/begleitprotokoll.md` oder die PDF, die hochgeladen wird.
   - `mein/ki-stellen.md` und, wenn vorhanden, das Hilfsmittelverzeichnis (Pflicht für Block 4 der Formalia).
   - `mein/quellen.md`, optional; ohne sie werden Belege nur gegen das Literaturverzeichnis geprüft.
   - Rohdaten und Material, optional: Fragebogenauswertung, Tabellen, Interviewmemos, Einwilligungen. Ohne sie werden Zahlen und Interviewbelege nur aus dem Text beurteilt, und das steht so im Bericht.
   - Der Abgabetermin aus `mein/profil.md`, optional; er steuert die Linie in der Prioritätenliste. Steht dort keiner, fragt der Skill nach und rechnet keinen aus (`regeln/fristen-und-abgabe.md`, Abschnitt 1).
   - Die Vorgaben aus `mein/schulvorgaben.md` (Zitierweise, Umfang, Layout, Abgabeform); sie schlagen jede Regel aus `regeln/`.
4. Nachsehen, ob neben der Arbeit ein früherer Bericht `selbstcheck_*.md` liegt, auch einer aus dem Skill `kritik`; wenn ja, für Phase 6 vormerken.
5. Modus, Maßstab und Material in wenigen Zeilen spiegeln, dann ohne weitere Rückfragen durchlaufen. Rückfragen sammelt der Skill für den Bericht, statt dich zwischendurch zu unterbrechen.

## Phase 2: Formalia

`references/formalia-checkliste.md` lesen und Punkt für Punkt abarbeiten: Pflichtbestandteile in Dokumentreihenfolge, Vorlagenreste und Arbeitsmarker, Konsistenz zwischen Verzeichnissen, Verweisen und Text, Offenlegung und Abgabeweg. Jeder Punkt hat dort einen deterministischen Prüfschritt mit poppler-Werkzeugen (pdfinfo, pdftotext, pdffonts, pdfimages) oder, bei .docx und Markdown, mit einer Textfassung; das Ergebnis ist eine Liste Bestandteil · Vorhanden · Fundstelle · Anmerkung. Andere Befehle als die poppler-Werkzeuge (grep, awk, sed, sort, wc, python3) fragt dein Werkzeug einzeln ab; alle lesen nur. grep meldet Exit 1, wenn es nichts findet; bei Suchen mit erwartet leerem Ergebnis ist das der Normalfall.

Blocker, kein Formfehler, sondern ein Prüfungsproblem, sind vier Befunde: ein fehlender Pflichtteil nach § 8 Abs. 4 Prüfungsordnung AHS (die Arbeit ist dann formal unvollständig); ein fehlendes Begleitprotokoll (§ 9 Abs. 2); eine Stelle aus `mein/ki-stellen.md` ohne Kennzeichnung im Text (Überarbeiten hebt die Pflicht nicht auf, und genau dieses Weglassen ist der Täuschungstatbestand, `regeln/ki-kennzeichnung.md`, Abschnitte 6 und 7); ein Titel auf dem Titelblatt, der vom genehmigten Titel im Portal abweicht (`regeln/aufbau-der-arbeit.md`, Abschnitt 3). Der Bericht nennt Blocker an erster Stelle und verweist auf `references/ki-offenlegung.md`. Hast du Titelblatt oder andere Teile nur aus dieser Fassung entfernt (Gate-Frage 3), sag das; dann steht in der Liste „aus dieser Fassung entfernt, von dir bestätigt“ statt einer Fundstelle, mit dem Hinweis, dass ihr Inhalt hier nicht geprüft wurde.

Im Modus Formalia endet die Prüfung hier: weiter mit Phase 6. Der Bericht enthält dann nur Kopf, Prioritätenliste aus den Formalia-Befunden, Formalia, „Nicht geprüft“ und den Vorschlag für Protokoll und Hilfsmittelverzeichnis; keine Kriterienbefunde.

## Phase 3: Lektüre, Fundstellen, Material, Abbildungen

1. `references/kriterien.md` vollständig lesen, dann `references/beurteilungsformular.md`: Es zeigt, wie das Beurteilungsformular aufgebaut ist und was die Kommission aus der Arbeit mitnimmt; der Abstract-Test daraus gehört zu K1.3 und K1.4.
2. Die Arbeit vollständig lesen (`pdftotext -layout`, kapitelweise; bei .docx und Markdown die Textfassung aus Phase 2), nicht nur Einleitung und Schlusskapitel. Zu jedem der sechs schriftlich geprüften Kriterien K1.1 bis K1.6 mindestens eine Fundstelle sammeln, positiv wie negativ: Kapitel, Seite, Absatz, Fußnote, Abbildungs- oder Tabellennummer, Protokolleintrag mit Datum. Ohne Fundstelle gibt es keinen Befund; eine Wertung ohne Fundstelle wird gestrichen, nicht umformuliert.
3. Roter Faden: jede Leitfrage (es sind drei bis fünf) von der Einleitung über das Kapitel, das sie bearbeitet, und dessen Zwischenergebnis bis ins Schlusskapitel verfolgen und den Weg im Bericht festhalten (K1.3 und K1.4).
4. Belege: eine Stichprobe von Belegen gegen das Literaturverzeichnis und `mein/quellen.md` halten. Steht die Quelle dort, deckt sich die Seitenangabe mit den belegten Stellen, und trägt die Stelle, soweit die Notizen es zeigen, die Aussage? Die Rückfrage, ob jeder Beleg selbst geprüft wurde, steht ausdrücklich im Bericht; sie ist unangenehm und die wichtigste dieser Liste (KI-FAQ 1.2, Bedingung 3).
5. Liegen Rohdaten oder Material vor: die berichteten Zahlen daraus nachrechnen, und prüfen, ob die Arbeit bei kleinen Stichproben Personen statt Prozent nennt und sagt, was ihre Auswahl nicht zeigen kann (`regeln/methodik.md`, Abschnitt 5). Bei Interviews: Leitfaden im Anhang, Einwilligungen, Zitate mit präziser Fundstelle (Interview, Minute oder Zeile) und, wenn ein Transkriptionswerkzeug benutzt wurde, ein Eintrag dazu im Begleitprotokoll (`regeln/methodik.md`, Abschnitt 4). Rechne damit, dass die Kommission in der Diskussion danach fragt.
6. `references/anforderungen.md` als Erwartungsliste durchgehen. Nicht jeder Punkt passt zu jeder Arbeit; was nicht passt, wird nicht als Mangel geführt, sondern als Frage für die Rücksprache mit deiner Betreuungsperson notiert. Was in `mein/schulvorgaben.md` steht, geht vor.
7. Abbildungen nur gerendert beurteilen, nie aus dem extrahierten Text: `pdftoppm -f <Seite> -l <Seite> -r 110 -png arbeit.pdf selbstcheck/seite`, dann die PNG ansehen; fehlt pdftoppm, die Seite mit dem Lesewerkzeug des Agenten direkt aus der PDF anzeigen. Raster oder Vektor über `pdfimages -list arbeit.pdf` bestimmen. Konkrete Abbildungsnummern nennen, positiv wie negativ. Liegt keine PDF vor, bleibt dieser Teil offen, mit dem Rat, eine PDF zu exportieren.
8. Sprache: `werkzeuge/text-pruefen.py` über die Arbeit laufen lassen (es liest .md, .txt und .docx; bei einer PDF die Textfassung `selbstcheck/arbeit.txt`) und mit dessen Fundstellenliste arbeiten, nicht mit dem Eindruck (`regeln/sprache-pruefen.md`, Abschnitt „Was wirkt und was Aberglaube ist“). Befunde als Häufung, nicht als Einzelfund (K1.5).

## Phase 4: Kriterienbefunde

Die dreizehn Kriterien stammen aus dem amtlichen Beurteilungsraster, Variante A (`regeln/beurteilung.md`). Der Raster ist eine unverbindliche Orientierungshilfe; die Gewichtung liegt im Ermessen der Prüferin oder des Prüfers und der Kommission, und die Zählung K1.1 bis K3.4 ist eine Hilfszählung, keine amtliche Bezeichnung. Die Prüffragen in `references/kriterien.md` sind die Lesart dieses Setups; die Kommission liest nach eigenem Ermessen.

| Nr. | Kriterium | Geprüft |
|---|---|---|
| K1.1 | Konzeption, Planung, Durchführung und Dokumentation des Arbeitsprozesses | schriftlich, mit Begleitprotokoll |
| K1.2 | Umgang mit Hilfestellungen und technischen Hilfsmitteln | schriftlich, mit Begleitprotokoll |
| K1.3 | Inhalt der schriftlichen Arbeit | schriftlich |
| K1.4 | Aufbau der schriftlichen Arbeit | schriftlich |
| K1.5 | Sprachliche Gestaltung der schriftlichen Arbeit | schriftlich |
| K1.6 | Formale Gestaltung der schriftlichen Arbeit | schriftlich |
| K2.1 | Inhalt und Struktur der Präsentation | mündlich |
| K2.2 | Sprachliche Realisierung und Interaktion | mündlich |
| K2.3 | Gestaltung und Visualisierung | mündlich |
| K3.1 | Sachkompetenz und Argumentationsfähigkeit | mündlich |
| K3.2 | Sprachliche Realisierung | mündlich |
| K3.3 | Reflexion des Arbeitsprozesses und der Ergebnisse | mündlich |
| K3.4 | Auswahl und Verwendung technischer Hilfsmittel | mündlich |

Je Kriterium K1.1 bis K1.6 hält der Skill fest:

- Einschätzung, als vorläufig gekennzeichnet: eine der Spalten des Rasters („nicht erfüllt“ · „das Wesentliche überwiegend erfüllt“ · „das Wesentliche zur Gänze erfüllt“ · „über das Wesentliche hinausgehend erfüllt“ · „weit über das Wesentliche hinausgehend erfüllt“) oder „offen“, immer mit Grund (Material fehlt, Kapitel fehlt, Themeneinreichung nicht vorgelegt, Variante B).
- Befund in zwei bis vier Sätzen, in dritter Person über die Arbeit, mit Fundstellen: welche Stelle die Stufe trägt und was zur nächsten Stufe fehlt. Den Wortlaut eines Deskriptors zitiert der Skill nur, wo er in `regeln/beurteilung.md` steht; manche Deskriptoren lauten auf zwei Stufen gleich, die Differenzierung ergibt sich dann aus der Gesamtbetrachtung (ebd., Abschnitt 2).
- Maßnahme als Todo im Infinitiv mit Aufwand (Minuten, Stunden, Tage); zeigt der Befund keinen Handlungsbedarf, darf sie „nichts“ lauten.

Die höchste Stufe behauptet eine umfassende, durchgehende Leistung und braucht eine tragende Fundstelle.

K2.1 bis K3.4 bleiben immer „offen: wird mündlich geprüft“. Der Skill nennt dort statt einer Einschätzung die Stelle der Arbeit oder des Begleitprotokolls, die das Kriterium vorbereitet, und verweist für das Üben auf den Skill `pruefung`.

Eine Gesamtstufe je Kompetenzbereich oder eine Note wird nicht gebildet, auch nicht intern (`regeln/beurteilung.md`, Abschnitt 7).

## Phase 5: Untergrenze und Prioritätenliste

Wird ein K1-Kriterium vorläufig als „nicht erfüllt“ eingeschätzt, steht im Bericht ausdrücklich die einzige harte Zuordnungsregel des Rasters: Für eine positive Beurteilung muss jeder der drei Kompetenzbereiche zumindest „überwiegend erfüllt“ sein; ein einzelnes nicht erfülltes Kriterium führt aber nicht zwangsläufig zu einem negativ bewerteten Kompetenzbereich (`regeln/beurteilung.md`, Abschnitt 2a). Dazu der Rat, vor der Abgabe das Gespräch mit deiner Betreuungsperson zu suchen und den Bericht als Gesprächsgrundlage zu nehmen, nicht als Urteil.

Prioritätenliste, in dieser Reihenfolge: Blocker aus Phase 2; großer Hebel (eine Einschätzung unter „das Wesentliche zur Gänze erfüllt“ in K1.1 bis K1.4: dort liegen die Beantwortung der Leitfragen und die Dokumentation des Arbeitsprozesses, und beides wird in der Diskussion unter K3.1, K3.3 und K3.4 noch einmal gefragt); schnelle Gewinne (kleiner Aufwand, sichtbare Wirkung, oft K1.5 und K1.6); kann warten (Wünschenswertes ohne Einfluss auf eine Einschätzung). Je Eintrag: Was · Wo · Kriterium · Aufwand. Ist der Abgabetermin bekannt, zieht der Skill eine Linie „schaffbar“ / „nur wenn Zeit bleibt“ und rechnet dabei Druck und Bindung mit ein, mindestens drei Tage vor der Abgabe (`regeln/fristen-und-abgabe.md`, Abschnitt 5).

## Phase 6: Bericht

1. `references/bericht-vorlage.md` füllen; alle Teile, die der Modus vorsieht, in der Reihenfolge der Vorlage. Für Teil 9 den Protokolleintrag und die Zeile für das Hilfsmittelverzeichnis nach `references/ki-offenlegung.md` mit echten Werten füllen: Werkzeug und Modell, Stand des Skills (aus der Zeile unter dem Frontmatter dieser Datei; derselbe Wert steht im Berichtskopf), Datum, Anzahl der Durchläufe, Umfang des geprüften Materials. Den Satz, was du mit den Befunden gemacht hast, schreibt der Skill nicht; er lässt die Stelle sichtbar frei und fragt danach (`regeln/begleitprotokoll.md`, Abschnitt 6).
2. Register des Berichts: du für die Ansprache, dritte Person über die Arbeit („die Arbeit belegt“, nicht „du belegst“), Todos im Infinitiv, jeder Absatz und jeder Listenpunkt eine Zeile. Keine Markdown-Tabellen, weil nicht jeder Editor sie darstellt; Überschriften und Listen. Keine Note, keine Punkte, keine Gesamtstufe.
3. Datei `selbstcheck_<JJJJ-MM-TT>.md` neben die Arbeit legen, im Modus Formalia `selbstcheck_<JJJJ-MM-TT>_formalia.md`. Textfassung und gerenderte Seiten liegen unter `selbstcheck/` neben der Arbeit. Beides gehört nicht in die Abgabe und nicht ins Portal: Hinweis im Chat. Läuft der Skill ohne Dateizugriff, etwa im Chat der App, steht der Bericht vollständig im Chat.
4. Liegt ein früherer Bericht daneben (Phase 1, Schritt 4), beginnt der Bericht mit dem Abschnitt „Seit dem letzten Check“: erledigt, neu, unverändert offen, und die Kriterien, deren Einschätzung sich verschoben hat.
5. Im Chat nur drei Dinge: die drei wichtigsten Punkte der Prioritätenliste, der Hinweis aus Phase 5, falls ein Kriterium vorläufig als „nicht erfüllt“ eingeschätzt ist, und der Pfad des Berichts. Alles Weitere steht in der Datei.
6. Fragst du danach nach einer Note, Punkten oder einer Gesamtstufe, wiederholt der Skill den Hinweis oben. Bittest du um Umformulierungen oder Korrekturen im Text, verweist er auf den Skill `schreiben`, wo jeder Absatz aus einem Entwurf nach `mein/ki-stellen.md` kommt. Und er erinnert daran, was danach kommt: Sieben der dreizehn Kriterien werden mündlich geprüft; nach der Abgabe beginnt Etappe 7 (Skill `pruefung`).

## Referenzdateien und wann sie gelesen werden

Die Regelwerke in `regeln/` lädt der Skill nur an den Stellen, an denen diese Datei oder eine Referenzdatei auf sie verweist, nicht alle auf einmal.

| Datei | Wann | Wofür |
|---|---|---|
| `references/ordnung.md` | Phase 1 | Pflichtteile, Begleitprotokoll, Abgabe, Beurteilung und Präsentation nach der Prüfungsordnung AHS; Begriffe |
| `references/rechtsrahmen.md` | Phase 1 | wer beurteilt, was der Raster bindet, Variante A und B, KI-Nutzung, Vertraulichkeit, Datenschutz |
| `references/formalia-checkliste.md` | Phase 2 | Pflichtbestandteile, Vorlagenreste, Konsistenz, Offenlegung, Abgabeweg, je Punkt der Prüfschritt |
| `references/kriterien.md` | Phase 3, Beginn | die dreizehn Kriterien, Stufen, Prüffragen, Fundstellenpflicht |
| `references/beurteilungsformular.md` | Phase 3, nach kriterien.md | Aufbau des Formulars, Abstract-Test, warum Selbstbegrenzung zählt |
| `references/anforderungen.md` | Phase 3 | Erwartungen aus der Handreichung als Basis für die Rücksprache mit der Betreuungsperson |
| `references/bericht-vorlage.md` | Phase 6 | Aufbau und Register des Berichts |
| `references/ki-offenlegung.md` | Phase 6 und bei jeder Frage zu Protokoll, Kennzeichnung oder Hilfsmittelverzeichnis | Protokolleintrag, Zeile für das Hilfsmittelverzeichnis, Abgleich der KI-Stellen |
