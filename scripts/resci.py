import os
from datetime import datetime

REPO_PATH = os.path.expanduser("~/ResLang/ArcaLang/XerxFav-ResLangCore")
LOG_PATH = os.path.join(REPO_PATH, "ci", "phase_report.md")

def scan_phases():
    phases = []
    for root, _, files in os.walk(REPO_PATH):
        for f in files:
            if f.endswith(".cpp") or f.endswith(".h"):
                phases.append(os.path.relpath(os.path.join(root, f), REPO_PATH))
    return phases

def generate_report(phases):
    with open(LOG_PATH, "w") as f:
        f.write(f"# 📊 CI Phase Report\n\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\n\n")
        for p in phases:
            f.write(f"- `{p}` — фазовый модуль\n")

if __name__ == "__main__":
    os.makedirs(os.path.join(REPO_PATH, "ci"), exist_ok=True)
    phases = scan_phases()
    generate_report(phases)
    print("✅ CI отчёт создан:", LOG_PATH)
