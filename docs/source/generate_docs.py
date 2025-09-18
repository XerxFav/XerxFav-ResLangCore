import subprocess

# Генерация SVG из DOT
subprocess.run([
    "dot", "-Tsvg", "scripts/ci_phase_map.dot", "-o", "docs/source/_static/ci_phase_map.svg"
])
