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



























 EOF
