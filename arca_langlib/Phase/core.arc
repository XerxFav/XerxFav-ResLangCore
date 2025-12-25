module Phase.Core:

  # ------------------------------------------------------------
  # 1. Потенциал ячейки ψ0 = ∛(1 - E^2)
  # ------------------------------------------------------------
  operator psi0_from_E:
    input:
      - E: Real
    output:
      - psi0: Real
    invariant:
      psi0 = cbrt(1 - E^2)
    domain:
      0 <= E <= 1
    description:
      "Локальный потенциал памяти ячейки по нормированной энергии."


  # ------------------------------------------------------------
  # 2. Глобальный потенциал Ψ_glob = 4π R^3 / (V - V0)
  # ------------------------------------------------------------
  operator psiglob_from_R_V:
    input:
      - R_glob: Real
      - V: Real
      - V0: Real
    output:
      - Psi_glob: Real
    invariant:
      Psi_glob = 4 * pi * R_glob^3 / (V - V0)
    domain:
      R_glob > 0
      V > V0
    description:
      "Глобальный потенциал пространства для заданного радиуса и объёма времени."


  # ------------------------------------------------------------
  # 3. Фазовый объём ΔV = ∛(1 + ψ0 / Ψ_glob)
  # ------------------------------------------------------------
  operator deltaV_from_psi0_Psiglob:
    input:
      - psi0: Real
      - Psi_glob: Real
    output:
      - deltaV: Real
    invariant:
      deltaV = cbrt(1 + psi0 / Psi_glob)
    domain:
      Psi_glob != 0
    description:
      "Фазовая деформация объёма времени."


  # ------------------------------------------------------------
  # 4. Фазовая плотность ρφ = (V - V0) / (4π R^3)
  # ------------------------------------------------------------
  operator phase_density:
    input:
      - V: Real
      - V0: Real
      - R: Real
    output:
      - rho_phi: Real
    invariant:
      rho_phi = (V - V0) / (4 * pi * R^3)
    domain:
      R > 0
      V >= V0
    description:
      "Фазовая плотность объёма времени."


  # ------------------------------------------------------------
  # 5. Энергетическая плотность ρE = E / (4π R0^3)
  # ------------------------------------------------------------
  operator energy_density:
    input:
      - E: Real
      - R0: Real
    output:
      - rho_E: Real
    invariant:
      rho_E = E / (4 * pi * R0^3)
    domain:
      R0 > 0
    description:
      "Энергетическая плотность подпространства."


  # ------------------------------------------------------------
  # 6. Эффективная масса m0 = (E ψ0) / (4π R0^3 (v/C)^2)
  # ------------------------------------------------------------
  operator m_effective_from_E_R0_psi0:
    input:
      - E: Real
      - R0: Real
      - psi0: Real
      - v_over_c: Real
    output:
      - m0: Real
    invariant:
      m0 = (E * psi0) / (4 * pi * R0^3 * v_over_c^2)
    domain:
      R0 > 0
      psi0 != 0
      v_over_c != 0
    description:
      "Эффективная масса, формируемая в подпространственном объёме."


  # ------------------------------------------------------------
  # 7. Резонансное отношение ψ_new = Ψ / ψ_res
  # ------------------------------------------------------------
  operator resonance_ratio:
    input:
      - Psi: Real
      - psi_res: Real
    output:
      - psi_new: Real
    invariant:
      psi_new = Psi / psi_res
    domain:
      psi_res != 0
    description:
      "Порождаемый новый резонанс."


  # ------------------------------------------------------------
  # 8. Индекс фазового заполнения n = 4π R^3 / (V - V0)
  # ------------------------------------------------------------
  operator phase_index_n:
    input:
      - R: Real
      - V: Real
      - V0: Real
    output:
      - n: Real
    invariant:
      n = 4 * pi * R^3 / (V - V0)
    domain:
      R > 0
      V > V0
    description:
      "Индекс фазового заполнения пространства."
