from arca_core import headers

with open("ontology.md", "w", encoding="utf-8") as f:
    f.write("# Ontology of ArcaLang\n\n")
    for name, meta in headers.MODULES.items():
        f.write(f"## {name}\n")
        f.write(f"- Phase: {meta['phase']}\n")
        f.write(f"- Description: {meta['description']}\n")
        f.write(f"- Dependencies: {', '.join(meta['dependencies'])}\n\n")
