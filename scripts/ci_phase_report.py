import subprocess
import re
import graphviz

phases = ["Quantum", "Logical", "Ontological", "Memory", "Docs", "CI"]
commits = subprocess.check_output(["git", "log", "--pretty=format:%h %s"]).decode().splitlines()

phase_map = {phase: [] for phase in phases}
for line in commits:
    for phase in phases:
        if re.search(phase, line):
            phase_map[phase].append(line)

# SVG-граф
dot = graphviz.Digraph(comment='Phase Map')
for phase, lines in phase_map.items():
    dot.node(phase, phase)
    for line in lines:
        dot.node(line.split()[0], line)
        dot.edge(phase, line.split()[0])

dot.render('ci_phase_map.svg', format='svg')
