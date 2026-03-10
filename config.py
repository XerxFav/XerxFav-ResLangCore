from dataclasses import dataclass
from typing import List, Literal

Mode = Literal["cub", "exp", "log", "mix"]


@dataclass
class MorphologyConfig:
    """
    Базовая конфигурация морфологического движка.
    Минимальное ядро, дальше можно наращивать (ключ, лог-параметры и т.п.).
    """

    modes: List[Mode]
    initial_impulse: float = 1.0
    alpha: float = 0.5  # смешивание cub/exp в режиме mix

    # задел под логарифмический режим
    log_gamma: float = 1.0
    log_beta: float = 1.0
    C0: float = 1.0
