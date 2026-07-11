import sys
from PIL import Image, ImageOps, ImageFilter

RAMP = "@%#WM8B$&okbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
WHITE_POINT = 175  # anything brighter is bare skin/background -> space

def convert(path, width, height, white=WHITE_POINT):
    img = Image.open(path).convert("L")
    img = img.crop((80, 0, 300, 315))          # head + collar, 0.70 aspect
    img = ImageOps.autocontrast(img, cutoff=1)
    img = img.filter(ImageFilter.SHARPEN)
    img = img.resize((width, height), Image.LANCZOS)
    px = img.load()
    lines = []
    for y in range(height):
        row = ""
        for x in range(width):
            p = px[x, y]
            if p >= white:
                row += " "
            else:
                t = (p / white) ** 1.2          # keep darks punchy
                row += RAMP[int(t * (len(RAMP) - 2))]
        lines.append(row.rstrip())
    return "\n".join(lines)

if __name__ == "__main__":
    white = int(sys.argv[1]) if len(sys.argv) > 1 else WHITE_POINT
    art = convert("photo_clean.png", 62, 48, white)
    open("ascii_art.txt", "w").write(art)
    print(art)
