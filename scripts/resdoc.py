import os
from pathlib import Path

def scan_headers(src_dir):
    headers = []
    for path in Path(src_dir).rglob("*.h"):
        headers.append(str(path.relative_to(src_dir)))
    return headers

def generate_readme(headers, output):
    with open(output, "w") as f:
        f.write("# 📘 ResLang Core Documentation\n\n")
        for h in headers:
            f.write(f"- `{h}` — фазовый интерфейс\n")

def generate_svg(headers, output):
    with open(output, "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400">\n')
        y = 20
        for h in headers:
            f.write(f'<text x="20" y="{y}" font-size="14">{h}</text>\n')
            y += 20
        f.write('</svg>\n')

if __name__ == "__main__":
    headers = scan_headers("reslang_core/include")
    generate_readme(headers, "reslang_core/docs/README.md")
    generate_svg(headers, "docs/ci/ci_phase_map.svg")
