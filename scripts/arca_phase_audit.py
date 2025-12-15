#!/usr/bin/env python3
import subprocess, re, os
from collections import defaultdict
from graphviz import Digraph

PHASES = {
    "Quantum": ["arca_core/quantum"],
    "Logical": ["arca_core/logical"],
    "Ontological": ["arca_core/ontology"],
    "Memory": ["arca_core/memory"],
    "Docs": ["docs", "README.md"],
    "CI": [".github/workflows", ".woodpecker.yml", ".drone.yml"]
}

def get_commits():
    raw = subprocess.check_output(["git", "log", "--pretty=format:%h %s"]).decode()
    commits = defaultdict(list)
    for line in raw.splitlines():
        for phase in PHASES:
            if re.search(phase, line):
                commits[phase].append(line)
    return commits

def get_files():
    changed = subprocess.check_output(["git", "diff", "--cached", "--name-only"]).decode().splitlines()
    files_by_phase = defaultdict(list)
    for f in changed:
        for phase, paths in PHASES.items():
            if any(f.startswith(p) for p in paths):
                files_by_phase[phase].append(f)
    return files_by_phase

def generate_svg(commits):
    dot = Digraph(comment='Phase Audit')
    for phase in PHASES:
        dot.node(phase, phase)
        for c in commits.get(phase, []):
            cid = c.split()[0]
            dot.node(cid, c)
            dot.edge(phase, cid)
    dot.render('ci_phase_map.svg', format='svg')
    print("🧬 SVG-граф сохранён как ci_phase_map.svg")

def main():
    print("🔍 Аудит фазовой структуры...")
    commits = get_commits()
    files = get_files()

    for phase in PHASES:
        print(f"\n📦 Фаза: {phase}")
        print("  🧠 Коммиты:")
        for c in commits.get(phase, []):
            print(f"    - {c}")
        print("  📂 Файлы:")
        for f in files.get(phase, []):
            print(f"    - {f}")

    generate_svg(commits)

if __name__ == "__main__":
    main()

