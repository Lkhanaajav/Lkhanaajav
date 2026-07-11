import sys
from PIL import Image, ImageOps, ImageFilter

RAMP = "@%#WM8B$&okbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def convert(path, width=62, height=48, white=195, crop=(95, 5, 290, 278)):
    img = Image.open(path).convert("L")
    img = img.crop(crop)                       # face-dominant crop
    img = ImageOps.autocontrast(img, cutoff=1)
    # large-radius unsharp = local contrast: darkens eye/nose shadows vs skin
    img = img.filter(ImageFilter.UnsharpMask(radius=10, percent=130, threshold=2))
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
                t = (p / white) ** 1.3         # soft shadows stay light chars
                row += RAMP[int(t * (len(RAMP) - 2))]
        lines.append(row.rstrip())
    return "\n".join(lines)

if __name__ == "__main__":
    white = int(sys.argv[1]) if len(sys.argv) > 1 else 195
    art = convert("photo_clean.png", white=white)
    open("ascii_art.txt", "w").write(art)
    print(art)
