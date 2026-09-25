#!/usr/bin/env python3
"""Bündelt die Regelwerke für die App-Variante (Claude-App, ChatGPT).

In der App gibt es kein Nachladen einzelner Dateien, und ChatGPT nimmt im
Gratis-Tarif nur fünf Dateien pro Projekt. Dieses Skript fasst die Regelwerke
aus regeln/ zu vier Themenpaketen zusammen und die eigenen Dateien aus mein/
zu einer fünften. Jede Quelldatei bleibt im Paket als eigener Abschnitt mit
ihrem Dateinamen erkennbar, damit Verweise wie „siehe zitierstile.md“ weiter
auffindbar sind.

Aufruf (im Ordner des Setups):
    python3 werkzeuge/buendeln.py            schreibt fuer-die-app/wissen/
    python3 werkzeuge/buendeln.py --pruefen  meldet nur, ob die Pakete aktuell sind
"""
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
REGELN = WURZEL / "regeln"
MEIN = WURZEL / "mein"
ZIEL = WURZEL / "fuer-die-app" / "wissen"

PAKETE = {
    "1-planen.md": (
        "Planen: Thema, Aufbau, Methode, Fristen",
        ["00-register.md", "thema-und-leitfragen.md", "aufbau-der-arbeit.md",
         "methodik.md", "fristen-und-abgabe.md"],
    ),
    "2-quellen.md": (
        "Quellen: finden, prüfen, zitieren, Plagiat",
        ["recherche-wege.md", "quellen-und-zitieren.md", "zitierstile.md",
         "plagiat-und-eigenleistung.md"],
    ),
    "3-schreiben.md": (
        "Schreiben: Schreibweise, Handwerk, Sprache",
        ["schreibweise.md", "schreibhandwerk.md", "sprache-pruefen.md"],
    ),
    "4-regeln-und-pruefung.md": (
        "Regeln und Prüfung: KI, Protokoll, Beurteilung, Präsentation",
        ["ki-kennzeichnung.md", "begleitprotokoll.md", "beurteilung.md",
         "praesentation.md"],
    ),
}
MEIN_PAKET = ("5-meine-unterlagen.md", "Meine Unterlagen",
              ["profil.md", "schulvorgaben.md", "begleitprotokoll.md", "quellen.md",
               "ki-stellen.md"])

KOPF = ("<!-- Automatisch erzeugt von werkzeuge/buendeln.py – nicht von Hand "
        "bearbeiten, sondern die Quelldateien ändern und neu bündeln. -->\n\n")


def ohne_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        ende = text.find("\n---\n", 4)
        if ende != -1:
            return text[ende + 5:].lstrip("\n")
    return text


def baue(titel: str, ordner: Path, dateien: list[str], ordnername: str) -> str:
    teile = [KOPF, f"# {titel}\n\n",
             "Enthält: " + ", ".join(f"`{d}`" for d in dateien) + "\n"]
    for name in dateien:
        pfad = ordner / name
        if not pfad.exists():
            raise SystemExit(f"Fehlt: {ordnername}/{name}")
        inhalt = ohne_frontmatter(pfad.read_text(encoding="utf-8"))
        teile.append(f"\n\n---\n\n<!-- Datei: {ordnername}/{name} -->\n\n{inhalt.rstrip()}\n")
    return "".join(teile)


def soll() -> dict[str, str]:
    ergebnis = {name: baue(titel, REGELN, dateien, "regeln")
                for name, (titel, dateien) in PAKETE.items()}
    name, titel, dateien = MEIN_PAKET
    ergebnis[name] = baue(titel, MEIN, dateien, "mein")
    return ergebnis


def fehlende_regelwerke() -> list[str]:
    gebuendelt = {d for _, dateien in PAKETE.values() for d in dateien}
    return sorted(p.name for p in REGELN.glob("*.md") if p.name not in gebuendelt)


def main() -> int:
    fehlend = fehlende_regelwerke()
    if fehlend:
        print("Diese Regelwerke stecken in keinem Paket:", ", ".join(fehlend))
        return 1
    pakete = soll()
    if "--pruefen" in sys.argv:
        veraltet = [n for n, t in pakete.items()
                    if not (ZIEL / n).exists() or (ZIEL / n).read_text(encoding="utf-8") != t]
        if veraltet:
            print("Veraltet:", ", ".join(veraltet), "– python3 werkzeuge/buendeln.py ausführen")
            return 1
        print(f"Alle {len(pakete)} Pakete sind aktuell.")
        return 0
    ZIEL.mkdir(parents=True, exist_ok=True)
    for name, text in pakete.items():
        (ZIEL / name).write_text(text, encoding="utf-8")
        print(f"{name}: {len(text):,} Zeichen".replace(",", "."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
