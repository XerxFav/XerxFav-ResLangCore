#!/bin/bash

# 🌐 Удалённые репозитории
GITHUB="https://github.com/XerxFav/XerxFav-ResLangCore"
CODEBERG="https://codeberg.org/XerxFav/XerxFav-ResLangCore"

# 📁 Локальный путь
LOCAL_REPO="$HOME/ResLang/ArcaLang/XerxFav-ResLangCore"

# 📜 Фазовая метка
PHASE_TAG="🧩 [phase:migration] Автоматическая синхронизация репозиториев"

# 📂 Лог миграции
LOG_FILE="$LOCAL_REPO/migration.log"

echo "🔁 Начинается фазовая миграция..." | tee -a "$LOG_FILE"
cd "$LOCAL_REPO"

# 📦 Добавление всех изменений
git add .
git commit -m "$PHASE_TAG" | tee -a "$LOG_FILE"

# 🚀 Пуш в GitHub и Codeberg
git push origin main | tee -a "$LOG_FILE"
git push codeberg main | tee -a "$LOG_FILE"

echo "✅ Миграция завершена: $(date)" | tee -a "$LOG_FILE"

python3 "$LOCAL_REPO/scripts/resci.py"
