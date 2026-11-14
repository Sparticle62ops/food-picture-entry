#!/usr/bin/env python3
"""Emit the entry picture: garlic butter steak bites, cast-iron hero shot."""
import sys
from pathlib import Path
from PIL import Image

SRC = Path(__file__).parent / "steak-bites-hero.png"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "final.png"

def emit() -> Path:
    if not SRC.exists():
        raise SystemExit(f"missing source picture: {SRC}")
    with Image.open(SRC) as im:
        im = im.convert("RGB")
        w, h = im.size
        if w < 1000 or h < 600:
            raise SystemExit(f"picture too small: {w}x{h}")
        im.save(OUT, "PNG")
    print(f"wrote {OUT} ({w}x{h} RGB)")
    return OUT

if __name__ == "__main__":
    emit()
