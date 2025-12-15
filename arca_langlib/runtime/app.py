"""
app.py — сервер FastAPI для ArcaLang/Dutrimxord
Запускается через `make serve`
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import numpy as np
import plotly.graph_objs as go

# Импортируем CycleManager из твоего runtime
from arca_langlib.runtime.cycle_manager import CycleManager

app = FastAPI(
    title="ArcaLang Runtime API",
    description="API для моделирования фазовых переходов, резонансных циклов и линейной алгебры",
    version="0.4.0"
)

# ---------------------------
# Модели данных
# ---------------------------
class MatrixInput(BaseModel):
    matrix: list[list[float]]

class SimulationInput(BaseModel):
    freq: float = 1.0
    damping: float = 0.05
    duration: float = 5.0
    steps: int = 100

# ---------------------------
# Эндпоинты
# ---------------------------
@app.get("/")
def root():
    return {"message": "Добро пожаловать в ArcaLang/Dutrimxord API!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/resonance")
def resonance(freq: float = 1.0, damping: float = 0.05):
    time = np.linspace(0, 2, 10)
    signal = (np.exp(-damping * time) * np.sin(2 * np.pi * freq * time)).tolist()
    return {"freq": freq, "damping": damping, "signal": signal}

@app.post("/matrix")
def matrix_eigen(input_data: MatrixInput):
    mat = np.array(input_data.matrix)
    eigenvalues, eigenvectors = np.linalg.eig(mat)
    return {
        "matrix": input_data.matrix,
        "eigenvalues": eigenvalues.tolist(),
        "eigenvectors": eigenvectors.tolist()
    }

@app.post("/simulate")
def simulate_cycle(params: SimulationInput):
    cm = CycleManager(freq=params.freq, damping=params.damping,
                      duration=params.duration, steps=params.steps)
    signal = cm.run_cycle().tolist()
    return {
        "freq": params.freq,
        "damping": params.damping,
        "duration": params.duration,
        "steps": params.steps,
        "signal": signal
    }

@app.post("/visualize", response_class=HTMLResponse)
def visualize_cycle(params: SimulationInput):
    """
    Эндпоинт для визуализации сигнала через Plotly.
    Возвращает интерактивный HTML-график.
    """
    cm = CycleManager(freq=params.freq, damping=params.damping,
                      duration=params.duration, steps=params.steps)
    signal = cm.run_cycle()
    time = np.linspace(0, params.duration, params.steps)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=signal, mode="lines", name="Signal"))
    fig.update_layout(title="Cycle Simulation", xaxis_title="Time", yaxis_title="Amplitude")

    return fig.to_html(full_html=True)
