from . import core, dynamics, simulation


def phase_step(E, psi0, Psi_glob, A, dx, dy, dz, sigma, eps):
    """
    Выполняет один фазовый шаг.
    Возвращает:
      - новое E
      - новое ΔV
      - адаптированную ψ0
      - корреляцию M (локальную)
      - флаг устойчивости
      - флаг равновесия
    """

    # 1. Энергетический импульс
    dE_trigger = dynamics.energy_trigger(A, dx, dy, dz, sigma)

    # 2. Обновление энергии
    E_new = simulation.update_energy(E, 0.0, dE_trigger)

    # 3. Обновление объёма
    deltaV_new = simulation.update_volume(psi0, Psi_glob)

    # 4. Адаптация памяти
    psi_new = dynamics.memory_adapt(psi0, E_new, Ecrit=E)

    # 5. Корреляция (локальная)
    M = dynamics.correlation(psi_new, psi0, Psi_glob)

    # 6. Устойчивость
    stable = simulation.stability_check(M, eps)

    # 7. Равновесие
    eq = simulation.equilibrium_check(
        dpsi_dt=psi_new - psi0,
        dE=E_new - E,
        eps=eps
    )

    return {
        "E": E_new,
        "deltaV": deltaV_new,
        "psi0": psi_new,
        "M": M,
        "stable": stable,
        "equilibrium": eq
    }
