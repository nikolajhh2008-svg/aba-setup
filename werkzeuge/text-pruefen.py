#!/usr/bin/env python3
"""
Prüft einen deutschen Text auf Zeichenfehler, generische Wendungen und
gleichförmigen Satzrhythmus.

Aufruf:
    python3 werkzeuge/text-pruefen.py mein/arbeit/kapitel-3.md
    python3 werkzeuge/text-pruefen.py meine-arbeit.docx

Liest .md, .txt und .docx. Braucht nichts installiert – nur Python 3.

Was dieses Werkzeug NICHT ist: ein KI-Detektor. Es zählt nach, was nachzählbar
ist. Die Belege zu jeder Regel stehen in regeln/sprache-pruefen.md, jeweils mit
der Angabe, wie gut sie belegt ist. Ein Treffer ist ein Hinweis auf eine Stelle,
die man ansehen sollte, kein Fehler.
"""

import re
import sys
import zipfile
from pathlib import Path

# ---------------------------------------------------------------- Schicht 1

ZEICHENREGELN = [
    (
        "—",
        "Geviertstrich",
        "Im Deutschen steht der Halbgeviertstrich mit Leerzeichen: Wort – Wort",
    ),
    (
        r'(?<!\w)"(?=\w)|(?<=\w)"(?!\w)',
        "Gerades Anführungszeichen",
        "Typografisch richtig sind „…“",
    ),
    (
        r"\.\.\.",
        "Drei einzelne Punkte",
        "Auslassungspunkte sind ein eigenes Zeichen: …",
    ),
    (
        r"[^\n ] {2,}[^\n ]",
        "Doppeltes Leerzeichen",
        "Ein Leerzeichen genügt",
    ),
    (
        r"\s+[,.;:!?]",
        "Leerzeichen vor Satzzeichen",
        "Satzzeichen schließen direkt an das Wort an",
    ),
    (
        r"\b(?:19|20)\d{2}-(?:19|20)\d{2}\b",
        "Bindestrich in Jahresspanne",
        "Zeitspannen brauchen den Streckenstrich ohne Leerzeichen: 2010–2024",
    ),
    (
        r"\bz\.B\.",
        "Fehlendes Leerzeichen in z. B.",
        "Richtig ist z. B. mit schmalem Leerzeichen",
    ),
    (
        r"\bS\.\d",
        "Fehlendes Leerzeichen bei Seitenangabe",
        "Richtig ist S. 14",
    ),
    (
        r"\bd\.h\.",
        "Fehlendes Leerzeichen in d. h.",
        "Richtig ist d. h.",
    ),
]

# ---------------------------------------------------------------- Schicht 2

MARKERWOERTER = {
    "essenziell": "notwendig wofür genau?",
    "essentiell": "notwendig wofür genau?",
    "vielfältig": "die Vielfalt aufzählen",
    "nahtlos": "streichen, im Fachtext Werbesprache",
    "maßgeschneidert": "angeben, was angepasst wurde",
    "ganzheitlich": "benennen, welche Aspekte einbezogen sind",
    "umfassend": "durch den Umfang ersetzen",
    "revolutionär": "Urteil ohne Maßstab",
    "bahnbrechend": "Urteil ohne Maßstab",
    "wegweisend": "Urteil ohne Maßstab",
    "beleuchten": "untersuchen, darstellen",
    "eintauchen": "untersuchen, auswerten",
    "unerlässlich": "sagen, wofür",
    "facettenreich": "die Facetten nennen",
}

FLOSKELN = {
    r"[Ee]s ist wichtig zu (beachten|betonen|erwähnen)": "die Aussage direkt machen",
    r"[Ee]s ist entscheidend (hervorzuheben|zu betonen)": "die Aussage direkt machen",
    r"[Ii]n der heutigen (Zeit|Gesellschaft|Welt)": "streichen oder datieren",
    r"spielt eine (entscheidende|wichtige|zentrale) Rolle": "das gemeinte Verb einsetzen",
    r"[Zz]usammenfassend lässt sich (sagen|festhalten)": "im Fazit überflüssig",
    r"[Ii]nsgesamt lässt sich festhalten": "nur behalten, wenn Neues folgt",
    r"[Aa]n dieser Stelle sei erwähnt": "erwähnen, ohne es anzukündigen",
    r"[Dd]es Weiteren": "Übergang, der die Beziehung benennt",
    r"[Dd]arüber hinaus": "Übergang, der die Beziehung benennt",
    r"[Nn]icht zuletzt": "Übergang, der die Beziehung benennt",
    r"[Vv]on (großer|entscheidender) Bedeutung": "sagen, wofür",
    r"nicht nur .{3,60}?, sondern auch": "zwei Sätze, ohne Aufwertungsrahmen",
}

BEHAUPTUNGS_FUELLWOERTER = [
    "natürlich",
    "bekanntlich",
    "selbstverständlich",
    "offensichtlich",
    "zweifellos",
    "unbestritten",
]

BELEGBEHAUPTUNGEN = [
    r"[Dd]ie Forschung (geht davon aus|zeigt|nimmt an)",
    r"[Ee]s wird (allgemein )?angenommen",
    r"[Ss]tudien (zeigen|belegen|weisen darauf hin)",
    r"[Ee]xperten (sind sich einig|gehen davon aus)",
    r"[Ww]issenschaftler(innen)? (haben|sind)",
    r"[Ee]s ist (allgemein )?bekannt",
]

SCHLUSSFLOSKELN = ("Zusammenfassend", "Insgesamt", "Somit", "Damit", "Folglich")


# ---------------------------------------------------------------- Einlesen


def text_aus_docx(pfad: Path) -> str:
    """Liest den Fließtext einer .docx ohne Fremdbibliothek."""
    with zipfile.ZipFile(pfad) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    xml = re.sub(r"</w:p>", "\n\n", xml)
    xml = re.sub(r"<w:br[^>]*/>", "\n", xml)
    text = re.sub(r"<[^>]+>", "", xml)
    ersetzungen = {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"', "&apos;": "'"}
    for such, ersatz in ersetzungen.items():
        text = text.replace(such, ersatz)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def text_einlesen(pfad: Path) -> str:
    if pfad.suffix.lower() == ".docx":
        return text_aus_docx(pfad)
    return pfad.read_text(encoding="utf-8")


def saetze(absatz: str) -> list:
    roh = re.split(r"(?<=[.!?])\s+", absatz.strip())
    return [s for s in roh if len(s.split()) > 2]


def absaetze(text: str) -> list:
    return [a.strip() for a in re.split(r"\n\s*\n", text) if a.strip()]


def zeile_von(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def ausschnitt(text: str, position: int, laenge: int = 60) -> str:
    start = max(0, position - 25)
    stueck = text[start : position + laenge].replace("\n", " ")
    return re.sub(r"\s+", " ", stueck).strip()


# ---------------------------------------------------------------- Prüfungen


def pruefe_zeichen(text: str) -> list:
    funde = []
    for muster, name, hinweis in ZEICHENREGELN:
        for treffer in re.finditer(muster, text):
            funde.append((zeile_von(text, treffer.start()), name, hinweis,
                          ausschnitt(text, treffer.start())))
    return funde


def pruefe_wortlisten(text: str) -> list:
    funde = []
    for wort, hinweis in MARKERWOERTER.items():
        for treffer in re.finditer(rf"(?<![\w]){wort}", text, re.IGNORECASE):
            funde.append((zeile_von(text, treffer.start()), f"Markerwort „{wort}“",
                          hinweis, ausschnitt(text, treffer.start())))
    for muster, hinweis in FLOSKELN.items():
        for treffer in re.finditer(muster, text):
            funde.append((zeile_von(text, treffer.start()), "Floskel", hinweis,
                          ausschnitt(text, treffer.start())))
    for wort in BEHAUPTUNGS_FUELLWOERTER:
        for treffer in re.finditer(rf"(?<![\w]){wort}(?![\w])", text, re.IGNORECASE):
            funde.append((zeile_von(text, treffer.start()), f"Füllwort „{wort}“",
                          "ersetzt einen Beleg durch eine Behauptung",
                          ausschnitt(text, treffer.start())))
    for muster in BELEGBEHAUPTUNGEN:
        for treffer in re.finditer(muster, text):
            funde.append((zeile_von(text, treffer.start()), "Belegbehauptung ohne Quelle",
                          "wer genau? Quelle nennen oder Satz streichen",
                          ausschnitt(text, treffer.start())))
    return funde


def pruefe_rhythmus(text: str) -> list:
    funde = []
    liste = absaetze(text)
    vorherige_satzzahl = None
    gleiche_in_folge = 1

    for nummer, absatz in enumerate(liste, start=1):
        s = saetze(absatz)
        if len(s) < 3:
            vorherige_satzzahl = len(s)
            continue

        laengen = [len(satz.split()) for satz in s]
        mittel = sum(laengen) / len(laengen)
        abweichung = (sum((x - mittel) ** 2 for x in laengen) / len(laengen)) ** 0.5

        if abweichung < 4:
            funde.append((nummer, "Gleichförmiger Satzrhythmus",
                          f"{len(s)} Sätze, Streuung {abweichung:.1f} Wörter "
                          f"(Schwelle 4) – ein kurzer Satz dazwischen trägt Gewicht",
                          laengen))

        letzter = s[-1].lstrip("„\"'")
        if letzter.startswith(SCHLUSSFLOSKELN):
            funde.append((nummer, "Zusammenfassender Schlusssatz",
                          "prüfen, ob er etwas Neues sagt – sonst streichen",
                          letzter[:70]))

        if len(s) == vorherige_satzzahl:
            gleiche_in_folge += 1
            if gleiche_in_folge == 3:
                funde.append((nummer, "Gleiche Absatzlänge in Folge",
                              f"drei Absätze mit je {len(s)} Sätzen", ""))
                gleiche_in_folge = 1
        else:
            gleiche_in_folge = 1
        vorherige_satzzahl = len(s)

    return funde


def kennzahlen(text: str) -> dict:
    woerter = re.findall(r"\b[\wäöüßÄÖÜ]+\b", text.lower())
    alle_saetze = [s for a in absaetze(text) for s in saetze(a)]
    return {
        "Wörter": len(woerter),
        "Zeichen": len(text),
        "Absätze": len(absaetze(text)),
        "Sätze": len(alle_saetze),
        "Wörter je Satz im Mittel": round(len(woerter) / max(1, len(alle_saetze)), 1),
        "Anteil verschiedener Wörter": f"{len(set(woerter)) / max(1, len(woerter)):.2f}",
    }


# ---------------------------------------------------------------- Ausgabe


def block(titel: str, funde: list, mit_zeile: str = "Zeile") -> None:
    print(f"\n{titel}  ({len(funde)})")
    print("-" * 70)
    if not funde:
        print("  nichts gefunden")
        return
    for eintrag in sorted(funde, key=lambda e: e[0]):
        ort, name, hinweis, beleg = eintrag
        print(f"  {mit_zeile} {ort}: {name}")
        print(f"      → {hinweis}")
        if beleg:
            print(f"      {beleg}")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    pfad = Path(sys.argv[1])
    if not pfad.exists():
        print(f"Datei nicht gefunden: {pfad}")
        return 1

    text = text_einlesen(pfad)
    if not text.strip():
        print("Die Datei enthält keinen Text.")
        return 1

    print("=" * 70)
    print(f"Prüfbericht: {pfad.name}")
    print("=" * 70)

    print("\nKennzahlen")
    print("-" * 70)
    for name, wert in kennzahlen(text).items():
        print(f"  {name}: {wert}")

    zeichen = pruefe_zeichen(text)
    block("SCHICHT 1 – Zeichenfehler (eindeutig, direkt korrigierbar)", zeichen)

    block("SCHICHT 2 – Wortwahl und Floskeln (ansehen, nicht blind ersetzen)",
          pruefe_wortlisten(text))

    block("SCHICHT 3 – Satz- und Absatzrhythmus", pruefe_rhythmus(text), "Absatz")

    print("\n" + "=" * 70)
    if zeichen:
        print(f"{len(zeichen)} Zeichenfehler sollten behoben werden – die sind eindeutig.")
    print("Alles Übrige ist ein Hinweis, kein Urteil. Ein Markerwort kann im")
    print("Einzelfall genau das richtige sein. Begründungen: regeln/sprache-pruefen.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
