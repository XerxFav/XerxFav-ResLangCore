# ArcaLangLib Specification

`arca_langlib` — это стандартная библиотека ArcaLang, включающая:

- **types/** — базовые типы данных и фазовые структуры
- **utils/** — утилиты для фаз, хронополя, заголовков
- **runtime/** — рантайм-интерпретатор, память, агенты
- **templates/** — шаблоны фаз, агентов, миграций

## Пример использования

```python
from arca_langlib.runtime.interpreter import evaluate

result = evaluate("hello", {})
print(result)  # <string:HELLO>

---

## 🚀 Что делать дальше

1. **Создай структуру каталогов и файлов**, как указано выше.
2. **Перенеси существующие модули** (`phase_types.py`, `chronotope.py`, `headers.py`) в `types/` и `utils/`.
3. **Добавь шаблоны YAML** в `templates/` — можно использовать текущие `arca-phase.yml` как основу.
4. **Разработай документацию** в `langlib_spec.md` — описание API, примеры, схемы.
5. **Интегрируй `arca_langlib` в `arca_core` и `evaluator.py`**, чтобы использовать типы и утилиты из одного места.

---

## Использование шаблонов

```python
from arca_langlib.templates import load_phase_template

template = load_phase_template("phase_template.yaml")
print(template["phase"]["name"])


---

### 6. 🔗 Интеграция
- Импортируй `arca_langlib` в `arca_core`, `evaluator.py`, `phase_agent`.
- Используй `ArcaValue`, `PhaseSignature`, `MemoryStore` как стандартные компоненты.

---

---

## 🧠 Модуль `memory.py`

Предоставляет интерфейс для хранения и извлечения данных фаз.

```python
from arca_langlib.runtime.memory import MemoryStore

mem = MemoryStore()
mem.save("key", 42)
mem.load("key")  # → 42

## Пример: PhaseSignature

```python
from arca_langlib.types.phase_types import PhaseSignature

sig = PhaseSignature("example", [("input1", "string")], [("result", "int")])
print(sig.describe())
