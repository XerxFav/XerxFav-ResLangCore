#!/usr/bin/env python3
import os

PHASE_DIRS = ["arca_core", "arca_logic", "arca_vm"]
MAKEFILE_PATH = "Makefile.phases"
BOOST_FLAGS = "-I/usr/include/boost -DBOOST_ALL_NO_LIB"
CXX_FLAGS = "-std=c++23 -Wall -Wextra -O2"

def collect_sources(phase):
    src_dir = os.path.join(phase, "src")
    return [f for f in os.listdir(src_dir) if f.endswith(".cpp")]

def generate_target(phase, sources):
    obj_files = [f.replace(".cpp", ".o") for f in sources]
    lines = [
        f"# 🔧 Фаза: {phase}",
        f"{phase}_objects = {' '.join(obj_files)}",
        f"{phase}_build: $({phase}_objects)",
        f"\t@echo '✅ Сборка {phase} завершена.'",
        ""
    ]
    for src in sources:
        obj = src.replace(".cpp", ".o")
        lines.append(f"{obj}: {phase}/src/{src}")
        lines.append(f"\tg++ {CXX_FLAGS} {BOOST_FLAGS} -c $< -o $@")
        lines.append("")
    return lines

def main():
    with open(MAKEFILE_PATH, "w") as f:
        f.write("# 📦 Автоматически сгенерированные фазовые цели\n\n")
        for phase in PHASE_DIRS:
            if os.path.isdir(phase):
                sources = collect_sources(phase)
                if sources:
                    lines = generate_target(phase, sources)
                    f.write("\n".join(lines))

if __name__ == "__main__":
    main()
