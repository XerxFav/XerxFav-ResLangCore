module Phase.Algometry:

  # ------------------------------------------------------------
  # 1. Инвариант C/L = U/A
  # ------------------------------------------------------------
  operator algometric_invariant:
    input:
      - C: Real
      - L: Real
      - U: Real
      - A: Real
    output:
      - valid: Bool
    invariant:
      valid = (C / L == U / A)
    domain:
      L != 0
      A != 0
    description:
      "Алгометрический инвариант согласования геометрии и энергии."

