/home/arca/ResLang/ArcaLang/
├── phase_agent/
│   ├── __init__.py
│   ├── agent.py          # Python-код CI-агента
│   ├── phase_log.yaml    # YAML-логи включения
│   ├── assets/
│   │   └── ci_agent.svg  # SVG-графика
│   └── README.md         # Доктрина CI-агента

## Phase Inclusion System
CI-агент реализует фазовую селекцию объектов по метрике включения:
- Локальная ёмкость: ψ₀obj
- Глобальный потенциал: Ψglob
- Ускорение: ω
- Плотность: ρ

Логика включения: ψ₀obj / Ψglob ≥ ρ · ω

## 🔁 Автоматизация миграций

Скрипт `scripts/arca_phase_migrate.py` обеспечивает перенос фазовых объектов между ArcaLang и ResLangCore, фиксируя каждый акт в `phase_log.yaml`.
## 🧪 Примеры использования

### 1. Проверка включения объекта

```python
from agent import PhaseAgent

agent = PhaseAgent(psi_obj=0.82, psi_glob=1.45, omega=0.12, rho=0.09)
print(agent.act())
![Phase Map](assets/phase_map.svg)

