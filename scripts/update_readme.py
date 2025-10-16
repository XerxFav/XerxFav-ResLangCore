#!/usr/bin/env python3
import os
from datetime import datetime

README_PATH = "README.md"
PHASES = {
    "arca_core": "Базовые структуры, типы и фазовая модель",
    "arca_logic": "Тернарная логика, правила вывода и логические фреймворки",
    "arca_vm": "Виртуальная машина, исполнение фазовых инструкций"
}

def generate_phase_map():
    lines = ["## 🧭 Фазовая карта ArcaLang\n"]
    for name, desc in PHASES.items():
        lines.append(f"- **{name}** — {desc}")
    return "\n".join(lines)

def generate_make_targets():
    lines = ["## ⚙️ Цели Makefile\n"]
    targets = [
        "install", "test", "phase-build", "audit", "report",
        "ci", "docs", "verify-commits", "generate-make-phase", "update-readme"
    ]
    for t in targets:
        lines.append(f"- `make {t}` — {describe_target(t)}")
    return "\n".join(lines)

def describe_target(t):
    return {
        "install": "Установка зависимостей",
        "test": "Запуск тестов",
        "phase-build": "Сборка фазовых компонентов",
        "audit": "Фазовый аудит и diff_report.md",
        "report": "Генерация phase_report.md и SVG",
        "ci": "Полный CI-проход",
        "docs": "Сборка документации",
        "verify-commits": "Проверка фазовых меток",
        "generate-make-phase": "Автогенерация целей Makefile",
        "update-readme": "Обновление README и phase_report"
    }.get(t, "Описание отсутствует")

def main():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(README_PATH, "a") as f:
        f.write(f"\n---\n\n📅 Обновлено: {timestamp}\n\n")
        f.write(generate_phase_map())
        f.write("\n\n")
        f.write(generate_make_targets())
        f.write("\n")

if __name__ == "__main__":
    main()
