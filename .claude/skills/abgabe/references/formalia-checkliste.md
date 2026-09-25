# Formalia-Checkliste

Übertragen aus `bladewing/thesis-check`, Datei references/formalia-checkliste.md (Lukas Iffländer, MIT-Lizenz, siehe `LICENSE.txt` im Skill-Ordner); Pflichtbestandteile nach Prüfungsordnung AHS und Handreichung statt HTW-Richtlinien, Vorlagenreste des thesis-template durch allgemeine Marker und die Musterbeispiele aus FAQ und Setup ersetzt, KI-Erklärung durch den Block „Offenlegung“ ersetzt, Block „Abgabeweg“ neu nach `regeln/fristen-und-abgabe.md`.

Für Phase 2 des Checks. Diese Phase ist deterministisch: Jeder Punkt hat einen Einzeiler, dessen Ausgabe der Befund ist; die Einschätzung kommt danach und stützt sich auf die Ausgabe, nicht auf den Eindruck. Im Modus Formalia endet der Skill `abgabe` nach dieser Datei mit dem Bericht `selbstcheck_<JJJJ-MM-TT>_formalia.md`, der Kopf, Prioritätenliste aus den Formalia-Befunden, den Teil „Formalia“, „Nicht geprüft“ und den Vorschlag für Protokoll und Hilfsmittelverzeichnis enthält, ohne Kriterienbefunde. Im Skill `kritik` (Zwischenstand) gelten nur die Blöcke 2 bis 4, und nur für die vorliegenden Kapitel; Block 5 entfällt.

## Vorbereitung

- Werkzeuge: poppler-utils (pdfinfo, pdftotext, pdffonts, pdfimages, pdftoppm) sowie grep, awk, sed, sort, wc (GNU-Varianten und eine UTF-8-Locale vorausgesetzt; unter macOS kommen die poppler-Werkzeuge über Homebrew, Paket `poppler`). grep beendet sich mit Exit 1, wenn es nichts findet; bei allen Suchen, deren Erwartung leer ist, und bei `grep -c` mit Ergebnis 0 ist das der Normalfall, kein Fehler. Prüfen mit `for t in pdfinfo pdftotext pdffonts pdfimages pdftoppm; do command -v "$t" >/dev/null || echo "fehlt: $t"; done`. Fehlt poppler, bleibt der Fallback, die PDF seitenweise mit dem Lesewerkzeug des Agenten zu lesen; die Einzeiler entfallen dann, und die Liste wird von Hand gefüllt, mit dem Vermerk „ohne Werkzeug geprüft“.
- Alle Befehle laufen im Ordner, in dem die Arbeit liegt, im Setup meist `mein/arbeit/`; `arbeit.pdf` steht für den Dateinamen der Arbeit. Dateien des Setups sprichst du von dort mit ihrem relativen Pfad an: `../ki-stellen.md`, `../begleitprotokoll.md`, `../quellen.md`, `../../werkzeuge/text-pruefen.py`. Ausgaben wandern nach `selbstcheck/`, das nicht in die Abgabe gehört.
- Textfassung anlegen, je nach Format der Arbeit:
  - PDF: `mkdir -p selbstcheck && pdftotext -layout arbeit.pdf selbstcheck/arbeit.txt`. In der Textfassung sind Seiten durch Formfeed getrennt; die Seitennummer in den awk-Befehlen ist die physische Seite (1 = Titelblatt), nicht die gedruckte. Im Bericht steht die gedruckte Seitenzahl, wenn es eine gibt, sonst „physische Seite N“; Zeilennummern beziehen sich auf `selbstcheck/arbeit.txt`.
  - Word (.docx): `mkdir -p selbstcheck && python3 -c "import importlib.util as u, sys, pathlib; s = u.spec_from_file_location('tp', sys.argv[1]); m = u.module_from_spec(s); s.loader.exec_module(m); print(m.text_aus_docx(pathlib.Path(sys.argv[2])))" ../../werkzeuge/text-pruefen.py arbeit.docx > selbstcheck/arbeit.txt`. Das nutzt den Leser aus `werkzeuge/text-pruefen.py` und braucht nichts installiert. Fußnoten stehen in einer eigenen Datei der .docx und fehlen in dieser Fassung; sie holt `unzip -p arbeit.docx word/footnotes.xml | perl -pe 's#</w:p>#\n#g; s/<[^>]+>//g' > selbstcheck/fussnoten.txt`. Seitenzahlen gibt es in einer .docx nicht; Fundstellen sind dann Kapitel und Absatz, und die Punkte zu Seiten, Schriften und Bildern (3.2, 3.9, 3.10) bleiben offen.
  - Markdown: `mkdir -p selbstcheck && cat kapitel-*.md > selbstcheck/arbeit.txt` (Dateinamen anpassen); Fundstellen sind Datei und Zeile.
- Eckdaten (nur PDF): `pdfinfo arbeit.pdf` liefert Seitenzahl, Papierformat und Metadaten; `awk 'BEGIN{RS="\f"} END{print NR}' selbstcheck/arbeit.txt` muss dieselbe Seitenzahl ergeben.
- Gekürzte Fassung (Gate-Frage 3): Hast du eine Fassung ohne Titelblatt hochgeladen, findet der Skill es nicht. Dann prüfst du die betreffenden Zeilen selbst in der vollständigen Fassung, die Einzeiler laufen dort genauso, und bestätigst das Ergebnis im Chat; in der Liste steht „aus dieser Fassung entfernt, von dir bestätigt“ statt einer Fundstelle. Ein Blocker ist nur, was weder gefunden noch bestätigt ist.
- Die Suchmuster decken die deutschen Überschriften nach der Handreichung ab. Heißen deine Überschriften anders, passt du die Wörter an. Was `mein/schulvorgaben.md` zu Form und Reihenfolge vorgibt, geht vor.

## Block 1: Pflichtbestandteile in Dokumentreihenfolge

Sieben Teile verlangt § 8 Abs. 4 Prüfungsordnung AHS, und es sind genau sieben: Titelblatt, Abstract, Inhaltsverzeichnis, Einleitung, Hauptteil, Schlusskapitel, Literatur- und Quellenverzeichnis. Fehlt einer, ist die Arbeit formal unvollständig: Blocker. Reihenfolge laut Handreichung: Titelblatt · Abstract · gegebenenfalls Vorwort · Inhaltsverzeichnis · Einleitung als Kapitel 1 · Hauptteil mit Methodenbeschreibung und gegebenenfalls Diskussion · Schlusskapitel · Literatur- und Quellenverzeichnis · weitere Verzeichnisse (Abbildungen, Abkürzungen, Hilfsmittel) · zuletzt Anhang und Glossar (`regeln/aufbau-der-arbeit.md`, Abschnitte 1 und 11). Das Begleitprotokoll wird mit abgegeben, ist aber kein Kapitel der Arbeit. Eine grobe Landkarte liefert `grep -n -E '^\s*([0-9]+\s+)?(Abstract|Vorwort|Inhaltsverzeichnis|Inhalt|Einleitung|Schluss|Schlusskapitel|Fazit|Resümee|Literaturverzeichnis|Literatur- und Quellenverzeichnis|Quellenverzeichnis|Literatur|Abbildungsverzeichnis|Tabellenverzeichnis|Abkürzungsverzeichnis|Hilfsmittelverzeichnis|Anhang|Glossar)\s*$' selbstcheck/arbeit.txt`; Einträge des Inhaltsverzeichnisses mit Punktleiste und Seitenzahl fallen durch das Zeilenende-Muster heraus.

### 1.1 Titelblatt (Pflicht)

- Prüfen: `pdftotext -f 1 -l 1 -layout arbeit.pdf -`
- Erwartung: Thema der Arbeit, gegebenenfalls Untertitel, Name, Klasse, Name und Adresse der Schule, Name der Betreuungsperson, Abgabedatum; alle Felder gefüllt, keine Platzhalter (Block 2), keine Seitenzahl. Der Titel steht exakt so da, wie er nach der Zustimmung der Schulleitung im ABA-Portal steht (Block 3, Punkt 3.1). Muster des Ministeriums: `ABA_Titelblatt_Muster.docx` auf ahs-aba.at (`regeln/aufbau-der-arbeit.md`, Abschnitt 3).

### 1.2 Abstract (Pflicht)

- Seite finden: `awk 'BEGIN{RS="\f"} /(^|\n) *Abstract *(\n|$)/ {print "physische Seite " NR}' selbstcheck/arbeit.txt`
- Zeichen zählen (Näherung, inklusive Leerzeichen): `awk '/^ *Abstract *$/{f=1;next} f && /^ *(Vorwort|Inhaltsverzeichnis|Inhalt) *$/{exit} f' selbstcheck/arbeit.txt | tr -s ' \n\f' ' ' | wc -m`
- Erwartung: zirka 1.000 bis 1.500 Zeichen inklusive Leerzeichen (§ 8 Abs. 5); Thema, Problemformulierung, methodische Vorgehensweise und wesentliche Ergebnisse; Präsens; direkt nach dem Titelblatt, ohne Kapitelnummer, ohne Zitate und Fußnoten. Ist die Arbeit nach § 8 Abs. 6 in einer lebenden Fremdsprache verfasst, gibt es zwei Abstracts. Silbentrennung, Seitenzahlen und Zeilenumbrüche verschieben die Zählung um einige Zeichen; im Grenzbereich in der Textverarbeitung nachzählen. Ob das Abstract berichtet statt ankündigt, prüft Phase 3 (Abstract-Test in `beurteilungsformular.md`).

### 1.3 Vorwort (optional)

- Prüfen: `grep -n -E '^\s*Vorwort\s*$' selbstcheck/arbeit.txt`
- Erwartung: nur Danksagung oder Widmung; die persönliche Motivation gehört in die Einleitung (`regeln/aufbau-der-arbeit.md`, Abschnitt 6).

### 1.4 Inhaltsverzeichnis (Pflicht)

- Prüfen: `grep -n -E '^\s*(Inhaltsverzeichnis|Inhalt)\s*$' selbstcheck/arbeit.txt` und die Einträge mit Punktleiste: `grep -n -E '\.( ?\.){3,}\s*[0-9IVX]+\s*$' selbstcheck/arbeit.txt | head -60`
- Erwartung: alle Kapitel und Unterkapitel mit exakt der Nummerierung und dem Wortlaut aus dem Text, mit Seitenzahlen; Verzeichnisse und Anhang ebenso; dezimal, in der Regel höchstens drei Ebenen; kein Eintrag für Titelblatt, Inhaltsverzeichnis und Begleitprotokoll. Seitenzahlen stimmen (Stichprobe: drei Einträge aufschlagen, Block 3, Punkt 3.2).

### 1.5 Einleitung (Pflicht)

- Prüfen: `grep -n -E '^\s*1\s+Einleitung\s*$' selbstcheck/arbeit.txt` und die Fragen in Kapitel 1: `awk '/^ *1 +Einleitung *$/{f=1} f && /^ *2 +[A-ZÄÖÜ]/{exit} f && /\?/' selbstcheck/arbeit.txt`
- Erwartung: Kapitel 1; die Forschungsfrage wörtlich als Frage und typografisch auffindbar, drei bis fünf Leitfragen, Begründung der Themenwahl, Vorgehensweise und Aufbauüberblick; keine Ergebnisse (`regeln/aufbau-der-arbeit.md`, Abschnitt 6). Findet die zweite Suche kein Fragezeichen, steht die Forschungsfrage höchstens sinngemäß im Text: ein Befund für Phase 3.

### 1.6 Hauptteil mit Methodenbeschreibung (Pflicht)

- Kapitel auflisten: `grep -n -E '^\s*[0-9]+\s+[A-ZÄÖÜ][^.]{2,}$' selbstcheck/arbeit.txt | grep -v -E '\s[0-9]+\s*$'` (wiederholte Treffer sind Kopfzeilen der Folgeseiten)
- Methodenbeschreibung finden: `grep -n -i -E '^\s*[0-9.]+\s+.*(Method|Vorgehen)' selbstcheck/arbeit.txt`
- Erwartung: nummerierte Kapitel zwischen Einleitung und Schlusskapitel; eine Beschreibung der angewandten Methoden, als eigenes Kapitel oder als Abschnitt (§ 8 Abs. 1a; ob eigenes Kapitel, ist offen). Findet die zweite Suche nichts, sucht Phase 3 die Beschreibung im Fließtext; fehlt sie ganz, ist das ein Befund zu K1.3, kein Blocker. Inhalt und roter Faden sind Sache von Phase 3.

### 1.7 Schlusskapitel (Pflicht)

- Prüfen: `grep -n -E '^\s*[0-9]+\s+(Schluss|Schlusskapitel|Fazit|Resümee|Schlussbetrachtung)' selbstcheck/arbeit.txt`
- Erwartung: das letzte Kapitel vor den Verzeichnissen; „Fazit“ und „Schluss“ sind als Überschrift zulässig. Ob es die Forschungsfrage erkennbar beantwortet und eine Schlussreflexion enthält, prüft Phase 3.

### 1.8 Literatur- und Quellenverzeichnis (Pflicht)

- Prüfen: `grep -n -E '^\s*(Literaturverzeichnis|Literatur- und Quellenverzeichnis|Quellenverzeichnis|Literatur)\s*$' selbstcheck/arbeit.txt`
- Kein KI-Werkzeug darin: `awk '/^ *(Literaturverzeichnis|Literatur- und Quellenverzeichnis|Quellenverzeichnis|Literatur) *$/{f=1} f && /^ *(Abbildungsverzeichnis|Tabellenverzeichnis|Abkürzungsverzeichnis|Hilfsmittelverzeichnis|Anhang|Glossar) *$/{exit} f' selbstcheck/arbeit.txt | grep -n -i -E 'ChatGPT|OpenAI|Claude|Anthropic|Copilot|Gemini|DeepL|Perplexity|Mistral'`
- Erwartung: vorhanden, nicht leer, jeder Eintrag vollständig im gewählten Zitierstil, Onlinequellen mit URL und Zugriffsdatum (Block 3, Punkt 3.7). Die zweite Suche bleibt leer: Sprachmodelle sind keine zitierfähigen Quellen und stehen nicht im Literaturverzeichnis (KI-FAQ 4.1 und 4.3); sie gehören ins Hilfsmittelverzeichnis. Ob jede Zitation einen Eintrag hat und jeder Eintrag zitiert wird, prüft Phase 3 unter K1.6.

### 1.9 Abbildungs-, Tabellen- und Abkürzungsverzeichnis (bei Bedarf)

- Vorkommen zählen: `for k in 'Abbildung|Abb\.' 'Tabelle|Tab\.'; do echo "$k: $(grep -c -E "^\s*($k) [0-9]+(\.[0-9]+)?" selbstcheck/arbeit.txt)"; done`
- Verzeichnisse finden: `grep -n -E '^\s*(Abbildungsverzeichnis|Tabellenverzeichnis|Abkürzungsverzeichnis)\s*$' selbstcheck/arbeit.txt`
- Erwartung: Wer Abbildungen hat, legt ein Abbildungsverzeichnis an; die Plattform des Ministeriums führt es als erforderlich, die Verordnung nicht (`regeln/aufbau-der-arbeit.md`, Abschnitt 1). Für Elementarten ohne Vorkommen keines. Ein Abkürzungsverzeichnis ersetzt nicht, jede Abkürzung bei der ersten Nennung auszuschreiben.

### 1.10 Hilfsmittelverzeichnis (optional, bei KI-Nutzung angezeigt)

- Prüfen: `grep -n -E '^\s*Hilfsmittelverzeichnis\s*$' selbstcheck/arbeit.txt` und der Bestätigungssatz der amtlichen Vorlage: `grep -n -F 'im vorliegenden Hilfsmittelverzeichnis' selbstcheck/arbeit.txt`
- Erwartung: nach dem Literatur- und Quellenverzeichnis; drei Spalten der Vorlage `ABA_Hilfsmittelverzeichnis.docx` (Hilfsmittel/Tool, Einsatzbereich und Zweck, relevanter Prompt); am Ende der Bestätigungssatz; jedes Werkzeug, das wesentlich beigetragen hat, auch Bild-, Ton- und Videoprogramme; dieser Check als eigene Zeile (`ki-offenlegung.md`). Offiziell optional, deshalb kein Blocker; stehen aber Einträge in `mein/ki-stellen.md` und fehlt das Verzeichnis, ist das ein Befund zu K1.2 (`regeln/aufbau-der-arbeit.md`, Abschnitt 11).

### 1.11 Anhang (optional)

- Prüfen: `grep -n -E '^\s*(Anhang|[A-Z]\s+[A-ZÄÖÜ][^.]{2,})\s*$' selbstcheck/arbeit.txt | grep -v -E '\s[0-9]+\s*$'` und der Vermerk zu beigelegten Dateien: `grep -n -i -E 'Datenträger|USB' selbstcheck/arbeit.txt`
- Erwartung: nur mit Inhalt und im Text verwiesen; Interviewleitfaden, Fragebogen, Einwilligungserklärungen, Transkriptauszüge, Rohdaten, gegebenenfalls maßgebliche Prompts (KI-FAQ 3.8); nicht das zentrale Argument. Ton- und separate Bilddateien liegen auf einem Datenträger bei den Druckexemplaren, mit Vermerk in der Arbeit (`regeln/aufbau-der-arbeit.md`, Abschnitt 11).

### 1.12 Begleitprotokoll (Pflicht, eigene Datei, Blocker)

- Prüfen: `ls -l ../begleitprotokoll.md` oder die PDF, die hochgeladen wird; Einträge: `grep -n -E '^### ' ../begleitprotokoll.md`
- Erwartung: vorhanden (§ 9 Abs. 2), mit Arbeitsablauf, Hilfsmitteln und Hilfestellungen, Vereinbarungen mit der Betreuungsperson und jedem KI-Einsatz; erster Eintrag bei der Themenfindung, nicht erst bei der Einreichung; Einträge in ganzen Sätzen und in der Ich-Form (`regeln/begleitprotokoll.md`). Nicht im Inhaltsverzeichnis der Arbeit. Vor der Abgabe in die amtliche Vorlage `ABA_Begleitprotokoll.docx` übertragen, sofern die Schule nichts anderes vorgibt. Lücken und offene Sätze prüft Block 4.
- Fehlt es: Blocker. Die Arbeit ist so nicht abgabefähig; der Bericht setzt das an die Spitze der Prioritätenliste.

### 1.13 Rechtliche Erklärung (Portal, nicht in der Arbeit)

- Prüfen: nichts im Text; von dir zu bestätigen.
- Erwartung: bei der Themeneinreichung unterschrieben oder mit ID Austria signiert und im Portal hochgeladen; bei der Abgabe bestätigst du, dass sie aktuell und korrekt ist. Ob die Schule zusätzlich ein unterschriebenes Exemplar im Druckstück erwartet, fragst du dort nach (`regeln/fristen-und-abgabe.md`, Abschnitt 4). Kein Blocker, außer die Schule verlangt die Erklärung in der Arbeit und sie fehlt.

## Block 2: Vorlagenreste und Arbeitsmarker

Alle Punkte sind Suchen, deren erwartetes Ergebnis leer ist; jeder Treffer ist ein Befund mit Seite und Zeile.

### 2.1 Platzhalter in eckigen Klammern

- Prüfen: `grep -n -E '\[[A-Za-zÄÖÜäöü][^]]{2,60}\]' selbstcheck/arbeit.txt`
- Erwartung: kein Treffer außer Zugriffsdaten der Form „[Zugriff: …]“ und, bei alphanumerischer Zitierweise, Zitatschlüsseln; beide werden überlesen.

### 2.2 Offene Belegstellen aus dem Skill `schreiben`

- Prüfen: `grep -n -F '[Beleg fehlt' selbstcheck/arbeit.txt`
- Erwartung: kein Treffer. Jeder Treffer ist eine Aussage ohne Beleg; großer Hebel für K1.3 und K1.6, und nie mit einer Quelle aus dem Gedächtnis zu füllen (`CLAUDE.md`, Abschnitt 2.1).

### 2.3 Datums- und Musterplatzhalter

- Prüfen: `grep -n -E 'TT\.MM\.JJJJ|JJJJ|Beispiel, das gelöscht werden kann' selbstcheck/arbeit.txt ../begleitprotokoll.md`
- Erwartung: kein Treffer; auch der Beispieleintrag im Kopf von `mein/begleitprotokoll.md` ist vor der Abgabe gelöscht.

### 2.4 Musterbeispiele aus FAQ und Setup

- Prüfen: `grep -n -E 'Microsoft Copilot, 12\.11\.2025|Futuristic city skyline|Calming Piano Vibes|home-automation-addon-pi|Kaffeehauskultur des Vormärz' selbstcheck/arbeit.txt`
- Erwartung: kein Treffer. Die Musterbeispiele der KI-FAQ und der Mustereintrag aus `mein/ki-stellen.md` beschreiben eine erfundene Nutzung; deine Kennzeichnungen beschreiben deine. Ist eines davon wirklich dein Thema, wird der Treffer überlesen.

### 2.5 Blindtext

- Prüfen: `grep -n -i -E 'lorem ipsum|dolor sit amet|consectetur' selbstcheck/arbeit.txt`
- Erwartung: kein Treffer.

### 2.6 Arbeitsnotizen und Marker

- Prüfen: `grep -n -E '\b(TODO|FIXME|TBD|XXX)\b|\?\?\?' selbstcheck/arbeit.txt` und `grep -n -i -E 'noch (schreiben|ergänzen|einfügen|prüfen|nachschauen)|hier fehlt|Quelle fehlt|Seite\?' selbstcheck/arbeit.txt`
- Erwartung: kein Treffer. Kommentare aus der Textverarbeitung erscheinen in einer PDF-Textfassung meist nicht; sie vor dem Export löschen, ist deine Sache.

## Block 3: Konsistenz

### 3.1 Titel identisch

- Titelblatt: `sed -n '1,25p' selbstcheck/arbeit.txt`; PDF-Metadaten: `pdfinfo arbeit.pdf | grep -E '^(Title|Author):'`; Vergleich mit dem genehmigten Titel aus dem Portal oder aus `mein/profil.md`.
- Erwartung: Der Titel auf dem Titelblatt ist wortgleich mit dem genehmigten Titel im ABA-Portal, einschließlich Schreibweise. Er erscheint wörtlich im Reifeprüfungszeugnis und ist nach der Zustimmung nicht mehr änderbar (`regeln/fristen-und-abgabe.md`, Abschnitt 3). Eine Abweichung ist ein Blocker. Die PDF-Metadaten sind entweder leer oder nennen denselben Titel und dich; ein fremder Name oder ein alter Arbeitstitel ist ein Befund.

### 3.2 Seitenzahlen durchgehend

- Letzte Zeile jeder Seite: `awk 'BEGIN{RS="\f"} {n=split($0,l,"\n"); for(i=n;i>0;i--) if(l[i] ~ /[^ \t]/){print NR": "l[i]; break}}' selbstcheck/arbeit.txt`
- Erwartung: eine der zwei Varianten der Handreichung, durchgehalten: Das Titelblatt zählt als Seite 1 ohne Nummer, Abstract, Vorwort und Inhaltsverzeichnis zählen mit, ohne Seitenzahl; oder Abstract, Vorwort und Inhaltsverzeichnis römisch, die Einleitung beginnt mit der arabischen 1 (`regeln/aufbau-der-arbeit.md`, Abschnitt 12). Ein Sprung, eine doppelte Nummer oder eine Textseite ohne Nummer ist ein Befund. Stichprobe gegen das Inhaltsverzeichnis: drei Einträge aus Punkt 1.4 aufschlagen (`pdftotext -f N -l N -layout arbeit.pdf - | head -5` mit der physischen Seite N) und prüfen, dass die Überschrift dort steht.

### 3.3 Keine unaufgelösten Verweise

- Prüfen: `grep -n -F '??' selbstcheck/arbeit.txt` und `grep -n -E 'Fehler! (Verweisquelle|Textmarke)|Error! (Reference source|Bookmark)' selbstcheck/arbeit.txt`
- Erwartung: kein Treffer. Die zweite Suche findet Querverweise der Textverarbeitung, deren Ziel gelöscht wurde.

### 3.4 Keine leeren Überschriften, höchstens drei Ebenen

- Aufeinanderfolgende Überschriften: `grep -n -E '^\s*[0-9]+(\.[0-9]+){0,2}\s+[A-ZÄÖÜ][^.]{2,}$' selbstcheck/arbeit.txt | awk -F: 'NR>1 && $1-prev<=2 {print "Kandidat: " prevline} {prev=$1; prevline=$0}'`
- Vierte Ebene: `grep -n -E '^\s*[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\s+[A-ZÄÖÜ]' selbstcheck/arbeit.txt`
- Fast leere Seiten: `awk 'BEGIN{RS="\f"} {t=$0; gsub(/[ \t\n]+/," ",t); if (length(t) < 120) print "physische Seite " NR " (" length(t) " Zeichen): " t}' selbstcheck/arbeit.txt`
- Erwartung: Unter jeder Überschrift steht mindestens ein Absatz eigener Text, bevor die nächste kommt; wer ein Kapitel 3.1 anlegt, braucht auch ein 3.2; in der Regel nicht mehr als drei Ebenen (`regeln/aufbau-der-arbeit.md`, Abschnitt 5). Kandidaten sind von Hand aufzuschlagen; ein Kapitel, das direkt mit seinem ersten Unterkapitel beginnt, ist üblich, eine Abschnittsüberschrift ohne Text darunter nicht.

### 3.5 Abbildungen und Tabellen im Text verwiesen, mit Quelle

- Prüfen: `for k in 'Abbildung|Abb\.' 'Tabelle|Tab\.'; do echo "== $k"; grep -o -E "($k) ?[0-9]+(\.[0-9]+)?" selbstcheck/arbeit.txt | sed -E 's/^[^0-9]*//' | sort -V | uniq -c; done`
- Quellenangabe in der Beschriftung: `grep -n -E '^\s*(Abbildung|Tabelle) [0-9]' selbstcheck/arbeit.txt | grep -v -i -E 'Quelle|eigene Darstellung|erstellt mit'`
- Erwartung: Jede Nummer kommt mindestens zweimal vor, einmal in der Beschriftung und mindestens einmal als Verweis im Text; Nummern mit genau einem Vorkommen sind Kandidaten, von Hand zu prüfen, weil ein Zeilenumbruch zwischen Wort und Nummer den Verweis verstecken kann. Jede Abbildung braucht eine Quellenangabe, auch die selbst erstellte („eigene Darstellung“); die zweite Suche listet Beschriftungen ohne erkennbare Quelle, die in der nächsten Zeile stehen kann. Verweise einheitlich „Abbildung“ oder „Abb.“, nicht gemischt.

### 3.6 Zitierweise einheitlich

- Zählen: `echo "Autor-Jahr: $(grep -o -E '\([A-ZÄÖÜ][a-zäöüß]+( et al\.| und [A-ZÄÖÜ][a-zäöüß]+| & [A-ZÄÖÜ][a-zäöüß]+)?,? [0-9]{4}[a-z]?' selbstcheck/arbeit.txt | wc -l)"; echo "Fußnotenzeilen: $(grep -c -E '^\s*[0-9]{1,3}\s+(Vgl\.|vgl\.|Ebd\.|ebd\.|[A-ZÄÖÜ][a-zäöüß]+,)' selbstcheck/arbeit.txt)"; echo "numerisch: $(grep -o -E '\[[0-9]+(,\s?[0-9]+)*\]' selbstcheck/arbeit.txt | wc -l)"`
- Erwartung: Eine Zählung überwiegt deutlich. Innerhalb des Stils einheitlich: „Vgl.“ nach der Vorgabe der Betreuungsperson (Regelfall: nur beim sinngemäßen Zitat), „ebd.“ entweder durchgehend oder gar nicht, Seitenangaben bei wörtlichen Zitaten, Literaturverzeichnis im selben Stil wie die Belege. Maßgeblich ist `mein/schulvorgaben.md`, sonst der gewählte Stil aus `regeln/zitierstile.md`.

### 3.7 Internetquellen mit Zugriffsdatum

- Zählen: `echo "URLs: $(grep -c -E 'https?://|www\.' selbstcheck/arbeit.txt) Zugriffsdaten: $(grep -c -i -E 'Zugriff|abgerufen' selbstcheck/arbeit.txt)"`
- Erwartung: Zu jeder Onlinequelle ein Zugriffsdatum im gewählten Format, etwa [Zugriff: TT.MM.JJJJ] (`regeln/aufbau-der-arbeit.md`, Abschnitt 11). Deutlich weniger Zugriffsdaten als URLs ist ein Befund; welche fehlen, zeigt die Liste im Verzeichnis. Dazu von dir zu bestätigen: Jede zitierte Webseite ist im Internet Archive gesichert, weil eine tote Fußnote in der Beurteilung wie eine erfundene wirkt (Etappe 6 in `FAHRPLAN.md`).

### 3.8 Sprache des Gerüsts einheitlich

- Prüfen: `echo "DE: $(grep -c -E '^\s*(Inhaltsverzeichnis|Abbildungsverzeichnis|Tabellenverzeichnis|Literaturverzeichnis|Hilfsmittelverzeichnis|Einleitung|Anhang)\s*$' selbstcheck/arbeit.txt) EN: $(grep -c -E '^\s*(Contents|List of Figures|List of Tables|Bibliography|References|Introduction|Appendix)\s*$' selbstcheck/arbeit.txt)"`
- Erwartung: Eine der beiden Zahlen ist null. Eine deutsche Arbeit mit englischen Verzeichnisüberschriften hat meist eine falsch eingestellte Dokumentsprache.

### 3.9 Schriften eingebettet (nur PDF)

- Prüfen: `pdffonts arbeit.pdf | awk 'NR>2 && $(NF-4) != "yes"'` und `pdffonts arbeit.pdf | grep -c 'Type 3'`
- Erwartung: erste Ausgabe leer (alle Schriften eingebettet), zweite Zahl null. Nicht eingebettete Schriften werden auf fremden Rechnern ersetzt und verschieben den Satz, auch im Druck. Die Handreichung empfiehlt höchstens zwei Schriftarten (`regeln/aufbau-der-arbeit.md`, Abschnitt 12); die Liste aus `pdffonts` zeigt, wie viele es sind.

### 3.10 Rasterbilder und Auflösung (nur PDF)

- Prüfen: `pdfimages -list arbeit.pdf` und `pdfimages -list arbeit.pdf | awk 'NR>2 && ($13+0) < 150 {print "physische Seite " $1 ": " $13 " ppi"}'`
- Erwartung: Diagramme und Schemata sind möglichst Vektorgrafiken und stehen dann nicht in der Liste; Fotos und Screenshots stehen drin und haben mindestens 150 ppi, besser 300, damit sie im Druck lesbar sind. Die inhaltliche Beurteilung der Abbildungen macht Phase 3 an gerenderten Seiten (`pdftoppm -f N -l N -r 110 -png arbeit.pdf selbstcheck/seite`), nie an der Textfassung.

### 3.11 Format und Layout

- Prüfen: `pdfinfo arbeit.pdf | grep -E '^(Pages|Page size):'`
- Erwartung: A4 (595 x 842 Punkte), Hochformat, alle Seiten gleich groß. Ränder, Schriftgröße und Zeilenabstand empfiehlt die Handreichung (Text 12 pt und 1,5-zeilig, Fußnoten 10 pt und einzeilig, linker Rand ca. 2,5 cm plus Bundsteg); entscheidend ist, was Schule oder Betreuungsperson vorgeben (`regeln/aufbau-der-arbeit.md`, Abschnitt 12). Die Seitenzahl ist eine Beobachtung für den Berichtskopf, kein Maßstab; ein Umfangslimit gibt es nicht.

## Block 4: Offenlegung

Zwei Pflichten, die laufend verwechselt werden: Dokumentation im Begleitprotokoll (Prozessebene) und Kennzeichnung an der Textstelle (Produktebene); die eine ersetzt die andere nicht (`regeln/ki-kennzeichnung.md`, Abschnitt 1). Dieser Block gleicht Liste, Text und Protokoll in beide Richtungen ab.

### 4.1 Jede Stelle der Liste ist im Text gekennzeichnet (Blocker)

- Einträge der Liste: `grep -n -E '^- [0-9]' ../ki-stellen.md` (der kursive Mustereintrag beginnt mit einem Sternchen und fällt heraus); noch offen markierte: `grep -n -F 'im Text gekennzeichnet: noch nicht' ../ki-stellen.md`
- Je Eintrag die Anfangsworte aus der Klammer im Text suchen: `grep -n -F '<Anfangsworte>' selbstcheck/arbeit.txt`, dann den Absatz und seine Fußnote aufschlagen (bei .docx in `selbstcheck/fussnoten.txt`).
- Erwartung: An jeder Stelle stehen Werkzeug und Datum, im Fließtext oder in der Fußnote, etwa nach dem Muster der FAQ „Werkzeug, TT.MM.JJJJ“ (KI-FAQ 4.2). Überarbeiten hebt die Pflicht nicht auf. Eine Stelle aus der Liste ohne Kennzeichnung im Text ist ein Blocker; ebenso ein Eintrag mit „im Text gekennzeichnet: noch nicht“. Findet sich die Stelle im Text nicht mehr, weil der Absatz gestrichen wurde, ist das kein Blocker, sondern eine Rückfrage: Dann gehört das in die Liste und ins Protokoll.

### 4.2 Jede Kennzeichnung im Text steht in der Liste

- Prüfen: `grep -n -E '(ChatGPT|Claude|Copilot|Gemini|DeepL|Perplexity|Mistral|Le Chat|DALL-E|Midjourney|Suno)[^.;]{0,60}[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{2,4}' selbstcheck/arbeit.txt` (bei .docx zusätzlich über `selbstcheck/fussnoten.txt`)
- Erwartung: Jeder Treffer im Fließtext, in Fußnoten und Beschriftungen gehört zu einem Eintrag in `mein/ki-stellen.md`; Treffer im Hilfsmittelverzeichnis werden überlesen. Ein Treffer ohne Eintrag ist kein Blocker, aber ein Befund: Die Liste ist unvollständig, und das Protokoll wird darauf geprüft (Punkt 4.3).

### 4.3 Das Protokoll deckt jede KI-Stelle, mit deinem Satz

- Daten vergleichen: die Daten der Einträge in `mein/ki-stellen.md` gegen `grep -n -E '^### ' ../begleitprotokoll.md`.
- Offene Lücken: `grep -n -F 'Diesen Satz ergänzt' ../begleitprotokoll.md`
- Erwartung: Zu jedem Datum, an dem eine KI-Stelle entstanden ist, gibt es einen Protokolleintrag, und jeder Eintrag zu einem KI-Einsatz enthält deinen Satz, was übernommen, verändert oder verworfen wurde und warum (KI-FAQ 1.1). Die zweite Suche bleibt leer; jeder Treffer ist eine Stelle, an der der Satz noch fehlt. Den Satz schreibt nur die Person, nie der Skill (`regeln/begleitprotokoll.md`, Abschnitt 6).

### 4.4 KI-Bilder, -Grafiken und -Tonspuren gekennzeichnet

- Prüfen: `grep -n -i -E '^\s*Abbildung [0-9].*(erstellt mit|generiert)' selbstcheck/arbeit.txt` gegen die Bild-, Ton- und Videowerkzeuge im Protokoll.
- Erwartung: Jede mit KI erstellte Abbildung trägt die Kennzeichnung in der Beschriftung, nach dem Muster der FAQ „Abbildung 1: Titel, erstellt mit Werkzeug, TT.MM.JJJJ“; Audio und Video im Abspann oder in den Shownotes (KI-FAQ 4.2, `regeln/ki-kennzeichnung.md`, Abschnitt 6).

### 4.5 Hilfsmittelverzeichnis vollständig

- Prüfen: die Liste „Verwendete Hilfsmittel“ im Kopf von `mein/begleitprotokoll.md` und die Werkzeuge aus 4.2 gegen das Hilfsmittelverzeichnis der Arbeit (Punkt 1.10).
- Erwartung: Jedes Werkzeug, das wesentlich zum Arbeitsprozess beigetragen hat, steht drin, auch dieser Check; keines steht im Literaturverzeichnis oder wird als Autorin oder Autor genannt (KI-FAQ 4.3 und 4.4).

## Block 5: Abgabeweg

Nur im Endcheck und im Modus Formalia. Die Verordnung verlangt die Abgabe digital, nicht per E-Mail, und zweifach ausgedruckt (§ 10); Portal, PDF-Format und Plagiatsdienst sind Verwaltungspraxis und können sich ohne Novelle ändern (`regeln/fristen-und-abgabe.md`, Abschnitte 2 und 4). Die meisten Punkte bestätigst du; der Skill fragt sie ab, statt sie anzunehmen.

### 5.1 Arbeit als PDF, höchstens 20 MB, lesbar

- Prüfen: `ls -lh arbeit.pdf && pdfinfo arbeit.pdf >/dev/null && echo lesbar`
- Erwartung: PDF, höchstens 20 MB; die Datei öffnet sich. Eine beschädigte Datei ist keine Abgabe.

### 5.2 Begleitprotokoll als eigene PDF

- Prüfen: dieselben Befehle für die PDF des Begleitprotokolls.
- Erwartung: eigene Datei, höchstens 20 MB, öffnet sich; zusätzlich liegt das Protokoll einem der beiden Druckexemplare bei. Ort, Datum und Unterschrift laut Vorlage nur auf der Beilage zu den ausgedruckten Exemplaren (`regeln/begleitprotokoll.md`, Abschnitt 6).

### 5.3 Abstract für das Portal

- Von dir zu bestätigen: Das Portal hat zwei Pflichtfelder für das Abstract; einzugeben ist es wortident, in kopierter Form, wie in der gedruckten Arbeit. Bei einer Arbeit auf Deutsch oder Englisch in beide Felder dieselbe Sprache; bei einer anderen Sprache ins erste Feld Deutsch oder Englisch, ins zweite die Sprache der Arbeit.

### 5.4 Druckexemplare und beigelegte Dateien

- Von dir zu bestätigen: zwei gedruckte Exemplare, Bindung nach Vorgabe der Schule, Druck und Bindung mindestens drei Tage vor der Abgabe; Ton- und separate Bilddateien auf einem Datenträger bei den Druckexemplaren, mit Vermerk in der Arbeit (Punkt 1.11).

### 5.5 Termin

- Prüfen: den Abgabetermin in `mein/profil.md` nachlesen.
- Erwartung: Verordnet ist das Ende der ersten Woche des zweiten Semesters; das konkrete Datum hängt an den Semesterferien des Bundeslandes und setzt die Schule. Steht keines im Profil, fragt der Skill danach und rechnet keines aus (`regeln/fristen-und-abgabe.md`, Abschnitt 1).

### 5.6 Hochladen

- Von dir zu bestätigen: Titel vorausgefüllt und geprüft; Abstract eingegeben und zwischengespeichert, erst danach lassen sich Dateien hochladen; Einwilligung zur Übermittlung an Turnitin (Pflicht); Bestätigung, dass die rechtliche Erklärung aktuell und korrekt ist; ob die Schule ein unterschriebenes Exemplar im Druckstück erwartet, ist geklärt. Nach dem Einreichen ist keine Bearbeitung mehr möglich.

## Ergebnisformat

Teil „Formalia“ des Berichts folgt `bericht-vorlage.md`: eine Liste für Block 1, darunter je eine Zeile für Block 2, Block 3 und Block 4, im Endcheck eine für Block 5, und eine Zeile „Blocker aus diesem Teil“. Keine Tabellen, weil der Bericht in Editoren gelesen wird, die sie nicht darstellen.

Block 1 als Liste mit einem Punkt je Bestandteil: Bestandteil · Vorhanden · Fundstelle · Anmerkung. Werte für „Vorhanden“: „ja“, „nein“, „entfällt: Grund“ (etwa „entfällt: keine Abbildungen“), „aus dieser Fassung entfernt, von dir bestätigt“ (gekürzte Fassung), „von dir bestätigt“ (Punkte ohne Prüfschritt). Die Fundstelle ist die gedruckte Seite oder „physische Seite N“ plus die Zeile in `selbstcheck/arbeit.txt`. In der Anmerkung stehen Blocker, Abweichungen von der Erwartung und die Maßnahme. Erfundenes Beispiel:

- Titelblatt: aus dieser Fassung entfernt, von dir bestätigt · – · Titelabgleich mit dem Portal (Punkt 3.1) in der Vollfassung selbst ausführen
- Abstract: ja · physische Seite 1, Zeile 3 · rund 1.380 Zeichen, Präsens; nennt Thema und Methode, aber kein Ergebnis (Abstract-Test, K1.3)
- Abbildungsverzeichnis: nein · – · sieben Abbildungen im Text, kein Verzeichnis
- Begleitprotokoll: ja · `mein/begleitprotokoll.md`, 14 Einträge · erster Eintrag bei der Themenfindung; zwei Einträge ohne deinen Satz (Block 4, Punkt 4.3)

Block 2 als eine Zeile „Vorlagenreste und Marker: …“: je Treffer Punkt, Fundstelle und Maßnahme, danach der Satz, welche Punkte ohne Treffer waren, damit sichtbar ist, was geprüft wurde. Block 3 als eine Zeile „Konsistenz: …“ und Block 4 als eine Zeile „Offenlegung: …“, je Prüfung Befund, Fundstelle und Maßnahme, Prüfungen ohne Befund in einem Halbsatz. Block 5 als eine Zeile „Abgabeweg: …“ mit dem, was geprüft, und dem, was von dir bestätigt ist. Danach die Zeile „Blocker aus diesem Teil: keine | …“.

Blocker stehen zusätzlich an der Spitze der Prioritätenliste (Phase 5). Was diese Checkliste nicht prüft: Rechtschreibung, Qualität der Quellen, Inhalt des Abstracts, Lesbarkeit der Abbildungen; das ist Sache von Phase 3 oder liegt außerhalb des Skills.
