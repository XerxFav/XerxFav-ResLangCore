"""
cycle_manager.py — базовый модуль для моделирования фазовых переходов и резонансных циклов
в рамках Dutrimxord/ArcaLang.
"""

import numpy as np
import plotly.express as px

class CycleManager:
    def __init__(self, steps=1000):
        self.steps = steps
        self.time = np.linspace(0, 10, steps)

    def resonance_cycle(self, freq=1.0, damping=0.05):
        """
        Простая модель затухающего резонансного цикла:
        x(t) = exp(-damping*t) * sin(2*pi*freq*t)
        """
        signal = np.exp(-damping * self.time) * np.sin(2 * np.pi * freq * self.time)
        return signal

    def phase_transition(self, threshold=0.5):
        """
        Модель фазового перехода: бинаризация сигнала по порогу.
        """
        signal = self.resonance_cycle()
        phase = (signal > threshold).astype(int)
        return phase

    def visualize(self, signal, title="Resonance Cycle"):
        """
        Визуализация сигнала через Plotly.
        """
        fig = px.line(x=self.time, y=signal, title=title, labels={"x":"Time","y":"Amplitude"})
        fig.show()


if __name__ == "__main__":
    cm = CycleManager(steps=500)

    # Резонансный цикл
    res_signal = cm.resonance_cycle(freq=2.0, damping=0.1)
    cm.visualize(res_signal, title="Resonance Cycle (freq=2.0, damping=0.1)")

    # Фазовый переход
    phase_signal = cm.phase_transition(threshold=0.3)
    cm.visualize(phase_signal, title="Phase Transition (threshold=0.3)")
