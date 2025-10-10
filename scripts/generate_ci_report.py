
import datetime, os
from pathlib import Path



 eef0aa1 (🧩 [phase:migration] 2025-10-10 Автоматическая синхронизация)
from pathlib import Path
import datetime
import yaml

# 📁 Путь к фазам
phases_dir = Path("phases")

# 📜 Заголовок фазового индекса
index = "# 🧭 ArcaLang: Фазовый индекс\n\n"
index += f"**Дата генерации**: {datetime.datetime.now().date()}\n\n"

# 🔍 Обход фаз
for phase in sorted(phases_dir.iterdir()):
	mig_file = phase / "migration.yaml"
	if mig_file.exists():
	data = yaml.safe_load(mig_file.read_text(encoding="utf-8"))
	index += f"## 🔹 Фаза: `{phase.name}`\n"
	index += f"- **Происхождение**: `{data.get('source', '—')}`\n"
	index += f"- **evolves_from**: `{data.get('evolves_from', '—')}`\n"
	index += f"- **Описание**: {data.get('notes', '—')}\n"
	index += f"- **README**: [phases/{phase.name}/README.md](../../phases/{phase.name}/README.md)\n\n"

# 💾 Сохранение отчёта
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
<<<<<<< HEAD
=======
"""
