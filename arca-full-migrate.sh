#!/bin/bash

echo "⮕ [phase-sync] Начинаю фазовую миграцию ArcaLang..."

# Фиксация изменений
git add .
git commit -m "phase: $(date +%Y-%m-%d) structural sync"

# Публикация на GitHub
echo "⮕ [push] Отправка в GitHub..."
git push origin main

# Публикация на Codeberg
echo "⮕ [push] Отправка в Codeberg..."
git push codeberg main

# Генерация фазового отчёта
echo "⮕ [report] Генерация phase_report.md..."
python3 scripts/ci_phase_report.py > ci/phase_report.md

echo "✅ [done] Миграция завершена."
