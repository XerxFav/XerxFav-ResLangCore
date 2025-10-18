#!/bin/bash

echo "⮕ [phase-sync] Начинаю фазовую миграцию ArcaLang..."

# Фиксация изменений
# 🌐 Удалённые репозитории
GITHUB="https://github.com/XerxFav/XerxFav-ResLangCore"
CODEBERG="https://codeberg.org/XerxFav/XerxFav-ResLangCore"

# 📁 Локальный путь
LOCAL_REPO="$HOME/ResLang/ArcaLang"
cd "$LOCAL_REPO"

# 📜 Фазовая метка
PHASE_TAG="🧩 [phase:migration] $(date +%Y-%m-%d) Автоматическая синхронизация"

# 📂 Лог миграции
LOG_FILE="$LOCAL_REPO/ci/migration.log"
mkdir -p "$(dirname "$LOG_FILE")"

echo "🔁 Начинается фазовая миграция..." | tee -a "$LOG_FILE"

# 🧠 Фаза: автоматическое разрешение конфликтов
echo "🧠 Проверка на git-конфликты..." | tee -a "$LOG_FILE"
python3 scripts/resolve_phase_conflicts.py

# 📦 Добавление всех изменений
git add .
git commit -m "$PHASE_TAG" | tee -a "$LOG_FILE"


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

# 🚀 Пуш в оба репозитория
echo "⮕ [push] GitHub..." | tee -a "$LOG_FILE"
git push origin main | tee -a "$LOG_FILE"

echo "⮕ [push] Codeberg..." | tee -a "$LOG_FILE"
git push codeberg main | tee -a "$LOG_FILE"

#🧠 Фазовая подпись в phase_report.md
echo "$PHASE_TAG" > ci/phase_report.md
python3 scripts/ci_phase_report.py >> ci/phase_report.md


# 🧠 CI-отчёт
echo "⮕ [report] Генерация phase_report.md..." | tee -a "$LOG_FILE"
python3 scripts/ci_phase_report.py > ci/phase_report.md


# 📊 Diff-отчёт
echo "⮕ [diff] Сравнение структуры..." | tee -a "$LOG_FILE"
tree -L 3 "$LOCAL_REPO" > ci/current_tree.txt
diff ci/current_tree.txt ci/tree_snapshot.txt > ci/diff_report.md

# 📈 Визуализация фазовой синхронизации
echo "⮕ [svg] Генерация ci_phase_map.svg..." | tee -a "$LOG_FILE"
python3 scripts/generate_phase_svg.py

# 📦 Коммит отчётов
git add ci/phase_report.md ci/diff_report.md ci/ci_phase_map.svg
git commit -m "📜 [phase:report] CI и diff отчёты обновлены" | tee -a "$LOG_FILE"
git push origin main | tee -a "$LOG_FILE"
git push codeberg main | tee -a "$LOG_FILE"

echo "✅ Миграция завершена: $(date)" | tee -a "$LOG_FILE"

eef0aa1 (🧩 [phase:migration] 2025-10-10 Автоматическая синхронизация)


if ! git remote | grep -q codeberg; then        #1. 🔐 Проверка remotes перед пушем
  git remote add codeberg "$CODEBERG"
fi

#📁 Снимок дерева перед сравнением

if [ ! -f ci/tree_snapshot.txt ]; then
  cp ci/current_tree.txt ci/tree_snapshot.txt
fi

#🧪 Проверка успешности коммита

if git diff --cached --quiet; then
  echo "⚠️ Нет изменений для коммита." | tee -a "$LOG_FILE"
else
  git commit -m "$PHASE_TAG" | tee -a "$LOG_FILE"
fi




































































<<<<<<< HEAD
>>>>>>> 163a223 (🧩 [phase:migration] 2025-10-16 Автоматическая синхронизация)
=======
=======
# Сравнение структуры
echo "⮕ [diff] Сравнение с предыдущим snapshot..."
tree -L 3 ~/ResLang/ArcaLang > ci/current_tree.txt
diff ci/current_tree.txt tree_snapshot.txt > ci/diff_report.md

# Добавление отчёта в коммит
git add ci/diff_report.md
git commit -m "phase: $(date +%Y-%m-%d) diff_report updated"

echo "✅ [done] Миграция завершена, отчёты обновлены."
>>>>>>> c77e847 (phase: 2025-10-03 structural sync)
>>>>>>> 7c633fc (phase: 2025-10-03 structural sync)
