---
name: sprache-pruefen
beschreibung: Prüfbare Verbotsliste gegen maschinentypisches Deutsch, mit Ersatzformulierungen und ausgewiesener Belegstärke
version: 1
stand: 2026-08-01
---

# Marker generischer Maschinensprache im Deutschen

Dieses Regelwerk hat zwei Aufgaben. Erstens: die Marker benennen, an denen ein
deutscher Text nach Sprachmodell klingt. Zweitens – und das ist der wichtigere
Teil – trennen, welche Gegenmaßnahmen tatsächlich wirken und welche Aberglaube
sind. Wer die wirkungslosen Maßnahmen mitführt, verbrennt Rechenzeit und
suggeriert eine Sicherheit, die es nicht gibt.

## Belegstärke – wie dieses Regelwerk seine Aussagen kennzeichnet

Jede Regel trägt eine von drei Marken:

- **[belegt]** – durch eine peer-reviewte Studie oder eine amtliche Sprachnorm
  gedeckt. Die Fundstelle steht dabei.
- **[plausibel]** – aus Praxisliteratur oder aus einer Studie mit
  nicht offengelegter Methodik; inhaltlich nachvollziehbar, aber nicht belegt.
- **[normativ]** – kein Echtheitsmarker, sondern eine Regel guten
  wissenschaftlichen Schreibens, die unabhängig von der Frage gilt, wer den Text
  verfasst hat.

Das ist kein Formalismus. Die belastbare Forschung zu Sprachmodellmarkern ist
fast vollständig englischsprachig und auf englische Korpora bezogen. Für
deutschsprachige Marker existiert im Wesentlichen Praxisliteratur, aber keine
auffindbare peer-reviewte Korpusstudie. Wer die deutsche Markerliste als belegt
ausgibt, behauptet mehr, als die Quellenlage hergibt.

Offene Aufgabe mit hohem Ertrag: ein eigener Messkorpus aus echten
deutschsprachigen Schülerarbeiten und modellgenerierten Texten zu denselben
Themen, gerechnet nach der offen dokumentierten Excess-Frequency-Methodik von
Kobak et al. (Repository: https://github.com/berenslab/llm-excess-vocab). Bis
das vorliegt, gelten die deutschen Wortlisten unten als [plausibel], nicht als
belegt.

---

## Schicht 1 – harte Zeichenfehler, automatisch korrigierbar

Dies ist der einzige Bereich, in dem eine Ersetzung ohne Rückfrage vertretbar
ist: eindeutige Regelverstöße gegen die deutsche Typografie, ohne
Bedeutungsrisiko, in Sekunden per Suchen-und-Ersetzen prüfbar.

### 1.1 Der Geviertstrich – der schärfste Marker im deutschen Text [belegt]

Regel: Im Deutschen ist der Gedankenstrich der **Halbgeviertstrich** U+2013
(„–") und wird beidseitig durch Leerzeichen abgetrennt. Der **Geviertstrich**
U+2014 ist in deutschen Fließtexten unüblich; er kommt allenfalls als längerer
Nullersatzstrich in Tabellen vor („45,— €").

Falsch: `Der Befund war eindeutig` U+2014 `alle drei Werkzeuge versagten.`
Richtig: `Der Befund war eindeutig – alle drei Werkzeuge versagten.`

Warum dieser eine Marker so scharf ist, ergibt sich aus dem Zusammentreffen von
drei Umständen:

1. Er ist im Deutschen nicht normgerecht. Quellen zur Norm:
   https://de.wikipedia.org/wiki/Halbgeviertstrich und
   https://www.typolexikon.de/gedankenstrich/ ; amtliches Regelwerk unter
   https://www.rechtschreibrat.com/
2. Deutsche Tastaturbelegungen erzeugen ihn nicht, und die Autokorrektur
   deutscher Textverarbeitung setzt ihn nicht. Ein Mensch, der auf einer
   deutschen Tastatur schreibt, tippt ihn praktisch nie.
3. Englischtrainierte Sprachmodelle produzieren ihn massenhaft. Eine Messung der
   Geviertstrich-Frequenz je 1.000 Wörter ergab für GPT-4.1 den Wert 10,62, für
   Claude Opus 4.6 den Wert 9,09, für DeepSeek V3 6,95 und für Metas
   Llama-Modelle 0. Quelle: https://arxiv.org/html/2603.27006v1

Zusatzbefund derselben Quelle: Die Frequenz ist gezielt feinjustierbar – Sam
Altman hat öffentlich bestätigt, dass sie in ChatGPT-Ausgaben nach Nutzerkritik
angepasst wurde. Der Marker ist also nicht naturgesetzlich, sondern eine
Trainingsartefakt-Signatur, die sich ändern kann. Als Prüfregel bleibt er
trotzdem gültig, weil die deutsche Norm unabhängig davon gilt.

Die dritte Variante ist die schlimmste: Geviertstrich mit Leerzeichen beidseits.
Diese Mischform aus englischem Zeichen und deutschem Abstand existiert in keiner
der beiden Typografien und ist damit der eindeutigste Hinweis überhaupt.

Ausnahmen, in denen U+2014 stehen bleiben darf: in Zeichenklassen regulärer
Ausdrücke, die Altbestand erkennen sollen, und dort, wo der Geviertstrich das
Gegenbeispiel ist – also in genau diesem Regelwerk.

### 1.2 Weitere automatisch korrigierbare Zeichenfehler [belegt, Sprachnorm]

- Gerade Anführungszeichen `"` und `'` statt der typografischen „…" und ‚…'
- Halbgeviertstrich im Gedankenstrich-Kontext ohne umgebende Leerzeichen
- Doppelte Leerzeichen; Leerzeichen vor Satzzeichen
- Auslassungspunkte als drei einzelne Punkte statt U+2026
- Fehlende geschützte Leerzeichen bei „S. 14", „z. B.", „Abb. 3", „Nr. 7",
  „vgl. S. 22" und bei Maßeinheiten („15 km", „30 %")
- Bindestrich statt Streckenstrich bei Spannen: „2010-2024" wird zu „2010–2024"
  (Halbgeviertstrich, hier ohne Leerzeichen)

---

## Schicht 2 – Wortlisten und Floskeln, nur markieren, nie ersetzen

Ab hier gilt: Es werden Fundstellen angezeigt und Ersatz vorgeschlagen, aber
nichts selbsttätig ersetzt. Ein Wort aus der Markerliste kann im Einzelfall
genau das richtige sein.

### 2.1 Der belegte englische Befund [belegt]

Die methodisch stärkste Arbeit ist die Excess-Vocabulary-Studie von Kobak et al.
Sie untersucht über 15 Millionen biomedizinische Abstracts aus PubMed der Jahre
2010 bis 2024 und überträgt die Methodik der Übersterblichkeitsrechnung auf
Wortfrequenzen. Befunde:

- Mindestens 13,5 Prozent der Abstracts des Jahres 2024 wurden mit
  Sprachmodellunterstützung verfasst; in einzelnen Teilkorpora bis zu 40 Prozent.
- Die Markerwörter des Jahres 2024 bestehen zu 66 Prozent aus Verben und zu
  14 Prozent aus Adjektiven. Frühere Frequenzverschiebungen (etwa durch Covid)
  wurden von Substantiven dominiert. Diese Verschiebung zu Verben und Adjektiven
  erzeugt den charakteristisch blumigen Klang.
- Extremwerte im Anstieg: „delves" 28-fach, „underscores" 13,8-fach,
  „showcasing" 10,7-fach.

Quellen: https://arxiv.org/abs/2406.07016 ,
https://www.science.org/doi/10.1126/sciadv.adt3813 ,
https://github.com/berenslab/llm-excess-vocab

Übertragbar auf das Deutsche ist daraus nicht die Wortliste, sondern das
Strukturmerkmal: **eine Häufung wertender Verben und Adjektive dort, wo ein
Fachtext Substantive und Sachverhalte erwartet.**

Eine Übersichtsarbeit zu linguistischen Merkmalen maschinell erzeugter Texte
nennt zusätzlich: formellerer und unpersönlicherer Stil, höherer Anteil von
Nomen, Determinierern und Adpositionen, geringerer Anteil von Adjektiven und
Adverbien, niedrigere lexikalische Vielfalt, kleinerer Wortschatz, repetitive
Muster. Die Autoren benennen selbst als Forschungslücke, dass die Forschung
stark auf Englisch und auf GPT-Modelle konzentriert ist. Quelle:
https://arxiv.org/abs/2510.05136

### 2.2 Deutsche Markerwörter [plausibel]

Wiederkehrend genannt in der Praxisliteratur. Je Wort ein tauglicher Ersatz –
und die Ersetzung besteht fast nie im Austausch des Wortes, sondern in der
Konkretisierung der Aussage.

- „essenziell" → „notwendig für X", oder: streichen und sagen, wofür genau
- „vielfältig" → die Vielfalt aufzählen: „in drei Formen: …"
- „nahtlos" → streichen; im Fachtext fast immer Werbesprache
- „maßgeschneidert" → „für X angepasst", mit Angabe, was angepasst wurde
- „ganzheitlich" → streichen oder benennen, welche Aspekte einbezogen sind
- „umfassend" → durch den Umfang ersetzen: „alle 14 geprüften Werkzeuge"
- „präzise" → durch den Wert ersetzen: „auf zwei Nachkommastellen"
- „eintauchen" (in ein Thema) → „untersuchen", „auswerten", „analysieren"
- „beleuchten" → „untersuchen", „darstellen"
- „revolutionär", „bahnbrechend", „wegweisend" → streichen; das sind Urteile
  ohne Maßstab
- „von entscheidender Bedeutung" → sagen, wofür es entscheidend ist

Quellen (Praxisliteratur, nicht begutachtet):
https://korrektur.de/ki-texte-erkennen-merkmale-checkliste ,
https://lillikoisser.at/ki-texte-erkennen/ ,
https://www.contentconsultants.de/ki-texte-erkennen-warum-man-texte-besser-selbst-schreibt/

### 2.3 Brückenfloskeln [plausibel und normativ]

Diese Wendungen sind unabhängig von ihrer Markerqualität schlechtes
wissenschaftliches Deutsch: Sie kündigen eine Aussage an, statt sie zu machen.

- „Es ist wichtig zu beachten, dass X." → „X."
- „Es ist entscheidend hervorzuheben, dass X." → „X."
- „In der heutigen Zeit / in der heutigen Gesellschaft" → streichen oder
  datieren: „seit der Novelle 2024"
- „spielt eine entscheidende Rolle" → das Verb einsetzen, das gemeint ist:
  „bestimmt", „begrenzt", „ermöglicht", „verhindert"
- „Insgesamt lässt sich festhalten, dass" → nur behalten, wenn danach etwas
  steht, das nicht schon dasteht
- „Zusammenfassend lässt sich sagen" → im Fazit überflüssig, weil dort ohnehin
  zusammengefasst wird
- „An dieser Stelle sei erwähnt" → erwähnen, ohne es anzukündigen
- „Nicht zuletzt", „Darüber hinaus", „Des Weiteren" als reine Reihung → durch
  einen Übergang ersetzen, der die logische Beziehung benennt (siehe
  `schreibweise.md`, Abschnitt 6)

Eine Praxisquelle nennt für „spielt eine entscheidende Rolle" 43 Prozent
Vorkommen in mutmaßlich maschinell erzeugten studentischen Einleitungen gegenüber
6 Prozent in nachweislich menschlichen. Die Methodik ist nicht offengelegt; die
Zahl wird hier als **plausibel, nicht belegt** geführt und darf nicht als Beleg
weiterzitiert werden – schon gar nicht in der eigenen Arbeit.

### 2.4 Satzmuster [plausibel und normativ]

- **„nicht nur …, sondern auch …"** – Zählung je 1.000 Wörter. Die Konstruktion
  ist nicht falsch, aber in maschineller Prosa stark überrepräsentiert. Ersatz:
  zwei Sätze, oder die Aufzählung ohne Aufwertungsrahmen.
  Negativ: „Die Methode ist nicht nur schnell, sondern auch kostengünstig."
  Positiv: „Die Methode ist schnell und kostet nichts."
- **Dreiergruppen** aus gleichrangigen Adjektiven oder Substantiven („intuitiv,
  schnell und effizient"). Ersatz: die Eigenschaft nennen, auf die es ankommt.
- **Zusammenfassungssatz am Absatzende, der nichts Neues sagt.** Beginnt
  typischerweise mit „Somit", „Damit", „Folglich", „Insgesamt",
  „Zusammenfassend". Prüfbar: Warnung, wenn mehr als ein Drittel der Absätze so
  endet.
- **Der Antithesen-Rahmen** „Es geht nicht um X, sondern um Y", wenn niemand X
  behauptet hat.

---

## Schicht 3 – statistische Merkmale, berechenbar ohne Modell

Diese Merkmale sind mit einer NLP-Bibliothek in unter einer Sekunde berechenbar
und kosten nichts. Sie sind der eigentliche Substanzteil der Prüfung, weil sie
nicht auf Wortlisten angewiesen sind.

- **Satzlängenvarianz je Absatz.** Der Marker ist nicht die Länge, sondern die
  Gleichförmigkeit. Startwert für die Warnung: Standardabweichung der
  Satzlängen innerhalb eines Absatzes unter 4 Wörtern. Der Schwellenwert ist am
  eigenen Korpus zu kalibrieren. [belegt für Englisch, übertragbar]
- **Absatzlängenverteilung.** Warnung bei drei oder mehr aufeinanderfolgenden
  Absätzen mit gleicher Satzanzahl. Praxisbeobachtung für maschinelle Prosa:
  Absätze aus drei bis fünf Sätzen zu je 18 bis 24 Wörtern. [plausibel]
- **Type-Token-Ratio**, gleitend über 500-Wort-Fenster. Niedrige lexikalische
  Vielfalt ist ein belegter Marker. [belegt für Englisch]
- **Wortartenverteilung**: Anteil Nomen und Adpositionen gegen Anteil Adjektive
  und Adverbien. [belegt für Englisch]
- **Absatz-Anfangsvarianz**: Wie viele Absätze beginnen mit demselben
  syntaktischen Muster (Subjekt-Prädikat, Adverbiale, Nebensatz)? [plausibel]
- **Aufzählungsdreier je 1.000 Wörter.** [plausibel]
- **Nullstelle Umgangssprache**: Anteil von Redensarten und Idiomen aus einer
  Referenzliste. Ein Wert von exakt null über 2.000 Wörter ist selbst ein
  Signal. Zu behandeln als Hinweis, nicht als Fehler – in einer Fachtextsorte ist
  ein niedriger Wert normal. [plausibel]

Der Prüfbericht dieser Schicht ist zugleich die Eingabe für den zweiten Durchgang
(siehe Abschnitt „Was wirkt", Punkt 4).

---

## Was wirkt und was Aberglaube ist

### 1. Wirkt: deterministische Nachbearbeitung auf Zeichenebene

Schicht 1. Hundert Prozent zuverlässig, kein Modell, keine Kosten, kein
Bedeutungsrisiko. Der einzige Punkt, an dem eine Ersetzung ohne Rückfrage
vertretbar ist.

### 2. Wirkt: Positivbeispiele im Kontext

Anthropic formuliert es für Systemprompts allgemein: diverse, kanonische
Beispiele statt erschöpfender Randfall-Listen; Beispiele kommunizieren
erwartetes Verhalten effizienter als Regeltext. In der Modell-Migrationsdoku
steht es schärfer, bezogen auf Verbositätssteuerung: Positivbeispiele, die das
gewünschte Maß zeigen, sind tendenziell wirksamer als Negativbeispiele oder
Anweisungen, die dem Modell sagen, was es nicht tun soll. Quelle:
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

Konsequenz: Jede Rollendefinition trägt zwei bis vier ausformulierte
Positivbeispiele in der Zielsprache. Das ist wirksamer als eine dreißigzeilige
Verbotsliste.

### 3. Wirkt eingeschränkt: Verbotslisten im Systemprompt

Sie funktionieren für einzelne, eindeutig identifizierbare Marker („verwende
niemals den Geviertstrich"), verlieren aber schnell an Wirkung, je länger die
Liste wird, und können gegenteilige Effekte haben.

Instruktiver dokumentierter Fall: Bei Claude Opus 5 **erhöht** eine Anweisung,
nicht zu denken oder nicht zu reasonieren, das Durchsickern von
`<thinking>`-Markierungen in die sichtbare Ausgabe, statt es zu unterdrücken.
Die generische Formulierung („keine internen oder System-XML-Tags in der
Antwort") ist messbar wirksamer als das explizite Benennen. Übertragen: „Vermeide
das Wort X" kann X salient machen.

Regel für dieses Setup: Verbotslisten kurz halten, generisch formulieren, und
die Detailprüfung dem Nachzählen überlassen statt der Anweisung.

### 4. Wirkt nur mit externem Signal: das Zwei-Pass-Verfahren

Der meistmissverstandene Punkt. Self-Refine (Madaan et al. 2023) schlug vor, dass
ein Modell seine eigene Ausgabe kritisiert und überarbeitet. Die
Nachfolgeforschung hat das erheblich relativiert: Intrinsische Selbstkorrektur
ohne externes Signal verbessert die Leistung oft nicht oder verschlechtert sie –
belegt für arithmetisches Reasoning, Closed-Book-QA, Codegenerierung,
Planerstellung und Graphfärbung. Quellen:
https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes
und https://arxiv.org/pdf/2404.04298

Die entscheidende Unterscheidung: **Stil ist keine Reasoning-Aufgabe.**
Intrinsische Selbstkorrektur scheitert beim Reasoning, weil das Modell sein
eigenes Feedback erfindet. Bei Stilregeln ist das Feedback extern und
deterministisch verfügbar – ein Regex-Lauf sagt objektiv, dass in Absatz 3 ein
Geviertstrich steht und dass fünf Sätze in Folge zwischen 19 und 23 Wörtern
liegen. Ein Zwei-Pass-Verfahren mit diesem Prüfbericht als Eingabe ist deshalb
keine intrinsische Selbstkorrektur, sondern werkzeuggestützte Korrektur, und die
funktioniert.

Umsetzung: Pass 1 schreibt. Die Prüfung zählt nach. Pass 2 bekommt konkrete
Fundstellen („Zeile 14: Geviertstrich; Absätze 2 bis 4: Satzlängenvarianz unter
Schwelle") und überarbeitet gezielt. **Ein zweiter Durchgang ohne diesen
Prüfbericht ist Aberglaube** – „schau nochmal drüber, ob es nach KI klingt"
erzeugt Betriebsamkeit und keine Verbesserung.

In diesem Setup liefert `werkzeuge/text-pruefen.py` genau diesen Prüfbericht.

### 5. Wirkt: Bewertermodell ungleich Erzeugermodell

Sprachmodelle bevorzugen selbst erzeugte Inhalte um 10 bis 25 Prozent.
Zusätzlich zu beachten: Positionsverzerrung mit bis zu 75 Prozent Präferenz für
die zuerst genannte Antwort, und Wortfülle-Verzerrung zugunsten längerer
Antworten unabhängig von der Qualität. Quellen:
https://arxiv.org/abs/2406.07791 und https://arxiv.org/html/2411.15594v6

Konsequenz für die eigene Arbeit: **Lass einen Text nicht von demselben Modell
bewerten, das ihn geschrieben hat, und nicht im selben Gespräch.** Wer einen
Entwurf prüfen lassen will, öffnet ein neues Gespräch, gibt nur den Text hinein
und nennt die Prüffrage – ohne zu erwähnen, wer ihn verfasst hat. Am
verlässlichsten ist ohnehin die Prüfung durch einen Menschen, der das Fach
kennt.

### 6. Tot: Temperatur-Schrauben

Bei den aktuellen Anthropic-Modellen sind `temperature`, `top_p` und `top_k`
entfernt; Anfragen, die sie setzen, werden mit HTTP 400 abgelehnt. Quelle:
https://platform.claude.com/docs/en/about-claude/models/migration-guide

Jede Anleitung im Netz, die „Temperatur hoch für menschlicheren Klang"
empfiehlt, ist auf aktuellen Modellen technisch nicht mehr umsetzbar.
Stilvarianz läuft über Prompting und Beispiele. Beim Anbieter Mistral existieren
die Parameter noch – das ist kein Argument für einen Anbieterwechsel, weil der
behauptete Effekt ohnehin nie belegt war.

### 7. Aberglaube: „Schreibe wie ein Mensch"

Es gibt keinen Beleg, dass generische Anweisungen dieser Art die messbaren Marker
senken. Sie verschieben den Text plausibel nur auf ein anderes Standardregister.
Ein analoger, gut dokumentierter Effekt: Bei Designaufgaben führen generische
Anweisungen („nicht cremefarben", „sauber und minimalistisch") dazu, dass das
Modell zu einer anderen festen Palette wechselt statt Varianz zu erzeugen.
Wirksam sind stattdessen konkrete Spezifikationen oder das Vorschlagen mehrerer
Richtungen zur Auswahl.

### 8. Unklar: Stilproben der Nutzerin oder des Nutzers

Eine EMNLP-Findings-Studie 2025 untersuchte über 400 reale Autorinnen und Autoren
und über 40.000 Generierungen je Modell, mit einem Ensemble aus
Autorschaftszuordnung, Autorschaftsverifikation, Stilabgleich und KI-Erkennung.
Befund: Sprachmodelle funktionieren gut bei strukturierten Formaten
(Nachrichten, E-Mail), scheitern aber bei nuanciertem, informellem Schreiben.
Quellen: https://arxiv.org/abs/2509.14543 ,
https://aclanthology.org/2025.findings-emnlp.532.pdf

Für eine Schularbeit ist die Lage günstiger, als die Studie nahelegt –
akademisches Deutsch ist ein strukturiertes Format. Aber es gibt keine Daten für
Deutsch. Die Zusage „schreibt in deinem Stil" ist damit nicht belegbar.
Textproben dürfen genutzt werden, aber als Annäherung, nicht als Imitation.

---

## Was über Erkennungswerkzeuge gesagt werden darf

Keine Aussage in beide Richtungen. Weder „das ist jetzt unerkennbar" noch eine
Entwarnung „0 Prozent KI laut Detektor". Beides ist aus derselben Faktenlage
angreifbar, weil die unabhängige Forschung Falsch-Positiv-Raten zwischen 4 und
über 60 Prozent misst. Belege in `ki-kennzeichnung.md`, Abschnitt 10.

Was gesagt werden darf: Der Text wurde gegen die Merkmale geprüft, die
sprachwissenschaftlich oder normativ als typisch für generierte Sprache belegt
sind – vom falschen Gedankenstrich bis zum gleichförmigen Satzrhythmus. Das ist
eine Aussage über die Prüfung, nicht über ein Detektorergebnis.

**Und der wichtigere Punkt:** Wer diese Prüfliste benutzt, um Spuren zu
verwischen, benutzt sie falsch. Der Kontrollmechanismus in Österreich ist nicht
der Detektor, sondern die Diskussion vor der Kommission und das Begleitprotokoll
(siehe `ki-kennzeichnung.md`). Die Liste ist dafür da, dass ein selbst
geschriebener Text nicht unnötig hölzern klingt und dass ein überarbeiteter
Entwurf wirklich überarbeitet ist – nicht dafür, eine fehlende Kennzeichnung zu
ersetzen.

---

## Anwendung beim Schreiben

Sinnvoll sind zwei Zeitpunkte, und einer davon ist nicht offensichtlich:

1. **Nach jedem fertigen Kapitel.** Erst Schicht 1 automatisch beheben, dann die
   Fundstellen aus Schicht 2 und 3 einzeln durchgehen.
2. **Nicht während des Schreibens.** Wer beim ersten Entwurf schon auf Marker
   achtet, schreibt langsamer und nicht besser. Der Prüflauf gehört in die
   Überarbeitung.

Die Kriterien der dritten Schicht sind binär, nicht skaliert. „Enthält dieser
Absatz einen Zusammenfassungssatz, der nichts Neues sagt? ja oder nein" ist
auswertbar. „Natürlichkeit 7 von 10" ist bedeutungslos, weil niemand weiß, was
eine Verschiebung auf 7,5 bedeuten würde.
