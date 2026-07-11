#!/usr/bin/env python3
"""Convert a photo to ASCII art for a neofetch-style GitHub profile.

Usage: python ascii_convert.py <image> [width] [height] [--invert]

Maps dark pixels to dense glyphs and light pixels to sparse ones (use
--invert for a dark-background photo). Output is written to ascii_art.txt.
"""
import sys
from PIL import Image, ImageOps, ImageFilter

# Dense -> sparse ramp; trailing space means highlights vanish into background.
RAMP = "@%#WM8B$&okbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def to_ascii(path, width=58, height=46, invert=False):
    img = Image.open(path).convert("L")
    img = ImageOps.autocontrast(img, cutoff=2)
    img = img.filter(ImageFilter.SHARPEN)
    # Character cells are ~2x taller than wide; resize handles the aspect.
    img = img.resize((width, height), Image.LANCZOS)
    if invert:
        img = ImageOps.invert(img)
    px = img.load()
    lines = []
    for y in range(height):
        # anything near-white is background — force to space, not '.'
        row = "".join(
            " " if px[x, y] >= 242 else RAMP[px[x, y] * (len(RAMP) - 1) // 255]
            for x in range(width)
        )
        lines.append(row.rstrip())
    return "\n".join(lines)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--invert"]
    invert = "--invert" in sys.argv
    path = args[0]
    width = int(args[1]) if len(args) > 1 else 58
    height = int(args[2]) if len(args) > 2 else 46
    art = to_ascii(path, width, height, invert)
    with open("ascii_art.txt", "w") as f:
        f.write(art)
    print(art)
