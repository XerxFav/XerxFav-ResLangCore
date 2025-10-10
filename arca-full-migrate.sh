#!/bin/bash

echo "⮕ [phase-sync] Начинаю фазовую миграцию ArcaLang..."

<<<<<<< HEAD
# Фиксация изменений

# 📁 Локальный путь
LOCAL_REPO="$HOME/ResLang/ArcaLang"
cd "$LOCAL_REPO"

# 📜 Фазовая метка
PHASE_TAG="🧩 [phase:migration] $(date +%Y-%m-%d) Автоматическая синхронизация"

# 📂 Лог миграции
LOG_FILE="$LOCAL_REPO/ci/migration.log"
mkdir -p "$(dirname "$LOG_FILE")"

echo "🔁 Начинается фазовая миграция..." | tee -a "$LOG_FILE"

# 📦 Добавление всех изменений
 eef0aa1 (🧩 [phase:migration] 2025-10-10 Автоматическая синхронизация)
git add .
git commit -m "phase: $(date +%Y-%m-%d) structural sync"

HEAD
# Публикация на GitHub
echo "⮕ [push] Отправка в GitHub..."
git push origin main

# Публикация на Codeberg
echo "⮕ [push] Отправка в Codeberg..."
git push codeberg main

# Генерация фазового отчёта
echo "⮕ [report] Генерация phase_report.md..."
python3 scripts/ci_phase_report.py > ci/phase_report.md

# Сравнение структуры
echo "⮕ [diff] Сравнение с предыдущим snapshot..."
tree -L 3 ~/ResLang/ArcaLang > ci/current_tree.txt
diff ci/current_tree.txt tree_snapshot.txt > ci/diff_report.md

# Добавление отчёта в коммит
git add ci/diff_report.md
git commit -m "phase: $(date +%Y-%m-%d) diff_report updated"

echo "✅ [done] Миграция завершена, отчёты обновлены."

# 🚀 Пуш в GitHub и Codeberg
echo "⮕ [push] GitHub..."
git push origin main | tee -a "$LOG_FILE"
echo "⮕ [push] Codeberg..."
git push codeberg main | tee -a "$LOG_FILE"

# 🧠 CI-отчёт
echo "⮕ [report] Генерация phase_report.md..."
python3 scripts/ci_phase_report.py > ci/phase_report.md

# 📊 Diff-отчёт
echo "⮕ [diff] Сравнение структуры..."
tree -L 3 "$LOCAL_REPO" > ci/current_tree.txt
diff ci/current_tree.txt ci/tree_snapshot.txt > ci/diff_report.md

# 📦 Коммит отчётов
git add ci/phase_report.md ci/diff_report.md
git commit -m "📜 [phase:report] Обновлены phase_report и diff_report" | tee -a "$LOG_FILE"
git push origin main | tee -a "$LOG_FILE"
git push codeberg main | tee -a "$LOG_FILE"

echo "✅ Миграция завершена: $(date)" | tee -a "$LOG_FILE"
eef0aa1 (🧩 [phase:migration] 2025-10-10 Автоматическая синхронизация)
