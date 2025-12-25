module Phase.Dynamics:

  # ------------------------------------------------------------
  # 1. Энергетический импульс ΔE = A exp(-r² / σ²)
  # ------------------------------------------------------------
  operator energy_trigger:
    input:
      - A: Real
      - dx: Real
      - dy: Real
      - dz: Real
      - sigma: Real
    output:
      - dE: Real
    invariant:
      dE = A * exp(-(dx^2 + dy^2 + dz^2) / sigma^2)
    domain:
      sigma > 0
    description:
      "Фазовый энергетический импульс в локальной области."


  # ------------------------------------------------------------
  # 2. Адаптация памяти ψ0_new = ψ0 (1 - (E - Ecrit)/E)
  # ------------------------------------------------------------
  operator memory_adapt:
    input:
      - psi0: Real
      - E: Real
      - Ecrit: Real
    output:
      - psi_new: Real
    invariant:
      psi_new = psi0 * (1 - (E - Ecrit) / E)
    domain:
      E != 0
    description:
      "Адаптация памяти при превышении критической энергии."


  # ------------------------------------------------------------
  # 3. Корреляция M = exp(-|ψi - ψj| / Ψglob)
  # ------------------------------------------------------------
  operator correlation:
    input:
      - psi_i: Real
      - psi_j: Real
      - Psi_glob: Real
    output:
      - M: Real
    invariant:
      M = exp(-abs(psi_i - psi_j) / Psi_glob)
    domain:
      Psi_glob != 0
    description:
      "Фазовая корреляция между двумя ячейками."


  # ------------------------------------------------------------
  # 4. Условие резонанса Ψ/ψ0 ≈ E²
  # ------------------------------------------------------------
  operator resonance_condition:
    input:
      - Psi: Real
      - psi0: Real
      - E: Real
    output:
      - R: Real
    invariant:
      R = Psi / psi0 - E^2
    domain:
      psi0 != 0
    description:
      "Отклонение от идеального фазового резонанса."
