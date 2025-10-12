from graphviz import Digraph
from pathlib import Path
import yaml

dot = Digraph(comment='ArcaLang Phase Map')
phases_dir = Path("phases")

for phase in sorted(phases_dir.iterdir()):
    mig_file = phase / "migration.yaml"
    if mig_file.exists():
        data = yaml.safe_load(mig_file.read_text(encoding="utf-8"))
        name = phase.name
        source = data.get("evolves_from", "root")
        dot.node(name, name)
        dot.edge(source, name)

dot.render("ci/ci_phase_map.svg", format="svg", cleanup=True)
print("✅ SVG фазовой карты создан.")
