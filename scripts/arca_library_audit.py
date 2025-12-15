#!/usr/bin/env python3
import matplotlib.pyplot as plt
import os, ast, subprocess
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
LIB_DIRS = [ROOT / "arca_langlib"]  # при необходимости добавь ROOT/"arca_core"
OUT_CI = ROOT / "ci" / "library_audit.md"
OUT_DOCS = ROOT / "docs" / "ci" / "library_audit.md"

def fmt_ts(ts):
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

def git_dates(rel_path):
    try:
        first = subprocess.check_output(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%ad", "--date=iso", "--", rel_path],
            cwd=ROOT, text=True
        ).strip().splitlines()
        last = subprocess.check_output(
            ["git", "log", "--follow", "-1", "--format=%ad", "--date=iso", "--", rel_path],
            cwd=ROOT, text=True
        ).strip()
        return first[0] if first else None, last if last else None
    except Exception:
        return None, None

def analyze_python_file(path: Path):
    info = {
        "module": str(path.relative_to(ROOT)),
        "size": path.stat().st_size,
        "mtime": fmt_ts(path.stat().st_mtime),
        "ctime": fmt_ts(path.stat().st_ctime),
        "classes": [],
        "functions": [],
        "needs_docstring": [],
        "doc_coverage": {"classes": (0,0), "functions": (0,0)}
    }
    first, last = git_dates(str(path.relative_to(ROOT)))
    if first: info["git_first"] = first
    if last: info["git_last"] = last

    try:
        src = path.read_text(encoding="utf-8", errors="ignore")
        tree = ast.parse(src, filename=str(path))
    except Exception as e:
        info["parse_error"] = str(e)
        return info

    class_docs, func_docs = 0, 0
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            doc = ast.get_docstring(node)
            public = not node.name.startswith("_")
            info["classes"].append({"name": node.name, "public": public, "has_doc": bool(doc)})
            if doc: class_docs += 1
            if public and not doc: info["needs_docstring"].append(f"Class {node.name}")
        elif isinstance(node, ast.FunctionDef):
            doc = ast.get_docstring(node)
            public = not node.name.startswith("_")
            info["functions"].append({"name": node.name, "public": public, "has_doc": bool(doc)})
            if doc: func_docs += 1
            if public and not doc: info["needs_docstring"].append(f"Function {node.name}")

    info["doc_coverage"]["classes"] = (class_docs, len(info["classes"]))
    info["doc_coverage"]["functions"] = (func_docs, len(info["functions"]))
    return info

def collect_library():
    modules, anomalies = [], []
    for lib_dir in LIB_DIRS:
        for path in lib_dir.rglob("*"):
            name = path.name
            if name.startswith("#") or name.endswith("~") or "," in name:
                anomalies.append(f"Temporary/backup: {path.relative_to(ROOT)}")
            if path.suffix in {".pyc", ".pyo", ".o", ".so"} and path.suffix != ".py":
                anomalies.append(f"Binary artifact: {path.relative_to(ROOT)}")
            if path.is_file() and path.suffix == ".py":
                modules.append(analyze_python_file(path))
    return modules, anomalies

def write_markdown(mods, anomalies, out_path: Path):
    lines = []
    lines.append("# ArcaLang Library Audit Report\n")
    lines.append("## 📊 Summary with Docstring Coverage\n")
    lines.append("| Module | Classes | Functions | Docstring Coverage (Classes) | Docstring Coverage (Functions) | Last commit | Last mtime |")
    lines.append("|---|---:|---:|---|---|---|---|")
    for m in mods:
        cc = m["doc_coverage"]["classes"]
        fc = m["doc_coverage"]["functions"]
        cc_str = f"{cc[0]}/{cc[1]} ({(cc[0]/cc[1]*100 if cc[1] else 0):.0f}%)"
        fc_str = f"{fc[0]}/{fc[1]} ({(fc[0]/fc[1]*100 if fc[1] else 0):.0f}%)"
        lines.append(f"| {m['module']} | {len(m['classes'])} | {len(m['functions'])} | {cc_str} | {fc_str} | {m.get('git_last','n/a')} | {m['mtime']} |")
    lines.append("\n---\n")
    lines.append("## 📂 Details by module\n")
    for m in mods:
        lines.append(f"### {m['module']}")
        lines.append(f"- **Size:** {m['size']} bytes")
        if "git_first" in m: lines.append(f"- **Git first commit:** {m['git_first']}")
        if "git_last" in m: lines.append(f"- **Git last commit:** {m['git_last']}")
        lines.append(f"- **Filesystem mtime:** {m['mtime']}")
        lines.append(f"- **Filesystem ctime:** {m['ctime']}")
        if m.get("parse_error"):
            lines.append(f"- **Parse error:** {m['parse_error']}\n")
            continue
        if m["classes"]:
            lines.append("#### Classes")
            for c in m["classes"]:
                lines.append(f"- Class {c['name']} | Public: {c['public']} | Docstring: {c['has_doc']}")
        if m["functions"]:
            lines.append("#### Functions")
            for f in m["functions"]:
                lines.append(f"- Function {f['name']} | Public: {f['public']} | Docstring: {f['has_doc']}")
        if m["needs_docstring"]:
            lines.append("#### Needs docstring (public API)")
            for nd in m["needs_docstring"]:
                lines.append(f"- {nd}")
        lines.append("\n")
    if anomalies:
        lines.append("---\n## ⚠️ Anomalies")
        for a in anomalies:
            lines.append(f"- {a}")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")

def main():
    mods, anomalies = collect_library()
    write_markdown(mods, anomalies, OUT_CI)
    write_markdown(mods, anomalies, OUT_DOCS)
    print(f"Wrote audit to {OUT_CI} and {OUT_DOCS}")

if __name__ == "__main__":
    main()
def plot_docstring_coverage(mods, out_path: Path):
    modules = [m["module"] for m in mods]
    class_cov = [
        (m["doc_coverage"]["classes"][0] / m["doc_coverage"]["classes"][1] * 100
         if m["doc_coverage"]["classes"][1] else 0)
        for m in mods
    ]
    func_cov = [
        (m["doc_coverage"]["functions"][0] / m["doc_coverage"]["functions"][1] * 100
         if m["doc_coverage"]["functions"][1] else 0)
        for m in mods
    ]

    x = range(len(modules))
    width = 0.35

    plt.figure(figsize=(10,6))
    plt.bar([i - width/2 for i in x], class_cov, width, label="Classes", color="skyblue")
    plt.bar([i + width/2 for i in x], func_cov, width, label="Functions", color="lightgreen")

    plt.xticks(x, modules, rotation=30, ha="right")
    plt.ylabel("Docstring coverage (%)")
    plt.title("ArcaLang Docstring Coverage by Module")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def main():
    mods, anomalies = collect_library()
    write_markdown(mods, anomalies, OUT_CI)
    write_markdown(mods, anomalies, OUT_DOCS)
    plot_docstring_coverage(mods, ROOT / "ci" / "docstring_coverage.png")
    print(f"Wrote audit to {OUT_CI}, {OUT_DOCS}, and coverage chart to ci/docstring_coverage.png")

