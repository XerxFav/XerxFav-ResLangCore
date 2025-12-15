# arca_langlib/types/protoform_operator.py
# ProtoFormOperator — ядро ArcaLang
# Содержит инварианты, резонансные состояния, энергетику, PotentialSpace и контракт инвариантности

import math

class ProtoFormOperator:
    """
    ProtoFormOperator — операционный класс для работы с потенциальным пространством,
    инвариантами, резонансными состояниями и энергетикой.
    """

    # === 1. Инварианты ===
    def invariant_phys(self, V: float, V0: float, R: float) -> float:
        return (V - V0) / (4 * math.pi * R**3)

    def invariant_abs(self, psi0: float, V: float, V0: float, R: float) -> float:
        return ( (1 - psi0)**(1/3) )**(3/2) / self.invariant_phys(V, V0, R)

    def calc_n(self, V: float, V0: float, R: float) -> float:
        return (4 * math.pi * R**3) / (V - V0)

    # === 2. Резонансные состояния ===
    def psi1(self, x: float, y: float, z: float, n: float) -> float:
        return -(x**n + y**n + z**n)

    def psi2(self, x: float, y: float, z: float, n: float) -> float:
        S = x**n + y**n + z**n
        return (2*x**n - S) * (2*y**n - S) * (2*z**n - S)

    def omega(self, psi2: float, psi1: float) -> float:
        return psi2 / psi1 if psi1 != 0 else float("inf")

    # === 3. Энергетика и масса ===
    def energy_from_field(self, psi0: float, V: float, V0: float, R: float) -> float:
        numerator = 4 * math.pi * R**3
        denominator = ((1 - psi0)**(1/3))**(3/2) / (V - V0)
        return math.sqrt(numerator / denominator)

    def local_mass(self, kappa: float, R0: float, v: float, C: float) -> float:
        return kappa * (4 * math.pi * R0**3) * (v / C)**2

    def density(self, z: float) -> float:
        return 1 / (z**(2/3))

    def N_vol(self, m: float, C: float, R: float, E: float) -> float:
        Qnd = self.Qnd(m, C)
        return Qnd / (4 * math.pi * R**3)

    def Qnd(self, m: float, C: float) -> float:
        return (1 / (m * C**2))**(1/3)

    # === 4. PotentialSpace ===
    def field_equation(self, psi0: float, V: float, V0: float, R: float) -> bool:
        lhs = ((1 - psi0)**(1/3))**(3/2) / (V - V0)
        rhs = 4 * math.pi * R**3
        return math.isclose(lhs, rhs, rel_tol=1e-9)

    def global_potential(self, Rglob: float, Vglob: float) -> float:
        return (4 * math.pi * Rglob**3) / Vglob

    def local_potential_obj(self, E: float) -> float:
        return (1 - E)**(2/3)

    def time_volume_global(self, psi0_obj: float, PsiGlob: float) -> float:
        return (1 + psi0_obj / PsiGlob)**(1/3)

    def time_volume_local(self, m0: float, v: float, C: float) -> float:
        return (1 / (m0 * (v/C)**2))**(1/3)

    def mass_energy_link(self, E: float, R0: float, m0: float, v: float, C: float, psi0_obj: float) -> bool:
        lhs = E / (4 * math.pi * R0**3)
        rhs = (m0 * (v/C)**2) / psi0_obj
        return math.isclose(lhs, rhs, rel_tol=1e-9)

    # === 5. Синтез ===
    def mass_genesis(self, R: float, r: float, V: float, V0: float, E: float, C: float, psi1: float, psi2: float) -> bool:
        omega_val = self.omega(psi2, psi1)
        lhs = (V - V0) / (4 * math.pi * R**3 * r**2)
        rhs1 = E / C**2
        rhs2 = (E * psi2) / omega_val if omega_val != 0 else float("inf")
        return math.isclose(lhs, rhs1, rel_tol=1e-9) and math.isclose(rhs1, rhs2, rel_tol=1e-9)

    def nuclear_synthesis(self, R: float, r: float, Z: float) -> float:
        return (4 * math.pi * R**3 * r**2) / Z

    # === 6. Контракт инвариантности ===
    def conserve(self, Iphys: float, Phi: float, epsilon: float) -> bool:
        Delta = Iphys - Phi
        return abs(Delta) <= epsilon

    def handoff(self, Iphys: float, Phi: float, epsilon: float) -> str:
        Delta = Iphys - Phi
        return "SWITCH_MODEL" if abs(Delta) > epsilon else "STAY"
