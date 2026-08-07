# ABA-Setup

**Ein Arbeits-Setup für Claude, mit dem man die abschließende Arbeit (ABA, früher
„vorwissenschaftliche Arbeit"/VWA) an einer österreichischen AHS schreibt – ohne
dabei die Regeln zu verletzen, die für genau diese Arbeit gelten.**

Es besteht aus drei Dingen:

- **Regelwerke** – was für die ABA tatsächlich gilt: Aufbau, Zitieren, Fristen,
  Beurteilungsraster, KI-Kennzeichnung. Belegt an Verordnung, SchUG und der
  offiziellen FAQ des Bildungsministeriums, mit Fundstelle an jeder Aussage.
- **Arbeitsschritte** – ein Fahrplan in sieben Etappen und je ein Skill dafür.
  Man tippt `thema` und arbeitet an der Fragestellung, `kritik` und bekommt eine
  Kapitelkritik mit Fundstellen.
- **Grenzen** – vier Regeln, die die KI nicht überschreitet. Keine erfundenen
  Quellen, kein fertiger Fließtext, jede Nutzung protokolliert, keine Note.

---

## Warum überhaupt

KI-Nutzung ist bei der abschließenden Arbeit erlaubt. Die offizielle FAQ des
Bildungsministeriums stellt ausdrücklich fest: „Ein generelles Verbot von
KI-Tools im Rahmen der abschließenden Arbeit ist nicht zulässig."

Erlaubt ist sie unter drei Bedingungen: **dokumentiert, kritisch reflektiert,
weiterverarbeitet.** Wer sie nicht offenlegt, riskiert die Wertung als
vorgetäuschte Leistung – das heißt keine Note, neues Thema, Wiederholung ohne
Betreuung.

Das Problem ist nicht das Werkzeug, sondern der Standardzustand. Ein Chatfenster
ohne Regeln erfindet Literaturangaben, schreibt Absätze, die niemand verteidigen
kann, und führt kein Protokoll. Dieses Setup ändert den Standardzustand.

Nebenbei zahlt es sich in der Beurteilung aus: Kriterium K1.2 bewertet den
„transparenten Einsatz technischer Hilfsmittel", Kriterium K3.4 verlangt, ihn in
der Diskussion mündlich zu begründen. Wer sauber dokumentiert, gewinnt dort,
statt zu verlieren.

---

## Einrichten

### Weg 1 – Claude Code (empfohlen, Terminal oder Desktop-App)

```bash
git clone https://github.com/DEIN-NAME/aba-setup.git
cd aba-setup
claude
```

Dann als erste Nachricht: **„Lass uns starten."**

Claude stellt drei Fragen, füllt `mein/profil.md` aus und sagt, was als Nächstes
dran ist. Kein Kopieren, kein Einrichten von Hand. Die Skills stehen sofort zur
Verfügung.

Kein Git installiert? Auf der GitHub-Seite oben rechts auf **Code → Download ZIP**,
entpacken, den Ordner in Claude Code öffnen.

### Weg 2 – Claude-App (claude.ai, ohne Terminal)

Siehe **[fuer-die-claude-app/ANLEITUNG.md](fuer-die-claude-app/ANLEITUNG.md)**.
Kurzfassung: ein Projekt anlegen, einen Text in die Projektanweisungen einfügen,
die Regelwerke ins Projektwissen hochladen. Dauert ein paar Minuten und
funktioniert danach genauso.

### Weg 3 – ein anderer KI-Dienst

Die Regelwerke sind gewöhnliche Textdateien. Sie funktionieren überall dort, wo
man Dateien hochladen oder Text einfügen kann. Was sie sagen, gilt unabhängig
davon, welches Modell sie liest.

---

## Was drin ist

```
CLAUDE.md          Die Betriebsanweisung für die KI – die vier harten Regeln
FAHRPLAN.md        Sieben Etappen von der Idee bis zur Diskussion
START-HIER.md      Einstieg für alle, die noch nie mit Claude gearbeitet haben

regeln/            13 Regelwerke, jedes mit Fundstellen
mein/              Deine Dateien: Profil, Begleitprotokoll, Quellen, Arbeitsstand
werkzeuge/         text-pruefen.py – zählt nach, was nachzählbar ist
.claude/skills/    Die Arbeitsschritte
fuer-die-claude-app/   Einrichtung ohne Terminal
```

Alles, was du selbst schreibst, liegt in `mein/`. Der Rest ändert sich nicht.

---

## Die vier Regeln

**1. Keine erfundenen Quellen.** Kein Titel, kein Jahr, keine Seitenzahl ohne
Deckung. In einer Untersuchung von 636 modellerzeugten Literaturangaben waren je
nach Modell 18 bis 55 Prozent vollständig erfunden, und von den existierenden
enthielten 24 bis 43 Prozent falsche Angaben. Die KI sagt hier „das habe ich
nicht", statt etwas Plausibles zu liefern.

**2. Kein fertiger Fließtext.** Du bekommst Rückmeldung zu dem, was du
geschrieben hast – keine Kapitel. Der Grund ist keine Prinzipienreiterei: Sieben
der dreizehn Beurteilungskriterien werden mündlich geprüft. Ein Absatz, den du
nicht selbst gedacht hast, kostet dich vor der Kommission mehr, als er dir beim
Schreiben erspart hat.

**3. Jede Nutzung wird protokolliert.** Nach jeder Sitzung ein Eintrag im
Begleitprotokoll – ungefragt. Das ist gesetzlich verlangt (§ 9 Abs. 2
Prüfungsordnung AHS), es ist ein Beurteilungskriterium, und es lässt sich
rückwirkend nicht rekonstruieren.

**4. Keine Note.** Keine Prognose, keine Prozentzahl, keine Niveaustufe. Nur:
Was ist belegt, was fehlt, an welcher Stelle.

---

## Was das nicht ist

- **Keine Rechtsauskunft.** Ein Arbeitsstand mit Fundstellen. Die offizielle FAQ
  wird ohne Ankündigung geändert und trägt kein Versionsdatum. Bei allem, was
  zählt, gilt die Auskunft deiner Schule.
- **Kein Ghostwriter.** Wer eine fertige Arbeit sucht, ist hier falsch – und
  zwar auch praktisch: Was hier entsteht, ist Rückmeldung, keine Kapitel.
- **Kein KI-Detektor und keine Tarnung.** Über Detektoren wird hier in keine
  Richtung eine Aussage gemacht. Die Forschung misst Falsch-Positiv-Raten
  zwischen 4 und über 60 Prozent; kontrolliert wird in Österreich ohnehin anders,
  nämlich über Begleitprotokoll und Diskussion.
- **Nicht für Deutschland oder die Schweiz.** Die österreichische Regelungsdichte
  – eine Verordnungsnorm plus eine sehr detaillierte amtliche FAQ – ist im
  Vergleich die Ausnahme und lässt sich nicht übertragen. Die Regelwerke zum
  Schreiben, Zitieren und zur Sprache gelten überall; die zum Verfahren nicht.

## Für welche Variante

Ausgearbeitet ist **Variante A: die schriftliche Arbeit mit forschendem Zugang.**

**Variante B** (gestalterisches oder künstlerisches Vorhaben mit Dokumentation)
ist nicht ausgeschlossen, aber nur teilweise abgedeckt. Was vollständig gilt:
Quellen und Zitieren, Schreibweise, Schreibhandwerk, Sprachprüfung,
KI-Kennzeichnung, Begleitprotokoll, Fristen, Präsentation und Diskussion – also
der weitaus größte Teil, denn die Dokumentation des Entstehungsprozesses ist ein
wissenschaftlicher Text und wird als solcher gelesen. Was fehlt: der
Beurteilungsraster für K1, der bei B vollständig anders aussieht.

⚠️ **Der Punkt, der überrascht:** Auch eine *forschende* Arbeit fällt unter
Variante B, sobald sie in einem gestalterischen Format umgesetzt wird – ein
Video-Podcast über ein Forschungsthema wird nach B beurteilt. Das Onboarding
fragt danach und sagt dir, was dann zu tun ist.

---

## Stand und Pflege

Die Regelwerke tragen im Kopf ein `stand`-Feld. Sie wurden im August 2026 an den
Primärquellen geprüft: Prüfungsordnung AHS (BGBl. II Nr. 174/2012 i.d.g.F.),
SchUG, https://www.ahs-aba.at samt FAQ, amtlicher Beurteilungsraster.

**Prüf die Fristen und Formvorgaben immer selbst nach.** Termine setzt das
Bundesland oder die Schule, nicht die Verordnung.

Fehler gefunden oder etwas veraltet? Issue oder Pull Request – besonders
willkommen sind Belege aus Primärquellen und Erfahrungen aus anderen
Bundesländern.

---

## Lizenz

CC BY-SA 4.0 für die Texte, MIT für das Skript in `werkzeuge/`. Siehe
[LICENSE](LICENSE). Nutzen, ändern, weitergeben ist ausdrücklich erwünscht –
auch für die eigene Schule.
