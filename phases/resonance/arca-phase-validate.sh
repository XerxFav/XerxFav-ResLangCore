#!/bin/bash
set -e

echo "🔍 Валидация фазы 'resonance'..."

META_FILE="phases/resonance/arca-phase.yml"
EVOLVED_FROM=$(yq '.phase.evolves_from' "$META_FILE")
PUSHED=$(yq '.phase.pushed' "$META_FILE")

if [ -z "$EVOLVED_FROM" ]; then
  echo "❌ evolves_from не указан"
  exit 1
fi

if [ "$PUSHED" != "true" ]; then
  echo "❌ pushed должен быть true"
  exit 1
fi

echo "✅ Валидация пройдена"
