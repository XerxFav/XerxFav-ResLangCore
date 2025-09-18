from arca_core import headers

def generate_phase_structure():
    for name, meta in headers.MODULES.items():
        print(f"[{meta['phase']}] {name}: {meta['description']}")
