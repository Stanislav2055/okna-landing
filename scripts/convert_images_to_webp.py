"""Convert .jpg, .jpeg, .png under public/images to .webp (Pillow)."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent / "public" / "images"
EXTS = {".jpg", ".jpeg", ".png"}


def main() -> int:
    if not ROOT.is_dir():
        print(f"ERROR: not a directory: {ROOT}", file=sys.stderr)
        return 1

    paths = sorted(
        p
        for p in ROOT.rglob("*")
        if p.is_file() and p.suffix.lower() in EXTS
    )
    print(f"Scan: {ROOT}")
    print(f"Found {len(paths)} file(s)")

    for src in paths:
        out = src.with_suffix(".webp")
        try:
            with Image.open(src) as im:
                im.save(out, "WEBP", quality=85, method=6)
            print(f"OK: {src.relative_to(ROOT)} -> {out.name}")
        except Exception as e:
            print(f"FAIL: {src}: {e}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
