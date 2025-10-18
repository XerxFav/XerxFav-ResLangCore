

# 🔍 Phase Diff Report — ArcaLang

**Дата анализа:** 2025-10-03  
**Фаза:** `manifest-refactor`  
**Автор:** Arctur + Copilot

---

## 🧠 Цель

Сравнить текущую структуру `ArcaLang` с сохранённым снимком `tree_snapshot.txt`, выявить изменения, перемещения, консолидации и удалённые артефакты.

---

## 📦 Структурные изменения

### 🔄 Перемещено

| Было в `tree_snapshot.txt`         | Стало в `ArcaLang`                  | Статус       |
|------------------------------------|-------------------------------------|--------------|
| `reslang_core/`                    | `arca_core/reslang/`               | ✅ Перенесено |
| `arca_memory/`                     | `arca_core/arca_memory/`           | ✅ Перенесено |
| `arca_fieldcore/`                  | `arca_core/arca_fieldcore/`        | ✅ Перенесено |
| `arca_interpreter/`               | `arca_core/arca_interpreter/`      | ✅ Перенесено |
| `phase_agent/`                     | `arca_core/phase_agent/`           | ✅ Перенесено |
| `scripts/`                         | `scripts/`                          | ✅ Сохранено |
| `tests/`                           | `tests/`                            | ✅ Сохранено |

---

### 🧾 Документация

| Артефакт                           | Новое расположение                  | Статус       |
|-----------------------------------|-------------------------------------|--------------|
| `arca_lang_spec.md`               | `docs/arca_lang_spec.md`            | ✅ Перенесено |
| `ontology.md`                     | `docs/ontology.md`                  | ✅ Перенесено |
| `Project_structure.txt`           | `docs/Project_structure.txt`        | ✅ Перенесено |
| `repo_structure.txt`              | `docs/repo_structure.txt`           | ✅ Перенесено |
| `🧠 Текущая структура ArcaLang`   | `docs/🧠 Текущая структура ArcaLang`| ✅ Перенесено |
| `**Закоммить и запушь**:.txt`     | `docs/Закоммить и запушь.txt`       | ✅ Перенесено |
| `README.md`                       | `README.md`                         | 🔄 Обновлено |
| `Makefile`                        | `Makefile`                          | 🔄 Переписано |

---

### 🧪 CI и фазовая инфраструктура

| Компонент                  | Статус       | Комментарий |
|---------------------------|--------------|-------------|
| `ci_phase_map.svg`        | ✅ Обновлено  | Визуализирует фазовую структуру |
| `phase_report.md`         | ✅ Генерируется | Через `generate_ci_report.py` |
| `arca-full-migrate.sh`    | ✅ Расширено  | Включает push, CI, diff |
| `generate_docs.py`        | ✅ Синхронизировано | В `scripts/` и `docs/source/` |

---

### 🧹 Удалено / Объединено

- `XerxFav-ResLangCore/` — полностью удалён
- `.git/` — удалён, история объединена
- `legacy/` — создан для хранения старых артефактов

---

## ✅ Вывод

Структура ArcaLang полностью онтологически собрана. Все модули, фазы, CI и документация перенесены, переписаны или синхронизированы. Проект готов к фазе `phase-indexing`, публикации и CI-автоматизации.

### ✅ Добавлен ternary.hpp
- Фазовая логика: ternary_state, ternary_eval
- Точность: Boost.Multiprecision
- Местоположение: arca_core_phase2/include
 163a223 (🧩 [phase:migration] 2025-10-16 Автоматическая синхронизация)

1,226d0
< /home/arca/ResLang/ArcaLang
< ├── arca_core
< │   ├── arca_fieldcore
< │   │   ├── fieldmap.py
< │   │   ├── generate_ontology.py
< │   │   ├── generator.py
< │   │   └── schema.py
< │   ├── arca_interpreter
< │   │   └── evaluator.py
< │   ├── arca_memory
< │   │   └── storage.py
< │   ├── chronotope.py
< │   ├── headers.py
< │   ├── phase1
< │   │   ├── chronotope.py
< │   │   ├── phase_types.py
< │   │   └── phase_utils.py
< │   ├── phase_agent
< │   │   ├── agent.py
< │   │   ├── assets
< │   │   ├── Copilot_20250927_105817.png
< │   │   ├── phase_log.yaml
< │   │   ├── phase_map.svg
< │   │   ├── phase_map.yaml
< │   │   ├── README.md
< │   │   └── XerxFav-ResLangCore -> /home/arca/ResLang/ArcaLang/XerxFav-ResLangCore
< │   ├── phase.py
< │   ├── __pycache__
< │   │   ├── chronotope.cpython-313.pyc
< │   │   └── phase.cpython-313.pyc
< │   ├── reslang
< │   │   ├── docs
< │   │   ├── include
< │   │   ├── #Makefile#
< │   │   ├── Makefile
< │   │   ├── Project_structure.txt
< │   │   ├── reslang
< │   │   ├── src
< │   │   └── tests
< │   ├── ResLang.code-workspace
< │   └── src
< │       ├── phase_types.cpp
< │       └── phase_utils.cpp
< ├── #arca-full-migrate.sh
< ├── #arca-full-migrate.sh#
< ├── arca-full-migrate.sh
< ├── arca_lang_spec.md
< ├── ci
< │   ├── current_tree.txt
< │   ├── diff_report.md
< │   ├── migration.log
< │   ├── phase_report.md
< │   └── tree_snapshot.txt
< ├── ci_phase_map.svg
< ├── ci_phase_map.svg.svg
< ├── CONTRIBUTING.md
< ├── docs
< │   ├── arca_lang_spec.md
< │   ├── ci
< │   │   ├── ci_phase_map.svg
< │   │   └── phase_index.md
< │   ├── coverage.txt
< │   ├── Current structure of Arcalang.txt
< │   ├── legacy
< │   │   ├── coverage.txt
< │   │   ├── Current structure of Arcalang.txt
< │   │   ├── LICENSE
< │   │   ├── phase_report.md
< │   │   ├── Project_structure.txt
< │   │   ├── README.md
< │   │   ├── repo_structure.txt
< │   │   ├── requirements.txt
< │   │   └── **Закоммить и запушь**:.txt
< │   ├── make.bat
< │   ├── Makefile
< │   ├── migration.log
< │   ├── ontology.md
< │   ├── Project_structure.txt
< │   ├── repo_structure.txt
< │   ├── source
< │   │   ├── conf.py
< │   │   ├── generate_docs.py
< │   │   ├── index.rst
< │   │   └── _static
< │   ├── spec
< │   │   ├── arca_lang_spec.md
< │   │   └── ontology.md
< │   ├── specification.md
< │   ├── The current structure of Arcalang
< │   ├── **Закоммить и запушь**:.txt
< │   └── 🧠 Текущая структура ArcaLang
< ├── htmlcov
< │   ├── class_index.html
< │   ├── coverage_html_cb_6fb7b396.js
< │   ├── favicon_32_cb_58284776.png
< │   ├── function_index.html
< │   ├── index.html
< │   ├── keybd_closed_cb_ce680311.png
< │   ├── status.json
< │   ├── style_cb_6b508a39.css
< │   ├── z_41d1b73d29037bb8_chronotope_py.html
< │   └── z_41d1b73d29037bb8_phase_py.html
< ├── LICENSE
< ├── Makefile
< ├── Makefile.phases
< ├── phase_agent
< │   ├── agent.py
< │   ├── ci_agent.svg
< │   ├── phase_log.yaml
< │   └── README.md
< ├── phase_report.md
< ├── phases
< │   ├── arca-phase.yml
< │   ├── field
< │   │   ├── arca-phase.yml
< │   │   ├── fieldmap.py
< │   │   ├── generate_ontology.py
< │   │   ├── generator.py
< │   │   ├── migration.yaml
< │   │   ├── README.md
< │   │   └── schema.py
< │   ├── interpreter
< │   │   ├── arca-phase.yml
< │   │   ├── evaluator.py
< │   │   ├── migration.yaml
< │   │   └── README.md
< │   ├── memory
< │   │   ├── arca-phase.yml
< │   │   ├── migration.yaml
< │   │   ├── README.md
< │   │   └── storage.py
< │   ├── migration.yaml
< │   ├── resonance
< │   │   ├── arca-phase.py
< │   │   ├── arca-phase-validate.sh
< │   │   ├── arca-phase.yml
< │   │   └── migration.yaml
< │   └── stabilization
< │       ├── arca-phase.yml
< │       ├── chronotope.py
< │       ├── chronotope.py,cover
< │       ├── headers.py
< │       ├── migration.yaml
< │       ├── phase.py
< │       ├── phase.py,cover
< │       └── README.md
< ├── phase_types.o
< ├── phase_utils.o
< ├── README.md
< ├── requirements.txt
< ├── ResLang -> /home/arca/ResLang
< ├── scripts
< │   ├── arca_phase_audit.py
< │   ├── arca_phase_migrate.py
< │   ├── ci
< │   │   ├── ci_phase_map.dot
< │   │   ├── docs
< │   │   ├── generate_ci_report.py
< │   │   ├── generate_docs.py
< │   │   └── generate_phase_svg.py
< │   ├── ci_phase_map.dot
< │   ├── ci_phase_report.py
< │   ├── generate_ci_report.py
< │   ├── generate_docs.py
< │   ├── gen_make_phases.py
< │   ├── legacy_migrate.sh
< │   ├── Makefile.phases
< │   ├── phase_rebase.sh
< │   ├── resci.py
< │   ├── resdoc.py
< │   └── update_readme.py
< ├── test_core
< ├── tests
< │   ├── arca_core_phase1
< │   │   └── test_phase_types.py
< │   ├── arca_core_phase2
< │   │   ├── test_phase_types.cpp
< │   │   ├── test_phase_utils.cpp
< │   │   ├── test_ternary.cpp
< │   │   └── Новый файл
< │   ├── gen_make_phases.py
< │   ├── __pycache__
< │   │   └── test_chronotope.cpython-313-pytest-8.4.2.pyc
< │   ├── ResLang -> /home/arca/ResLang
< │   ├── stabilization
< │   │   ├── test_chronotope.py
< │   │   ├── test_evaluator.py
< │   │   ├── test_generator.py
< │   │   ├── test_headers.py
< │   │   ├── test_phase.py
< │   │   ├── test_scenario.py
< │   │   ├── test_schema.py
< │   │   └── test_storage.py
< │   ├── test_chronotope.py
< │   ├── test_evaluator.py
< │   ├── test_generator.py
< │   ├── test_headers.py
< │   ├── test_phase.py
< │   ├── test_scenario.py
< │   ├── test_schema.py
< │   └── test_storage.py
< ├── test_utils
< ├── token.txt
< ├── venv
< │   ├── bin
< │   │   ├── activate
< │   │   ├── activate.csh
< │   │   ├── activate.fish
< │   │   ├── Activate.ps1
< │   │   ├── pip
< │   │   ├── pip3
< │   │   ├── pip3.13
< │   │   ├── python -> python3
< │   │   ├── python3 -> /usr/bin/python3
< │   │   └── python3.13 -> python3
< │   ├── include
< │   │   └── python3.13
< │   ├── lib
< │   │   └── python3.13
< │   ├── lib64 -> lib
< │   └── pyvenv.cfg
< ├── woodpecker
< │   └── docker-compose.yml
< └── 🧭 Стандартизированные фазовые метки для коммитов.txt
< 
< 48 directories, 176 files
 19fda02 (🧩 [phase:migration] 2025-10-18 Автоматическая синхронизация)
