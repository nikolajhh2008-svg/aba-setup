---
name: uebergabe
description: Den Stand einer Sitzung so festhalten, dass die nächste Sitzung – oder eine andere KI – ohne Vorwissen weitermachen kann, und beim Start die letzte Übergabe aufnehmen. Nutzen am Ende jeder Arbeitssitzung, bei „ich muss aufhören“, „für heute Schluss“, „wo waren wir“, „weiter von letztem Mal“, vor einem Wechsel zu einer anderen App, und bevor der Gesprächsverlauf zu lang wird.
license: MIT
---

Übertragen aus `blader/baton` (blader, MIT-Lizenz, siehe `LICENSE.txt`), ins Deutsche
und auf die ABA angepasst. Änderungen: Ablageort `mein/uebergaben/` statt `.baton/`,
Abgleich mit den Dateien in `mein/` statt mit Git, Abschnittsnamen für eine
Schülerarbeit statt für Code; zusätzlich die mit **ABA** markierten Absätze.

# Übergabe

## Überblick

Eine Staffel funktioniert nur, wenn der Stab sauber übergeben wird. Wer die Arbeit
übernimmt – eine neue Sitzung, ein anderes Fenster, eine andere App –, beginnt mit
**null Kontext**. Eine Übergabe ist eine einzige Markdown-Datei, mit der die nächste
Sitzung sofort weiterarbeiten kann, statt alles neu herzuleiten.

**Grundsatz:** Festhalten, was die nächste Sitzung aus den Dateien nicht
rekonstruieren kann – die *Absicht*, die *schon verworfenen Wege* und den *genauen
nächsten Schritt* –, gestützt auf den tatsächlichen Stand der Dateien, nicht auf die
Erzählung im Chat.

Zwei Seiten: **Übergabe schreiben** (du hörst auf) und **Übergabe aufnehmen** (du
fängst an).

## Wann

**Übergabe schreiben, wenn:**
- eine Sitzung mit unfertiger Arbeit endet („ich muss aufhören“, „für heute
  Schluss“),
- die Person zu einer anderen App wechselt (z. B. von der Claude-App zu Cowork),
- der Gesprächsverlauf lang wird und bald zusammengefasst werden könnte.

**Übergabe aufnehmen, wenn:**
- eine Sitzung beginnt – immer zuerst nachsehen, ob eine liegt.

**Nicht verwenden für:** eine abgeschlossene Aufgabe ohne Fortsetzung, oder dauerhafte
Entscheidungen – die gehören in `mein/profil.md` und `mein/schulvorgaben.md`.

**ABA – getrennt vom Begleitprotokoll:** Die Übergabe ist ein Arbeitszettel für die
nächste Sitzung. Das Begleitprotokoll (Skill `protokoll`) ist der amtliche Nachweis.
Beides am Sitzungsende, aber nie das eine statt des anderen.

## Wo die Übergabe liegt

Ablageort: **`mein/uebergaben/`** – anlegen, wenn es den Ordner noch nicht gibt.

Dateiname: **`<JJJJ-MM-TT>-<kurzes-stichwort>.md`**
(z. B. `mein/uebergaben/2026-11-12-kapitel-2-forschungsstand.md`).

Die nächste Sitzung findet die neueste über das Datum im Dateinamen.

**In der App ohne Dateizugriff:** Gib die Übergabe als Text aus, mit dem Hinweis, sie
als Datei in den eigenen ABA-Ordner zu legen und in der nächsten Sitzung
hochzuladen.

## Die eiserne Regel: erst prüfen, dann schreiben

Eine Übergabe aus der Chat-Erzählung statt aus dem echten Stand ist schlimmer als
keine – sie schickt die nächste Sitzung mit falscher Sicherheit in die falsche
Richtung. Vor dem Schreiben lies `mein/arbeitsstand.md`, sieh nach, welche Dateien in
`mein/arbeit/` und `mein/recherche/` tatsächlich existieren und was darin steht. Der
Abschnitt „Stand“ muss den tatsächlichen Dateistand wiedergeben. Widerspricht der
Stand der Erzählung, **dokumentiert die Übergabe den Stand** und benennt die Lücke.

## Aufbau

Jeden Abschnitt ausfüllen. Ist einer wirklich leer, „nichts“ schreiben – nicht
löschen (die nächste Sitzung verlässt sich auf die gleiche Form).

```markdown
# Übergabe: <einzeiliger Titel der Arbeit>

**Kurz:** <1–3 Sätze: worum es geht, wo es steht, der eine nächste Schritt.>

## Absicht und Ziel
Wozu diese Arbeit dient und wie das Ergebnis aussehen soll. Mit einem
Abnahmekriterium – z. B. „Kapitel 2 beantwortet Leitfrage 1 und jede Aussage hat
einen Beleg mit Seitenzahl“.

## Stand (geprüft an den Dateien)
- Dateien, die es gibt: <Pfade, aus dem Ordner gelesen>
- Fertig: <was steht und von der Person bestätigt ist>
- Halbfertig: <was begonnen ist, mit Datei und Stelle>
- Geprüft: <was tatsächlich gegengeprüft wurde, z. B. Quellen mit
  literaturverzeichnispruefung>
- Angenommen, nicht geprüft: <was du glaubst, aber nicht belegt hast>

## Erkenntnisse und Stolpersteine
Der wertvollste Abschnitt – was die nächste Sitzung nicht aus den Dateien erfährt:
- nicht offensichtliche Erkenntnisse
- **schon verworfene Wege** (damit sie nicht wiederholt werden) und *warum*
- **nicht anfassen** – Stellen, die so bleiben sollen, und der Grund

## Verweise
- wichtige Stellen: `mein/arbeit/kapitel-2.md`, Abschnitt 2.3 – was dort ist
- Quellen, Recherchenotizen in `mein/recherche/`, frühere Übergaben
- Vorgaben der Betreuungsperson, die heute eine Rolle gespielt haben

## Nächste Schritte
Geordnet, konkret, der unmittelbar nächste Schritt zuerst. Nicht „am Kapitel
weiterarbeiten“ – sondern der wörtliche nächste Handgriff.

## Offene Fragen
Offene Entscheidungen und die derzeitige Tendenz (damit es weitergehen kann, auch
wenn niemand antwortet). **ABA:** Fragen, die nur die Betreuungsperson beantworten
kann, zusätzlich in `mein/profil.md` unter „Offene Fragen an die Betreuungsperson“.
```

## Übergabe aufnehmen (weitermachen)

1. **Finden:** die neueste Datei in `mein/uebergaben/` lesen.
2. **Vertrauen, aber prüfen:** „Stand“ gegen die echten Dateien abgleichen, bevor du
   handelst – die Person kann inzwischen in Word weitergearbeitet haben.
3. **Weitermachen** bei „Nächste Schritte“.
4. **Erledigte Übergaben aufräumen:** Wenn die Arbeit daraus erledigt ist, die
   dauerhaften Erkenntnisse nach `mein/arbeitsstand.md` übernehmen und die Übergabe
   löschen. Alte Übergaben nicht in `mein/uebergaben/` anhäufen lassen.

## Häufige Fehler

- **Die Übergabe wiederholt nur, was in den Dateien steht.** Die Dateien gibt es
  schon. Festhalten: Absicht, verworfene Wege, nächster Schritt.
- **Aus dem Chat gebaut, nicht aus den Dateien.** Erst prüfen – eine selbstsicher
  falsche Übergabe ist schlimmer als keine.
- **Vager nächster Schritt** („weitermachen“). Den wörtlichen nächsten Handgriff
  schreiben.
- **Verworfene Wege fehlen.** Zu benennen, was *nicht* funktioniert hat, ist der
  wertvollste Inhalt – es erspart eine komplette Neuherleitung.
- **Verstreute Ablage.** Immer `mein/uebergaben/` – nie woanders, sonst findet die
  nächste Sitzung sie nicht.
- **Alte Übergaben häufen sich.** Aufräumen, wenn die Arbeit erledigt ist.

## Antwort

Nach dem Schreiben den genauen Pfad der Datei nennen und in einer Zeile sagen, was
drinsteht.
