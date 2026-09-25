<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/assets/banner-dark.svg">
  <img alt="ABA-Setup: Ein Blatt füllt sich Zeile für Zeile, eine Feder schreibt mit, daneben haken sich die vier Regeln ab – keine erfundenen Quellen, schreibt mit dir, Protokoll läuft mit, sauber gekennzeichnet." src=".github/assets/banner-light.svg" width="100%">
</picture>

<div align="center">

**Schreib deine abschließende Arbeit mit Claude oder ChatGPT.**<br/>
Schritt für Schritt, belegt und offengelegt.

[![Texte: CC BY-SA 4.0](https://img.shields.io/badge/Texte-CC%20BY--SA%204.0-3F6E4E.svg)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/Code-MIT-8A6D3B.svg)](LICENSE)
[![Für: AHS Österreich](https://img.shields.io/badge/F%C3%BCr-AHS%20%C3%96sterreich-B5452F.svg)](https://www.ahs-aba.at)
[![Läuft mit: Claude · ChatGPT](https://img.shields.io/badge/L%C3%A4uft%20mit-Claude%20%C2%B7%20ChatGPT-D97706.svg)](fuer-die-app/ANLEITUNG.md)
[![Stand: September 2026](https://img.shields.io/badge/Stand-September%202026-555555.svg)](#stand-und-pflege)

[Starten](#starten) · [Die vier Regeln](#die-vier-regeln) · [Was drin ist](#was-drin-ist) · [Fahrplan](FAHRPLAN.md) · [Erste Schritte](START-HIER.md)

</div>

Die abschließende Arbeit (ABA, früher VWA) darf mit KI geschrieben werden – das
Bildungsministerium stellt ausdrücklich fest: „Ein generelles Verbot von
KI-Tools im Rahmen der abschließenden Arbeit ist nicht zulässig.“ Erlaubt ist sie
unter drei Bedingungen: **dokumentiert, kritisch reflektiert, weiterverarbeitet.**

Ein nacktes Chatfenster erfüllt keine davon. Es erfindet Literaturangaben,
schreibt Absätze, die niemand verteidigen kann, und führt kein Protokoll. Dieses
Setup ändert den Standardzustand: **sechzehn Regelwerke mit Fundstellen, zwölf
Arbeitsschritte und vier Regeln** – damit die KI mit dir schreibt, ohne Quellen zu
erfinden, und alles so festhält, wie es die Prüfungsordnung verlangt.

Du gibst Claude oder ChatGPT den Ordner, bekommst drei kurze Fragen – und dann
arbeitet ihr an deiner Arbeit.

---

## Starten

Lade den Ordner herunter (**Code → Download ZIP**, entpacken) – das ist ab jetzt
dein ABA-Ordner. Du schreibst in Word, die KI arbeitet daneben mit deinem Ordner.

**Empfohlen: Claude Cowork.** Claude in der Desktop-App mit Zugriff auf deinen
Ordner: liest deine Word-Dateien, legt neue an und speichert Stand, Quellen,
Recherche und Protokoll direkt bei dir. Einmal die Skills aus
`fuer-die-app/skills/` in dein Claude-Konto hochladen, den Ordner freigeben, dann:

> Lies CLAUDE.md und lass uns starten.

**Oder ChatGPT Work** (ChatGPT-Desktop-App mit Ordnerzugriff), **oder im Browser**
als Notbehelf. Alle Wege Schritt für Schritt:
**[fuer-die-app/ANLEITUNG.md](fuer-die-app/ANLEITUNG.md)**.

**Mit Claude Code** (Terminal):

```bash
git clone https://github.com/nikolajhh2008-svg/aba-setup.git
cd aba-setup
claude
```

Du bekommst zuerst eine Übersicht über alles, was schon in deinem Ordner liegt,
dann drei kurze Fragen – und dann arbeitet ihr an deiner Arbeit. Nichts bleibt nur
im Chat: Am Ende jeder Sitzung liegen Protokolleintrag und Übergabe für das nächste
Mal in deinem Ordner.

---

## Die vier Regeln

**1. Keine erfundenen Quellen.** Kein Titel, kein Jahr, keine Seitenzahl ohne
Deckung. In einer Untersuchung von 636 modellerzeugten Literaturangaben waren je
nach Modell 18 bis 55 Prozent vollständig erfunden
([Walters & Wilder 2023](https://www.nature.com/articles/s41598-023-41032-5)).
Hier gibt es stattdessen Kataloge, Suchbegriffe – und im Entwurf eine markierte
Lücke, bis die Quelle da ist.

**2. Geschrieben wird mit dir, Absatz für Absatz.** Erst Leitfrage, Quellen mit
Seitenzahl und deine Aussage in einem Satz, dann der Plan des Kapitels, dann ein
Absatz nach dem anderen – jeweils mit einer Rückfrage an dich. Sieben der
dreizehn Beurteilungskriterien werden mündlich geprüft; einen Absatz, den du
mitgebaut hast, kannst du verteidigen.

**3. Guter Text statt generischer.** Der Maßstab sind echte Absätze aus
begutachteten Fachartikeln, je einer für Einleitung, Forschungsstand, Methode,
Ergebnisse, Grenzen und Schluss. Jeder Entwurf wird vor dem Zeigen außerdem
gegen eine Prüfliste gehalten: keine Floskeln, keine Verstärkerwörter, keine
Dreierketten, kein „—“, kein Schlusssatz, der nur wiederholt. Konkret,
wissenschaftlich, österreichisches Standarddeutsch.

**4. Alles wird offengelegt.** Jede Stelle aus einem Entwurf landet in
`mein/ki-stellen.md`, jede Sitzung im Begleitprotokoll. Vor der Abgabe wird
daraus die Kennzeichnung, die die amtliche FAQ verlangt. Genau das macht die
Nutzung erlaubt – verschwiegene KI-Hilfe gilt als vorgetäuschte Leistung.

---

## Was drin ist

```
CLAUDE.md               Die Betriebsanweisung – liest Claude bei jedem Start
FAHRPLAN.md             Sieben Etappen von der Idee bis zur Diskussion
START-HIER.md           Für alle, die noch nie mit Claude gearbeitet haben

regeln/                 16 Regelwerke mit Fundstellen, dazu ein Register
mein/                   Deine Dateien: Profil, Protokoll, Quellen, Recherche,
                        Übergaben, deine Word-Dateien in arbeit/
werkzeuge/              text-pruefen.py zählt nach, was nachzählbar ist;
                        buendeln.py und paket-pruefen.py halten das Setup stimmig
.claude/skills/         Die zwölf Arbeitsschritte
fuer-die-app/           Einrichtung für Cowork, ChatGPT und Browser, Skill-ZIPs
```

**Die Regelwerke** decken ab, was bei der ABA tatsächlich zählt: Thema und
Leitfragen · Aufbau · Methodik · Fristen und Abgabe · Recherchewege und seriöse
Quellen · Quellen und Zitieren · Zitierstile · Plagiat und Eigenleistung ·
wissenschaftliche Schreibweise · Schreibhandwerk · Stilvorbilder aus echten
Fachartikeln · Sprachprüfung ·
KI-Kennzeichnung · Begleitprotokoll · Beurteilung · Präsentation und Diskussion.
Belegt an Prüfungsordnung, SchUG, der amtlichen FAQ und dem Beurteilungsraster.

**Die Arbeitsschritte** stammen, wo es sie schon gab, aus gepflegten
Open-Source-Projekten und sind ins Deutsche übertragen und auf die ABA angepasst –
Herkunft und Lizenz stehen in jedem Skill. Normale Sätze funktionieren genauso,
aber diese Wörter treffen direkt:

- `start` – Übersicht über alles im Ordner, dann Onboarding in drei Fragen
- `thema` – Forschungslücke, Forschungsfrage, Leitfragen, Portaltext
  *(nach lishix520/academic-paper-skills)*
- `quellen` – eine Quelle prüfen und aufnehmen
- `literaturverzeichnispruefung` – jede Angabe live gegen OpenAlex, K10plus, DNB,
  Crossref prüfen *(benedikt-e/literaturverzeichnispruefung)*
- `gliederung` – Kapitel aus Sicht des Beurteilungsrasters prüfen
  *(nach lishix520/academic-paper-skills)*
- `schreiben` – ein Kapitel gemeinsam schreiben, Abschnitt für Abschnitt
  *(nach Anthropics doc-coauthoring)*
- `humanizer-de` – jeden Entwurf auf generische Sprache prüfen, Modus Formal
  *(marmbiz/humanizer-de)*
- `kritik` – ein Kapitel mit Fundstellen prüfen *(nach bladewing/thesis-check)*
- `protokoll` – Eintrag fürs Begleitprotokoll
- `uebergabe` – Stand für die nächste Sitzung festhalten *(nach blader/baton)*
- `abgabe` – Endkontrolle vor dem Hochladen *(nach bladewing/thesis-check)*
- `pruefung` – Diskussion vor der Kommission üben
  *(nach Jellypod-Inc/school-skills, socratic-tutor)*

Alles, was du selbst schreibst, liegt in `mein/`. Der Rest ändert sich nicht.

---

## Was das nicht ist

- **Keine Rechtsauskunft.** Ein Arbeitsstand mit Fundstellen. Die offizielle FAQ
  wird ohne Ankündigung geändert und trägt kein Versionsdatum. Bei allem, was
  zählt, gilt die Auskunft deiner Schule.
- **Kein Knopf für eine fertige Arbeit.** Es entsteht Absatz für Absatz, aus
  deinem Material und mit deinen Entscheidungen – weil du die Arbeit am Ende
  vor einer Kommission vertrittst.
- **Kein KI-Detektor und kein Versteckspiel.** Über Detektoren wird hier in keine
  Richtung eine Aussage gemacht. Die Forschung misst Falsch-Positiv-Raten
  zwischen 4 und über 60 Prozent; kontrolliert wird in Österreich ohnehin anders,
  nämlich über Begleitprotokoll und Diskussion.
- **Nicht für Deutschland oder die Schweiz.** Die österreichische Regelungsdichte
  – eine Verordnungsnorm plus eine sehr detaillierte amtliche FAQ – ist im
  Vergleich die Ausnahme und lässt sich nicht übertragen. Die Regelwerke zum
  Schreiben, Zitieren und zur Sprache gelten überall; die zum Verfahren nicht.

## Für welche Variante

Ausgearbeitet ist **Variante A: die schriftliche Arbeit mit forschendem Zugang.**
Für **Variante B** (gestalterisches oder künstlerisches Vorhaben mit
Dokumentation) gilt fast alles ebenso – Quellen, Zitieren, Sprache,
KI-Kennzeichnung, Begleitprotokoll, Fristen, Präsentation. Anders ist der
Beurteilungsraster in K1.

⚠️ Auch eine *forschende* Arbeit fällt unter Variante B, sobald sie in einem
gestalterischen Format abgegeben wird – ein Video-Podcast über ein
Forschungsthema etwa. Das Onboarding fragt danach.

---

## Stand und Pflege

Jedes Regelwerk trägt im Kopf ein `stand`-Feld. Geprüft an den Primärquellen:
Prüfungsordnung AHS (BGBl. II Nr. 174/2012 i.d.g.F.), SchUG,
[ahs-aba.at](https://www.ahs-aba.at) samt FAQ, amtlicher Beurteilungsraster.

**Termine und Formvorgaben setzen Bundesland, Schule und Betreuungsperson** – sie
schlagen jede Regel hier. Prüf sie immer selbst nach.

Fehler gefunden oder etwas veraltet? [Issue öffnen](../../issues/new/choose) –
am liebsten mit Link zur Primärquelle. Wie Beiträge aussehen:
[CONTRIBUTING.md](CONTRIBUTING.md).

---

## Lizenz

Texte unter [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.de),
das Skript in `werkzeuge/` unter MIT – siehe [LICENSE](LICENSE). Nutzen, ändern,
weitergeben ist ausdrücklich erwünscht, auch für die eigene Schule.
