
from pathlib import Path
from pathlib import Path

import datetime, os
import yaml

phases_dir = Path("phases")
index = "# 🧭 ArcaLang: Фазовый индекс\n\n"
index += f"**Дата генерации**: {datetime.datetime.now().date()}\n\n"

for phase in sorted(phases_dir.iterdir()):
    mig_file = phase / "migration.yaml"
    if mig_file.exists():
        data = yaml.safe_load(mig_file.read_text(encoding="utf-8"))
        index += f"## 🔹 Фаза: `{phase.name}`\n"
        index += f"- **Происхождение**: `{data['source']}`\n"
        index += f"- **evolves_from**: `{data['evolves_from']}`\n"
        index += f"- **Описание**:   {data['notes']}\n"
        index += f"- **README**: [phases/{phase.name}/README.md](../../phases/{phase.name}/README.md)\n\n"

Path("docs/ci/phase_index.md").write_text(index, encoding="utf-8")
print("✅ Фазовый индекс синхронизирован.")

# README структура
structure = """## 🧭 Фазовая структура проекта ArcaLang
```text
ResLang/
├── arca_core/        # 🔢 [Logical]
├── arca_fieldcore/   # 🧩 [Ontological]
├── arca_interpreter/ # 🧬 [Quantum]
├── arca_memory/      # 📦 [Memory]
├── docs/             # 📜 [Docs]
├── tests/            # 🧪 [Test]
├── scripts/          # ⚙️ [CI]
└── .github/workflows # ⚙️ [CI]
"""
