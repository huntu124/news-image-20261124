#!/usr/bin/env python3
"""news-image-20261124 — writes one image summarising the world news of
Monday 24 November 2026 to $MAKEFUN_OUTPUT_DIR/entry.png.

The image (1080x1350 JPEG, a "front page" of eight headline cards) is
rendered deterministically with Pillow from the fixed story list in
render.py when Pillow is importable; otherwise the repository's
news-2026-11-24.jpg (produced by exactly that render) is written out
byte-identically. Both paths are deterministic: two runs produce identical
files. No network, no external API keys, standard library plus optional
Pillow. Run: python3 main.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def render_with_pillow(dest):
    try:
        from PIL import Image  # noqa: F401
        import render as r
    except Exception:
        return False
    try:
        r.render(dest)
        return True
    except Exception:
        return False


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    if not render_with_pillow(dest):
        import shutil
        shutil.copyfile(os.path.join(HERE, "news-2026-11-24.jpg"), dest)
    print("wrote", dest, os.path.getsize(dest), "bytes")


if __name__ == "__main__":
    main()
