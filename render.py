#!/usr/bin/env python3
"""Render the 24 November 2026 world-news digest image with Pillow.

Deterministic: fixed layout, fixed colours, fixed text, fixed font sizes.
Two runs produce byte-identical output. This script produced
news-2026-11-24.jpg shipped in this repository; main.py re-renders with the
same code when Pillow is available, and falls back to the shipped bytes
otherwise.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (246, 244, 239)
INK = (24, 24, 28)
MUTED = (110, 108, 104)
ACCENT = (178, 34, 34)
RULE = (208, 205, 198)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


STORIES = [
    ("IRAN / HORMUZ",
     "Mine blasts set three oil tankers ablaze in Strait of Hormuz",
     "Iran's IRGC Navy says two tankers struck naval mines in the eastern "
     "strait and fires broke out on all three vessels, a day after it "
     "claimed US air cover failed to stop the blasts; it warned ships "
     "against unauthorised routes."),
    ("GAZA",
     "Israeli drone strike kills three at Khan Younis police post",
     "A strike on a police post on Street 5 in Al-Mawasi killed three "
     "Palestinians and wounded five, medics at Nasser Hospital say; "
     "ceasefire violations since October 2025 have killed 1,675 people."),
    ("UN SECURITY COUNCIL",
     "Russia and Ukraine clash over Black Sea shipping attacks",
     "Moscow ruled out any new grain deal, calling it a scheme of Ukrainian "
     "food for Western weapons, and said Kyiv's forces have targeted more "
     "than 200 commercial vessels across five seas since July."),
    ("CYBER / SHIPPING",
     "US eyes Iran in dozens of cyberattacks against tankers",
     "US officials are probing possible Iranian responsibility for attacks "
     "on as many as 50 ships carrying oil and explosive cargoes, following "
     "the widening confrontation around the Gulf."),
    ("SPACE",
     "Report: Russia plans to put a nuclear weapon in space",
     "Intelligence assessments say Moscow is developing an orbital nuclear "
     "capability, a move that would breach the Outer Space Treaty and "
     "raise alarm across NATO capitals."),
    ("PACIFIC",
     "Solomon Islands flip allegiance back to Australia",
     "Honiara signals a realignment away from Beijing's security "
     "cooperation and back toward Canberra, reversing years of closer "
     "China ties in the Pacific."),
    ("UN / GAZA",
     "UN deputy chief: 'no excuse for inaction' on Gaza suffering",
     "As aid remains constrained and strikes continue, the UN's deputy "
     "chief demanded renewed humanitarian access across the enclave."),
    ("MARKETS",
     "Jensen is back, and shares rally",
     "The return of Nvidia's chief to the spotlight lifts tech shares, "
     "with investors reading the appearance as a signal of confidence "
     "in the AI build-out."),
]


def draw_text(draw, xy, text, f, fill, max_w):
    """Word-wrap to max_w, return y advance."""
    x, y = xy
    words, line = text.split(), ""
    lh = f.size + 5
    for w in words:
        trial = (line + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_w:
            line = trial
        else:
            draw.text((x, y), line, font=f, fill=fill)
            y += lh
            line = w
    if line:
        draw.text((x, y), line, font=f, fill=fill)
        y += lh
    return y


def render(path):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    f_head = font("DejaVuSerif-Bold.ttf", 24)
    f_body = font("DejaVuSans.ttf", 16)
    f_mast = font("DejaVuSerif-Bold.ttf", 48)
    f_date = font("DejaVuSans.ttf", 19)
    f_tag = font("DejaVuSans-Bold.ttf", 14)

    # Masthead
    d.rectangle([0, 0, W, 8], fill=ACCENT)
    d.text((54, 30), "THE WORLD IN ONE PAGE", font=f_mast, fill=INK)
    d.text((54, 94), "Monday 24 November 2026 \u00b7 a one-image digest of "
                     "the day's world news", font=f_date, fill=MUTED)
    d.line([54, 134, W - 54, 134], fill=INK, width=3)

    x0 = 54
    cw = W - 2 * x0
    for i, (kicker, head, body) in enumerate(STORIES):
        cy = 158 + i * 96
        d.rectangle([x0, cy, x0 + 4, cy + 88], fill=ACCENT)
        ty = cy + 2
        d.text((x0 + 18, ty), kicker, font=f_tag, fill=ACCENT)
        ty += 22
        ty = draw_text(d, (x0 + 18, ty), head, f_head, INK, cw - 24)
        draw_text(d, (x0 + 18, ty + 2), body, f_body, (60, 60, 64), cw - 24)

    # footer
    d.line([54, H - 52, W - 54, H - 52], fill=RULE, width=2)
    d.text((54, H - 42), "Sources: Xinhua \u00b7 Kyodo \u00b7 Firstpost \u00b7 "
                          "World Watch \u00b7 Balusco wires, 23 Nov 2026 \u00b7 "
                          "deterministic render \u00b7 MIT licence",
           font=f_tag, fill=MUTED)

    img.save(path, "JPEG", quality=92)
    return path


if __name__ == "__main__":
    import sys
    print(render(sys.argv[1] if len(sys.argv) > 1 else "news-2026-11-24.jpg"))
