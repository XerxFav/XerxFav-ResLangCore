# 
#      ___              _             _                 
#     /   \__ _ _ __ __| | __ _ _   _| | ___   __ _ ___ 
#    / /\ / _` | '__/ _` |/ _` | | | | |/ _ \ / _` / __|
#   / /_// (_| | | | (_| | (_| | |_| | | (_) | (_| \__ \
#  /___,' \__,_|_|  \__,_|\__,_|\__, |_|\___/ \__, |___/
#                               |___/         |___/     
#
# ArcaLang / Dutrimxord — Project Guide
#

## 🔧 Makefile Guide

### Основные цели
- **deps** — установка базовых зависимостей (core + viz) и утилит  
- **install-core / install-ml / install-viz / install-extras / install-all** — установка зависимостей по профилям  
- **sync-reqs** — синхронизация `requirements.txt` с полным набором  
- **install** — установка пакета в editable‑режиме  

### Качество и тестирование
- **test** — запуск unit‑тестов  
- **coverage** — отчёт покрытия кода  
- **lint / format** — проверка стиля и автоформатирование  

### Документация
- **doc** — генерация HTML‑документации  
- **serve-doc** — локальный сервер документации (порт 8080)  
- **clean-doc** — очистка артефактов документации  

### Аудит
- **audit** — фазовый аудит (`scripts/arca_phase_audit.py`)  
- **audit-lib** — аудит библиотеки (`scripts/arca_library_audit.py`) с проверкой docstring‑coverage (порог ≥80%)  

### CI/CD и разработка
- **ci** — полный цикл: очистка, зависимости, мосты, тесты, покрытие, документация, аудит. Артефакты сохраняются в `ci/artifacts/`  
- **dev** — режим разработки: авто‑перезапуск тестов и документации при изменении файлов  
- **all** — полный цикл без очистки  

### Сервисы и утилиты
- **serve** — запуск FastAPI‑приложения (`http://0.0.0.0:8000`)  
- **viz** — демонстрация визуализации (heatmap)  
- **cycle** — запуск менеджера фазовых переходов  

### Справка
- **help** — выводит список всех целей Makefile  

---

## 📊 CI Pipeline

Полный поток шагов при запуске `make ci`:

     deps → bridges-all → test → coverage → doc → audit → audit-lib → artifacts
     
     
- **deps** — установка зависимостей  
- **bridges-all** — сборка мостов  
- **test** — запуск unit‑тестов  
- **coverage** — отчёт покрытия кода  
- **doc** — генерация документации  
- **audit** — фазовый аудит  
- **audit-lib** — аудит библиотеки с проверкой docstring  
- **artifacts** — сохранение отчётов и графиков  

---

## ⚡ Quick Start

### 1. Установка зависимостей
```bash
make deps

#make test

#Запуск тестов
bash
make test
#Генерация документации
make doc
make serve-doc   # открыть локально на http://localhost:8080
#Полный CI/CD цикл
make ci

git add README.md git commit -m "Обновлен README.md: Makefile Guide + CI Pipeline + Quick Start + ASCII баннер" git push

## PhaseBit & QND_CONST — фазовые переходы

ArcaLang использует фазовую модель, основанную на трёх состояниях:

- **QND** — Quantum Nondemolition
- **PHASE** — Phase Tracking
- **ACT** — Active Execution

Переходы между режимами определяются значением `QND_CONST`:

| Условие | Режим |
|--------|-------|
| `PhaseBit.QND` и `QND_CONST < 1` | Stable nondemolition regime |
| `PhaseBit.PHASE` и `QND_CONST ≥ 1` | Phase amplification regime |
| `PhaseBit.ACT` и `QND_CONST > 10` | High-energy active regime |
| Иначе | Neutral regime |

График фазовых переходов автоматически генерируется в CI и доступен как артефакт.

Пример артефакта:  
`phase-transition-plot.png`  
(см. вкладку **Actions → Artifacts**)

#Карта зависимостей (финальная)metapysics_dependencies
00_intro_physys
 ├── 01_singular_physys
 ├── 02_adaptive_physys
 └── 03_interaction_physys
       ├── 04_phase_memory
       ├── 05_impedance_hysteresis
       ├── 06_resonance_node
       └── 07_phase_network
             ├── 08_phase_operators
             ├── 09_functors_categories
             └── 10_superposition
11_reslang_architecture
12_timeline_30aug

























 EOF
