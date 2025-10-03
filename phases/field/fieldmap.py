# fieldmap.py — визуализация фазовых переходов

from schema import is_valid_transition

PHASES = ["neutral", "positive", "negative"]

def render_map():
    with open("fieldmap_output.txt", "w") as f:
        f.write("Phase Transition Map:\n\n")
        for from_phase in PHASES:
            for to_phase in PHASES:
                if is_valid_transition(from_phase, to_phase):
                    line = f"{from_phase} → {to_phase}\n"
                    f.write(line)
                    print(line)

if __name__ == "__main__":
    render_map()

def generate_dot():
    with open("fieldmap.dot", "w") as f:
        f.write("digraph PhaseMap {\n")
        for from_phase in PHASES:
            for to_phase in PHASES:
                if is_valid_transition(from_phase, to_phase):
                    f.write(f'  "{from_phase}" -> "{to_phase}";\n')
        f.write("}\n")

if __name__ == "__main__":
    generate_dot()
