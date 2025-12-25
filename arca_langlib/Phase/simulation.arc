module Phase.Simulation:

  # ------------------------------------------------------------
  # 1. Обновление энергии ячейки
  # ------------------------------------------------------------
  operator update_energy:
    input:
      - E0: Real
      - dE_t: Real
      - dE_trigger: Real
    output:
      - E_new: Real
    invariant:
      E_new = E0 + dE_t + dE_trigger
    description:
      "Обновление энергии ячейки с учётом импульса."


  # ------------------------------------------------------------
  # 2. Обновление объёма времени ΔV
  # ------------------------------------------------------------
  operator update_volume:
    input:
      - psi0: Real
      - Psi_glob: Real
    output:
      - V_new: Real
    invariant:
      V_new = cbrt(1 + psi0 / Psi_glob)
    domain:
      Psi_glob != 0
    description:
      "Перестройка фазового объёма."


  # ------------------------------------------------------------
  # 3. Проверка устойчивости M >= ε
  # ------------------------------------------------------------
  operator stability_check:
    input:
      - M: Real
      - eps: Real
    output:
      - stable: Bool
    invariant:
      stable = (M >= eps)
    description:
      "Проверка устойчивости фазовой связи."


  # ------------------------------------------------------------
  # 4. Проверка фазового равновесия
  # ------------------------------------------------------------
  operator equilibrium_check:
    input:
      - dpsi_dt: Real
      - dE: Real
      - eps: Real
    output:
      - eq: Bool
    invariant:
      eq = (abs(dpsi_dt) < eps) and (abs(dE) < eps)
    description:
      "Условие фазового равновесия."
