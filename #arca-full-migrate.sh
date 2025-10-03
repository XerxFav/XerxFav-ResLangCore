#!/bin/bash
# 📦 Полная фазовая миграция из XerxFav-ResLangCore → ArcaLang с генерацией README

SRC="$HOME/ResLang/ArcaLang/XerxFav-ResLangCore"
DST="$HOME/ResLang/ArcaLang"
DATE=$(date +"%Y-%m-%d")
rsync -av reslang_core/ "$TARGET_REPO/reslang_core/"

echo "🔧 Создание фазовых каталогов..."
mkdir -p "$DST/phases/stabilization"
mkdir -p "$DST/phases/field"
mkdir -p "$DST/phases/interpreter"
mkdir -p "$DST/phases/memory"
mkdir -p "$DST/docs/spec"
mkdir -p "$DST/docs/legacy"
mkdir -p "$DST/docs/ci"
mkdir -p "$DST/scripts/ci"
mkdir -p "$DST/tests/stabilization"

echo "📄 Копирование спецификаций → docs/spec"
[ -f "$SRC/arca_lang_spec.md" ] && cp "$SRC/arca_lang_spec.md" "$DST/docs/spec/"
[ -f "$SRC/specification.md" ] && cp "$SRC/specification.md" "$DST/docs/spec/"
[ -f "$SRC/ontology.md" ] && cp "$SRC/ontology.md" "$DST/docs/spec/"


echo "📁 Копирование модулей ядра → stabilization"
cp "$SRC/arca_core/"*.py "$DST/phases/stabilization/"
echo "📝 Генерация README → stabilization"
cat <<EOF > "$DST/phases/stabilization/README.md"
# Фаза: stabilization

**Происхождение**: Модули перенесены из \`XerxFav-ResLangCore/arca_core\`  
**Дата миграции**: $DATE  
**Назначение**: Базовые компоненты ядра ArcaLang  
**Фиксация**: phase=stabilization, evolves_from=origin
EOF

echo "📁 Копирование fieldcore → field"
cp "$SRC/arca_fieldcore/"*.py "$DST/phases/field/"
echo "📝 Генерация README → field"
cat <<EOF > "$DST/phases/field/README.md"
# Фаза: field

**Происхождение**: Модули перенесены из \`XerxFav-ResLangCore/arca_fieldcore\`  
**Дата миграции**: $DATE  
**Назначение**: Генерация онтологий, схем, fieldmap  
**Фиксация**: phase=field, evolves_from=stabilization
EOF

echo "📁 Копирование интерпретатора → interpreter"
cp "$SRC/arca_interpreter/"*.py "$DST/phases/interpreter/"
echo "📝 Генерация README → interpreter"
cat <<EOF > "$DST/phases/interpreter/README.md"
# Фаза: interpreter

**Происхождение**: Модули перенесены из \`XerxFav-ResLangCore/arca_interpreter\`  
**Дата миграции**: $DATE  
**Назначение**: Оценка выражений, интерпретация  
**Фиксация**: phase=interpreter, evolves_from=field
EOF

echo "📁 Копирование памяти → memory"
cp "$SRC/arca_memory/"*.py "$DST/phases/memory/"
echo "📝 Генерация README → memory"
cat <<EOF > "$DST/phases/memory/README.md"
# Фаза: memory

**Происхождение**: Модули перенесены из \`XerxFav-ResLangCore/arca_memory\`  
**Дата миграции**: $DATE  
**Назначение**: Хранилище, фазовая память  
**Фиксация**: phase=memory, evolves_from=interpreter
EOF

echo "📄 Копирование спецификаций → docs/spec"
cp "$SRC/arca_lang_spec.md" "$DST/docs/spec/"
cp "$SRC/specification.md" "$DST/docs/spec/"
cp "$SRC/ontology.md" "$DST/docs/spec/"

echo "📄 Копирование исторических описаний → docs/legacy"
cp "$SRC/"*.txt "$DST/docs/legacy/"
cp "$SRC/README.md" "$DST/docs/legacy/"
cp "$SRC/LICENSE" "$DST/docs/legacy/"

echo "🗺️ Копирование SVG и Makefile → docs/ci"
cp "$SRC/docs/ci_phase_map.svg" "$DST/docs/ci/"
cp "$SRC/docs/Makefile" "$DST/docs/ci/"
cp "$SRC/docs/make.bat" "$DST/docs/ci/"

echo "🧪 Копирование тестов → tests/stabilization"
cp "$SRC/tests/"test_*.py "$DST/tests/stabilization/"

echo "⚙️ Копирование CI-скриптов → scripts/ci"
cp "$SRC/scripts/"*.py "$DST/scripts/ci/"
cp "$SRC/scripts/"*.dot "$DST/scripts/ci/"

declare -A PHASES
PHASES[stabilization]="origin"
PHASES[field]="stabilization"
PHASES[interpreter]="field"
PHASES[memory]="interpreter"

echo "🔧 Создание фазовых каталогов..."
for PHASE in "${!PHASES[@]}"; do
  mkdir -p "$DST/phases/$PHASE"
done

mkdir -p "$DST/docs/spec" "$DST/docs/legacy" "$DST/docs/ci"
mkdir -p "$DST/scripts/ci" "$DST/tests/stabilization"

echo "📁 Копирование и генерация README + arca-phase.yml..."
for PHASE in "${!PHASES[@]}"; do
  case $PHASE in
    stabilization) cp "$SRC/arca_core/"*.py "$DST/phases/$PHASE/" ;;
    field) cp "$SRC/arca_fieldcore/"*.py "$DST/phases/$PHASE/" ;;
    interpreter) cp "$SRC/arca_interpreter/"*.py "$DST/phases/$PHASE/" ;;
    memory) cp "$SRC/arca_memory/"*.py "$DST/phases/$PHASE/" ;;
  esac

  echo "📝 README → $PHASE"
  cat <<EOF > "$DST/phases/$PHASE/README.md"
# Фаза: $PHASE

**Происхождение**: Модули перенесены из \`XerxFav-ResLangCore/$PHASE\`  
**Дата миграции**: $DATE  
**Назначение**: Автоматически сгенерировано  
**Фиксация**: phase=$PHASE, evolves_from=${PHASES[$PHASE]}
EOF

  echo "📄 arca-phase.yml → $PHASE"
  cat <<EOF > "$DST/phases/$PHASE/arca-phase.yml"
phase:
  name: $PHASE
  desc: Автоматически сгенерировано на основе миграции $DATE
  tags: [migrated, $PHASE]
  evolves_from: ${PHASES[$PHASE]}
  pushed: true
EOF
done

echo "📄 Копирование спецификаций → docs/spec"


[ -f "$SRC/arca_lang_spec.md" ] && cp "$SRC/arca_lang_spec.md" "$DST/docs/spec/"
[ -f "$SRC/specification.md" ] && cp "$SRC/specification.md" "$DST/docs/spec/"
[ -f "$SRC/ontology.md" ] && cp "$SRC/ontology.md" "$DST/docs/spec/"

cp "$SRC/arca_lang_spec.md" "$DST/docs/spec/"
cp "$SRC/specification.md" "$DST/docs/spec/"
cp "$SRC/ontology.md" "$DST/docs/spec/"

echo "📄 Копирование исторических описаний → docs/legacy"
cp "$SRC/"*.txt "$DST/docs/legacy/"
cp "$SRC/README.md" "$DST/docs/legacy/"
cp "$SRC/LICENSE" "$DST/docs/legacy/"

echo "🗺️ Копирование SVG и Makefile → docs/ci"
cp "$SRC/docs/ci_phase_map.svg" "$DST/docs/ci/"
cp "$SRC/docs/Makefile" "$DST/docs/ci/"
cp "$SRC/docs/make.bat" "$DST/docs/ci/"

echo "🧪 Копирование тестов → tests/stabilization"
cp "$SRC/tests/"test_*.py "$DST/tests/stabilization/"

echo "⚙️ Копирование CI-скриптов → scripts/ci"
cp "$SRC/scripts/"*.py "$DST/scripts/ci/"
cp "$SRC/scripts/"*.dot "$DST/scripts/ci/"

echo "🗺️ Генерация SVG-карты фаз → docs/ci/arca_phase_map.svg"
python3 - <<EOF
import graphviz

phases = ["stabilization", "field", "interpreter", "memory"]
edges = {
    "stabilization": "origin",
    "field": "stabilization",
    "interpreter": "field",
    "memory": "interpreter"
}

dot = graphviz.Digraph(comment="Arca Phase Map")
for phase in phases:
    dot.node(phase)
for child, parent in edges.items():
    dot.edge(parent, child, label="evolves_from")
dot.render("$DST/docs/ci/arca_phase_map", format="svg")
EOF

echo "✅ Миграция завершена. README, arca-phase.yml и SVG-карта созданы."

echo "🧾 Генерация фазового CI-отчёта → docs/ci/phase_index.md"
REPORT="$DST/docs/ci/phase_index.md"
echo "# 🧭 ArcaLang: Фазовый индекс" > "$REPORT"
echo "**Дата генерации**: $DATE" >> "$REPORT"
echo "" >> "$REPORT"

for PHASE in "${!PHASES[@]}"; do
  DESC=$(grep 'desc:' "$DST/phases/$PHASE/arca-phase.yml" | sed 's/desc: //')
  echo "## 🔹 Фаза: \`$PHASE\`" >> "$REPORT"
  echo "- **Происхождение**: \`XerxFav-ResLangCore/$PHASE\`" >> "$REPORT"
  echo "- **evolves_from**: \`${PHASES[$PHASE]}\`" >> "$REPORT"
  echo "- **Описание**: $DESC" >> "$REPORT"
  echo "- **README**: [phases/$PHASE/README.md](../../phases/$PHASE/README.md)" >> "$REPORT"
  echo "" >> "$REPORT"
done

echo "✅ CI-отчёт создан: docs/ci/phase_index.md"
