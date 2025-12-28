graph TD
    A00["00 Intro Physys"]
    A01["01 Singular Physys"]
    A02["02 Adaptive Physys"]
    A03["03 Interaction Physys"]
    A04["04 Phase Memory"]
    A05["05 Impedance & Hysteresis"]
    A06["06 Resonance Node"]
    A07["07 Phase Network"]
    A08["08 Phase Operators"]
    A09["09 Functors & Categories"]
    A10["10 Superposition"]
    A11["11 ArcaLang Architecture"]
    A12["12 Timeline"]

    A00 --> A01
    A00 --> A02
    A00 --> A03

    A03 --> A04
    A03 --> A05
    A03 --> A06
    A03 --> A07

    A07 --> A08
    A07 --> A09
    A07 --> A10

    A10 --> A11
## Связь с ArcaLang

Оператор валидности `ν(P)` и итеративный оператор `𝓘(𝓒ₙ, Pₙ₊₁)` имеют прямое отображение в ядро ArcaLang:

- `ProtoFormOperator.classify_category(P1, P2, P3)` реализует модель чётной/нечётной категориальности,
- `ProtoFormOperator.iterate_configuration(Cn, P_next)` реализует итеративное расширение фазовой сети.

Таким образом, MetaPhysics задаёт теоретическую архитектуру, а ArcaLang — исполнимую форму этих операторов.

