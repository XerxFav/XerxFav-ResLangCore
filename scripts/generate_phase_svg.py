# scripts/generate_phase_svg.py
from graphviz import Digraph

dot = Digraph(comment='Phase Map')
dot.node('A', 'Phase 1')
dot.node('B', 'Phase 2')
dot.edge('A', 'B', label='migration')
dot.render('ci/ci_phase_map.svg', format='svg')
