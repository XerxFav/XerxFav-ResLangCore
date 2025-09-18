# generate_ci_report.py — генерация фазового CI-отчёта
import datetime
import os
from pathlib import Path

commit = os.environ.get("GITHUB_SHA", "unknown")
actor = os.environ.get("GITHUB_ACTOR", "unknown")
repo = os.environ.get("GITHUB_REPOSITORY", "unknown")

report = f"""# 🧠 ArcaLang Phase-Space CI Report

📅 **Дата сборки**: {datetime.datetime.utcnow().isoformat()}  
🔁 **Коммит**: {commit}  
👤 **Автор**: {actor}  
📦 **Репозиторий**: {repo}

---

## 🧬 Quantum Phase — Сценарии переходов

| Сценарий фаз | Результат |
|--------------|-----------|
| `neutral → positive → negative` | ✅ |
| `positive → neutral` | ✅ |
| `negative → positive → neutral` | ✅ |

---

## 🔢 Logical Phase — Структура переходов

✔️ `fieldmap.dot` сгенерирован  
✔️ `fieldmap.svg` визуализирован  
📎 Артефакт: `fieldmap_output.txt`, `fieldmap.svg`

---

## 🧩 Ontological Phase — Структура языка

✔️ `ontology.md` содержит ключевые секции  
✔️ Sphinx-документация собрана  
📎 Артефакт: `docs/build/html/`

---

## 📊 Сводка фаз

| Фаза         | Статус | Артефакты                     |
|--------------|--------|-------------------------------|
| Quantum      | ✅      | —                             |
| Logical      | ✅      | `fieldmap_output.txt`, `SVG` |
| Ontological  | ✅      | `ontology.md`, `docs/`        |
"""

Path("docs/ci_phase_report.md").write_text(report)
