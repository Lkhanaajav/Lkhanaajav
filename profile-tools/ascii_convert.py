import math
from PIL import Image, ImageOps, ImageFilter

RAMP = "@%#WM8B$&okbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
W, H = 70, 54
SOBEL_X = ImageFilter.Kernel((3, 3), [-1, 0, 1, -2, 0, 2, -1, 0, 1], scale=1, offset=128)
SOBEL_Y = ImageFilter.Kernel((3, 3), [-1, -2, -1, 0, 0, 0, 1, 2, 1], scale=1, offset=128)

img = Image.open("photo_clean.png").convert("L")
img = img.crop((95, 5, 290, 278))
img = ImageOps.autocontrast(img, cutoff=1)

big = img.resize((W * 3, H * 3), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1))
edges = big.filter(ImageFilter.FIND_EDGES).resize((W, H), Image.LANCZOS).load()  # G's detector
gx = big.filter(SOBEL_X).resize((W, H), Image.LANCZOS).load()
gy = big.filter(SOBEL_Y).resize((W, H), Image.LANCZOS).load()
dark = img.filter(ImageFilter.UnsharpMask(radius=10, percent=110)).resize((W, H), Image.LANCZOS).load()

def edge_glyph(dx, dy):
    ang = math.degrees(math.atan2(dy, dx)) % 180
    if ang < 22.5 or ang >= 157.5:
        return "|"
    if ang < 67.5:
        return "\\"
    if ang < 112.5:
        return "-"
    return "/"

grid = [[" "] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        p = dark[x, y]
        if p < 130:
            grid[y][x] = RAMP[int(min((p / 195) ** 1.25, 1.0) * (len(RAMP) - 2))]
        elif edges[x, y] > 26 and p < 215:
            grid[y][x] = edge_glyph(gx[x, y] - 128, gy[x, y] - 128)

for y in range(H):
    for x in range(W):
        if grid[y][x] != " ":
            nb = sum(1 for j in range(max(0, y-1), min(H, y+2))
                     for i in range(max(0, x-1), min(W, x+2))
                     if (i, j) != (x, y) and grid[j][i] != " ")
            if nb <= 1:
                grid[y][x] = " "

open("ascii_art.txt", "w").write("\n".join("".join(r).rstrip() for r in grid))
print("ascii_art.txt written")
