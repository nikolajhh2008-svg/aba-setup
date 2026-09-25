#!/usr/bin/env python3
"""Bündelt die Regelwerke für die App-Variante (Claude-App, ChatGPT).

In der App gibt es kein Nachladen einzelner Dateien, und ChatGPT nimmt im
Gratis-Tarif nur fünf Dateien pro Projekt. Dieses Skript fasst die Regelwerke
aus regeln/ zu vier Themenpaketen zusammen und die eigenen Dateien aus mein/
zu einer fünften. Jede Quelldatei bleibt im Paket als eigener Abschnitt mit
ihrem Dateinamen erkennbar, damit Verweise wie „siehe zitierstile.md“ weiter
auffindbar sind.

Aufruf (im Ordner des Setups):
    python3 werkzeuge/buendeln.py            schreibt fuer-die-app/wissen/ und fuer-die-app/skills/
    python3 werkzeuge/buendeln.py --pruefen  meldet nur, ob die Pakete aktuell sind
"""
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
REGELN = WURZEL / "regeln"
MEIN = WURZEL / "mein"
ZIEL = WURZEL / "fuer-die-app" / "wissen"
SKILLS = WURZEL / ".claude" / "skills"
ZIP_ZIEL = WURZEL / "fuer-die-app" / "skills"

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
        ["schreibweise.md", "schreibhandwerk.md", "sprache-pruefen.md",
         "stilvorbilder.md",
         # Übernommener Skill humanizer-de (MIT), Pfade relativ zur Wurzel
         "../.claude/skills/humanizer-de/SKILL.md",
         "../.claude/skills/humanizer-de/references/patterns.md",
         "../.claude/skills/humanizer-de/references/decision-tables.md"],
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
             "Enthält: " + ", ".join(f"`{Path(d).name}`" for d in dateien) + "\n"]
    for name in dateien:
        pfad = (ordner / name).resolve()
        if not pfad.exists():
            raise SystemExit(f"Fehlt: {ordnername}/{name}")
        inhalt = ohne_frontmatter(pfad.read_text(encoding="utf-8"))
        anzeige = pfad.relative_to(WURZEL)
        teile.append(f"\n\n---\n\n<!-- Datei: {anzeige} -->\n\n{inhalt.rstrip()}\n")
    return "".join(teile)


def soll() -> dict[str, str]:
    ergebnis = {name: baue(titel, REGELN, dateien, "regeln")
                for name, (titel, dateien) in PAKETE.items()}
    name, titel, dateien = MEIN_PAKET
    ergebnis[name] = baue(titel, MEIN, dateien, "mein")
    return ergebnis


def fehlende_regelwerke() -> list[str]:
    gebuendelt = {d for _, dateien in PAKETE.values() for d in dateien if "/" not in d}
    return sorted(p.name for p in REGELN.glob("*.md") if p.name not in gebuendelt)


def skill_zip(ordner: Path) -> bytes:
    """Ein Skill-Ordner als ZIP für den Upload in Claude (Cowork, Claude-App).
    Feste Zeitstempel, damit dieselben Dateien dieselbe ZIP ergeben."""
    import io, zipfile
    puffer = io.BytesIO()
    with zipfile.ZipFile(puffer, "w", zipfile.ZIP_DEFLATED) as z:
        for datei in sorted(p for p in ordner.rglob("*") if p.is_file()):
            if "__pycache__" in datei.parts or datei.name == ".DS_Store":
                continue
            info = zipfile.ZipInfo(f"{ordner.name}/{datei.relative_to(ordner).as_posix()}",
                                   date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, datei.read_bytes())
    return puffer.getvalue()


def zips() -> dict[str, bytes]:
    return {f"{o.name}.zip": skill_zip(o) for o in sorted(SKILLS.iterdir())
            if (o / "SKILL.md").exists()}


def main() -> int:
    fehlend = fehlende_regelwerke()
    if fehlend:
        print("Diese Regelwerke stecken in keinem Paket:", ", ".join(fehlend))
        return 1
    pakete = soll()
    if "--pruefen" in sys.argv:
        veraltet = [n for n, t in pakete.items()
                    if not (ZIEL / n).exists() or (ZIEL / n).read_text(encoding="utf-8") != t]
        veraltet += [n for n, b in zips().items()
                     if not (ZIP_ZIEL / n).exists() or (ZIP_ZIEL / n).read_bytes() != b]
        if veraltet:
            print("Veraltet:", ", ".join(veraltet), "– python3 werkzeuge/buendeln.py ausführen")
            return 1
        print(f"Alle {len(pakete)} Pakete und Skill-ZIPs sind aktuell.")
        return 0
    ZIEL.mkdir(parents=True, exist_ok=True)
    for name, text in pakete.items():
        (ZIEL / name).write_text(text, encoding="utf-8")
        print(f"{name}: {len(text):,} Zeichen".replace(",", "."))
    ZIP_ZIEL.mkdir(parents=True, exist_ok=True)
    for alt in ZIP_ZIEL.glob("*.zip"):
        alt.unlink()
    for name, daten in zips().items():
        (ZIP_ZIEL / name).write_bytes(daten)
    print(f"{len(zips())} Skill-ZIPs in fuer-die-app/skills/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
