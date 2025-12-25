import math


def sphere_volume(R: float) -> float:
    return (4.0 / 3.0) * math.pi * (R ** 3)


def torus_volume(R: float, r: float) -> float:
    return 2.0 * (math.pi ** 2) * R * (r ** 2)


def global_volume_from_Psiobj(Psi_obj: float) -> float:
    return (1.0 / (Psi_obj ** 2)) ** (1.0 / 3.0)


def geom_density(R: float, V: float) -> float:
    return (4.0 * math.pi * (R ** 3)) / V
