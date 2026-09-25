#!/usr/bin/env python3
"""Prüft das ganze Setup auf innere Stimmigkeit.

Für alle, die das Repository weiterentwickeln. Meldet jede Prüfung einzeln,
zählt mit, wie viele gelaufen sind, und wertet einen Absturz als Fehler –
ein Prüfer, der bei einem Absturz „alles in Ordnung“ meldet, ist schlimmer
als keiner.

Aufruf (im Ordner des Setups):
    python3 werkzeuge/paket-pruefen.py
"""
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
MD = sorted(p for p in WURZEL.rglob("*.md")
            if ".git" not in p.parts and "wissen" not in p.parts)
ALLE_NAMEN = {p.name for p in WURZEL.rglob("*") if ".git" not in p.parts}
GRENZE_ANWEISUNG = 8000  # Zeichen, Grenze der ChatGPT-Projektanweisung

ergebnisse: list[tuple[str, bool, str]] = []


def pruefung(name):
    def huelle(funktion):
        try:
            befunde = funktion()
            ergebnisse.append((name, not befunde, "\n".join(befunde[:12])))
        except Exception as fehler:  # Absturz zählt als rot
            ergebnisse.append((name, False, f"Absturz: {fehler!r}"))
        return funktion
    return huelle


def rel(p: Path) -> str:
    return str(p.relative_to(WURZEL))


@pruefung("Verweise auf .md- und .py-Dateien zeigen auf vorhandene Dateien")
def _verweise():
    befunde = []
    muster = re.compile(r"`(?:[\w./-]*/)?([\w-]+\.(?:md|py))`")
    for p in MD:
        for nr, zeile in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            for name in muster.findall(zeile):
                if name not in ALLE_NAMEN:
                    befunde.append(f"{rel(p)}:{nr} verweist auf {name}")
    return befunde


@pruefung("Das Register nennt jedes Regelwerk")
def _register():
    register = (WURZEL / "regeln" / "00-register.md").read_text(encoding="utf-8")
    return [f"fehlt im Register: {p.name}" for p in sorted((WURZEL / "regeln").glob("*.md"))
            if p.name != "00-register.md" and f"`{p.name}`" not in register]


@pruefung("Jedes Regelwerk hat name, beschreibung und stand im Kopf")
def _frontmatter():
    befunde = []
    for p in sorted((WURZEL / "regeln").glob("*.md")):
        kopf = p.read_text(encoding="utf-8").split("\n---\n", 1)[0]
        for feld in ("name:", "beschreibung:", "stand:"):
            if feld not in kopf:
                befunde.append(f"{rel(p)}: {feld} fehlt")
    return befunde


@pruefung("Jeder Skill hat name und description")
def _skills():
    befunde = []
    for p in sorted(WURZEL.glob(".claude/skills/*/SKILL.md")):
        kopf = p.read_text(encoding="utf-8").split("\n---\n", 1)[0]
        for feld in ("name:", "description:"):
            if feld not in kopf:
                befunde.append(f"{rel(p)}: {feld} fehlt")
    return befunde


@pruefung("Kein Geviertstrich „—“")
def _geviert():
    return [f"{rel(p)}:{nr}" for p in MD
            for nr, z in enumerate(p.read_text(encoding="utf-8").splitlines(), 1)
            if "—" in z.replace("„—“", "")]  # „—“ in Anführung ist die Regel selbst


@pruefung("Deutsche Anführungszeichen: nach „ folgt “, kein gerades Zeichen")
def _anfuehrung():
    befunde = []
    muster = re.compile(r"„[^“\"\n]{0,200}\"")
    for p in MD:
        for nr, zeile in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if muster.search(zeile):
                befunde.append(f"{rel(p)}:{nr}")
    return befunde


@pruefung(f"Projektanweisung passt in {GRENZE_ANWEISUNG} Zeichen")
def _laenge():
    text = (WURZEL / "fuer-die-app" / "projektanweisung.md").read_text(encoding="utf-8")
    teil = text.split("\n---\n", 1)[1] if "\n---\n" in text else text
    n = len(teil.strip())
    return [] if n <= GRENZE_ANWEISUNG else [f"{n} Zeichen"]


@pruefung("Die App-Pakete in fuer-die-app/wissen/ sind aktuell")
def _pakete():
    lauf = subprocess.run([sys.executable, str(WURZEL / "werkzeuge" / "buendeln.py"), "--pruefen"],
                          capture_output=True, text=True)
    return [] if lauf.returncode == 0 else [(lauf.stdout + lauf.stderr).strip()]


@pruefung("Das Prüfwerkzeug text-pruefen.py läuft an einem Beispieltext")
def _textpruefer():
    beispiel = WURZEL / "werkzeuge" / ".probe.md"
    beispiel.write_text("Die Studie zeigt eine Wirkung. Sie wurde 2020 veröffentlicht.\n",
                        encoding="utf-8")
    try:
        lauf = subprocess.run([sys.executable, str(WURZEL / "werkzeuge" / "text-pruefen.py"),
                               str(beispiel)], capture_output=True, text=True)
    finally:
        beispiel.unlink()
    return [] if lauf.returncode in (0, 1) and "Traceback" not in lauf.stderr \
        else [f"Exit {lauf.returncode}: {lauf.stderr.strip()[:300]}"]


def main() -> int:
    for name, gruen, text in ergebnisse:
        print(("✓ " if gruen else "✗ ") + name)
        if not gruen:
            for zeile in text.splitlines():
                print("    " + zeile)
    rot = sum(1 for _, g, _ in ergebnisse if not g)
    print(f"\n{len(ergebnisse)} Prüfungen gelaufen, {rot} rot.")
    return 1 if rot else 0


if __name__ == "__main__":
    sys.exit(main())
