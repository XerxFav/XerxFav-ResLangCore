| Модуль | Зависит от | Порождает |
|--------|-------------|-----------|
| 00_intro_physys | — | 01, 02, 03 |
| 01_singular_physys | 00 | 03, 06 |
| 02_adaptive_physys | 00 | 03, 05 |
| 03_interaction_physys | 01, 02 | 04, 05, 06, 07 |
| 04_phase_memory | 03 | 07 |
| 05_impedance_hysteresis | 02, 03 | 07 |
| 06_resonance_node | 01, 03 | 07 |
| 07_phase_network | 03, 04, 05, 06 | 08, 09, 10 |
| 08_phase_operators | 07 | 09, 10 |
| 09_functors_categories | 07, 08 | 10 |
| 10_superposition | 08, 09 | — |
| 11_reslang_architecture | 00–10 | — |
| 12_timeline_30aug | — | — |
