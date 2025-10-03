#!/bin/bash
# 🧬 Автоматизированный фазовый ребейс

echo "🔄 Фазовый ребейс: подтягиваем origin/main..."
git fetch origin main

echo "🧠 Проверка на незакоммиченные изменения..."
if ! git diff-index --quiet HEAD --; then
  echo "⚠️ Есть незакоммиченные изменения. Сначала сделай коммит или stash."
  exit 1
fi

echo "📐 Выполняем ребейс..."
git rebase origin/main

if [ $? -eq 0 ]; then
  echo "✅ Ребейс завершён. Готов к фазовому пушу."
else
  echo "❌ Конфликт при ребейсе. Разреши вручную и запусти: git rebase --continue"
fi
