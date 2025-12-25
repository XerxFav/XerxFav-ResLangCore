import matplotlib.pyplot as plt
import numpy as np


def plot_phase_trajectory(times, E_values, psi_values, V_values):
    plt.figure(figsize=(8, 5))
    plt.plot(times, E_values, label="E(t)")
    plt.plot(times, psi_values, label="ψ₀(t)")
    plt.plot(times, V_values, label="ΔV(t)")
    plt.legend()
    plt.xlabel("t")
    plt.ylabel("Values")
    plt.title("Phase Trajectory")
    plt.grid(True)
    plt.show()


def plot_phase_map(field, title="Phase Map"):
    plt.figure(figsize=(6, 6))
    plt.imshow(field, cmap="viridis")
    plt.colorbar()
    plt.title(title)
    plt.show()


def plot_correlation_matrix(M):
    plt.figure(figsize=(6, 6))
    plt.imshow(M, cmap="coolwarm", vmin=0, vmax=1)
    plt.colorbar()
    plt.title("Correlation Matrix")
    plt.show()
