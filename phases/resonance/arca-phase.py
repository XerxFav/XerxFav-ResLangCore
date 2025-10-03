import graphviz
import yaml
import os

def load_metadata(phases_dir="phases"):
    metadata = {}
    for phase in os.listdir(phases_dir):
        path = os.path.join(phases_dir, phase, "arca-phase.yml")
        if os.path.exists(path):
            with open(path) as f:
                data = yaml.safe_load(f)
                metadata[data["phase"]["name"]] = data["phase"]
    return metadata

def extract_graph(metadata):
    edges = []
    for name, data in metadata.items():
        src = data.get("evolves_from")
        if src:
            edges.append((src, name, "evolves"))
    return edges

def generate_svg_map(metadata, export="docs/phase-map"):
    dot = graphviz.Digraph(comment="Arca Phase Map")
    for name in metadata:
        dot.node(name)
    for src, dst, rel in extract_graph(metadata):
        dot.edge(src, dst, label=rel)
    dot.render(export, format='svg')
