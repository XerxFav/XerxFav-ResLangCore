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
