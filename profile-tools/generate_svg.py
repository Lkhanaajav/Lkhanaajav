#!/usr/bin/env python3
"""Generate dark_mode.svg / light_mode.svg: ASCII portrait + neofetch info panel."""
from html import escape

ART_FILE = "ascii_art.txt"
INFO_WIDTH = 62          # every info line padded to this many chars
CHAR_W = 7.2             # 12px monospace advance
ART_LH = 13
PAD = 20

THEMES = {
    "dark_mode": dict(bg="#0d1117", border="#30363d", art="#c9d1d9",
                      key="#ffa657", val="#c9d1d9", dot="#484f58",
                      user="#58a6ff", muted="#8b949e"),
    "light_mode": dict(bg="#ffffff", border="#d0d7de", art="#57606a",
                       key="#953800", val="#1f2328", dot="#d0d7de",
                       user="#0969da", muted="#57606a"),
}

USERNAME = "lkhanaajav@github"
INFO = [
    ("USER", USERNAME),
    ("SEP", "-" * 45),
    ("KV", ("Role", "AI Engineer, CompletaAI Co-founder")),
    ("KV", ("Education", "M.S. ECE, University of Oklahoma (2026)")),
    ("KV", ("Location", "Austin, TX")),
    ("KV", ("Awards", "IMO Silver Medalist, IEEE/MDPI author")),
    ("BLANK", None),
    ("SECTION", "Languages & AI/ML"),
    ("KV", ("Programming", "Python, C/C++, TypeScript, JavaScript, SQL")),
    ("KV", ("AI/ML", "PyTorch, Transformers, LLMs, RAG, CV")),
    ("KV", ("LLM", "MCP servers, agentic workflows, evals")),
    ("KV", ("Vision", "segmentation, depth, BEV perception")),
    ("BLANK", None),
    ("SECTION", "Systems & Robotics"),
    ("KV", ("Backend", "FastAPI, REST APIs, Docker, AWS, GCP, Linux")),
    ("KV", ("Realtime", "3ms/frame CPU inference, embedded ARM64")),
    ("KV", ("Robotics", "autonomous navigation, sensor fusion, SLAM")),
    ("KV", ("Data", "pandas, NumPy, time-series, IoT pipelines")),
    ("BLANK", None),
    ("SECTION", "Featured Projects"),
    ("KV", ("timeseries-mcp", "MCP server: stats tools for AI agents")),
    ("KV", ("mcp-trajectory-evals", "eval harness for tool-using agents")),
    ("KV", ("tracelab", "AI agent observability & evaluation")),
    ("KV", ("email-guardian", "Claude-powered email intelligence")),
    ("BLANK", None),
    ("SECTION", "Currently"),
    ("KV", ("Thesis", "real-time monocular BEV navigation")),
    ("KV", ("Seeking", "AI/ML engineering roles in Austin")),
    ("BLANK", None),
    ("SECTION", "Contact"),
    ("KV", ("Email", "lhanaamijgee@gmail.com")),
    ("KV", ("LinkedIn", "linkedin.com/in/lhanaa")),
    ("KV", ("GitHub", "github.com/Lkhanaajav")),
]

art_lines = open(ART_FILE).read().splitlines()
art_w = max(len(l) for l in art_lines) * CHAR_W
info_x = PAD + art_w + 24
width = round(info_x + INFO_WIDTH * CHAR_W + PAD)
height = round(len(art_lines) * ART_LH + 2 * PAD)
INFO_LH = min(22, (height - 60) // len(INFO))   # stretch panel to full height
info_y0 = (height - len(INFO) * INFO_LH) / 2 + 12


def kv_tspans(key, value, c):
    n = INFO_WIDTH - len(key) - 3 - len(value)  # "Key: " + dots + " " + value
    dots = "." * max(n, 3)
    return (f'<tspan fill="{c["key"]}">{escape(key)}:</tspan>'
            f'<tspan fill="{c["dot"]}"> {dots} </tspan>'
            f'<tspan fill="{c["val"]}">{escape(value)}</tspan>')


for name, c in THEMES.items():
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'viewBox="0 0 {width} {height}" font-family="SFMono-Regular,Consolas,'
           f'Liberation Mono,Menlo,monospace" font-size="12px">',
           f'<rect x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="8" '
           f'fill="{c["bg"]}" stroke="{c["border"]}"/>']
    def tl(n_chars):
        # pin line width so alignment survives any viewer font
        return f'textLength="{n_chars * CHAR_W:.1f}" lengthAdjust="spacingAndGlyphs"'

    y = PAD + ART_LH
    for line in art_lines:
        if line:
            out.append(f'<text x="{PAD}" y="{y}" xml:space="preserve" {tl(len(line))} '
                       f'fill="{c["art"]}">{escape(line)}</text>')
        y += ART_LH
    y = info_y0
    full = tl(INFO_WIDTH)
    for kind, data in INFO:
        if kind == "USER":
            out.append(f'<text x="{info_x}" y="{y:.0f}" font-weight="bold" {tl(len(data))} '
                       f'fill="{c["user"]}">{escape(data)}</text>')
        elif kind == "SEP":
            out.append(f'<text x="{info_x}" y="{y:.0f}" {tl(len(data))} '
                       f'fill="{c["muted"]}">{data}</text>')
        elif kind == "SECTION":
            dashes = "-" * (INFO_WIDTH - len(data) - 3)
            out.append(f'<text x="{info_x}" y="{y:.0f}" xml:space="preserve" {full}>'
                       f'<tspan fill="{c["muted"]}">- </tspan>'
                       f'<tspan fill="{c["user"]}" font-weight="bold">{escape(data)}</tspan>'
                       f'<tspan fill="{c["muted"]}"> {dashes}</tspan></text>')
        elif kind == "KV":
            out.append(f'<text x="{info_x}" y="{y:.0f}" xml:space="preserve" {full}>'
                       + kv_tspans(*data, c) + "</text>")
        y += INFO_LH
    out.append("</svg>")
    with open(f"{name}.svg", "w") as f:
        f.write("\n".join(out))
    print(f"{name}.svg  {width}x{height}")
