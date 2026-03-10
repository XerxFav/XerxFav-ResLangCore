import math
import matplotlib.pyplot as plt


# ============================================================
# 1. БАЗОВАЯ КРИВАЯ
# ============================================================

def base_curve(x):
    """y = ∛(1/x²). Возвращает None, если x=0."""
    if x == 0:
        return None
    return (1 / (x * x)) ** (1/3)


# ============================================================
# 2. ПОВОРОТ ТОЧКИ
# ============================================================

def rotate(x, y, theta):
    """Поворот точки (x, y) на угол theta (в радианах)."""
    ct = math.cos(theta)
    st = math.sin(theta)
    return (
        x * ct - y * st,
        x * st + y * ct
    )


# ============================================================
# 3. ОБЛАСТЬ НАБЛЮДАТЕЛЯ r
# ============================================================

def observer_radius_region(m, k=1.0, alpha=0.6):
    """
    Возвращает область наблюдателя:
    r_min(m), r_max(m)

    r_max = k * ∛(1/m)
    r_min = α * r_max
    """
    r_max = k * (1 / m) ** (1/3)
    r_min = alpha * r_max
    return r_min, r_max


# ============================================================
# 4. ГЕНЕРАЦИЯ ТРЁХ ВЕТВЕЙ
# ============================================================

def generate_ternary_branches(xmin=-5, xmax=5, step=0.05):
    branch0 = []
    branch120 = []
    branch240 = []

    theta120 = math.radians(120)
    theta240 = math.radians(240)

    x = xmin
    while x <= xmax:
        y = base_curve(x)
        if y is not None:
            branch0.append((x, y))
            branch120.append(rotate(x, y, theta120))
            branch240.append(rotate(x, y, theta240))
        x += step

    return {
        "branch0": branch0,
        "branch120": branch120,
        "branch240": branch240
    }


# ============================================================
# 5. ВИЗУАЛИЗАЦИЯ
# ============================================================

def plot_grav_core(branches, r_min=None, r_max=None):
    plt.figure(figsize=(7, 7))

    # Ветви
    for name, pts in branches.items():
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        plt.plot(xs, ys, label=name)

    # Радиус наблюдателя
    if r_min is not None:
        circle = plt.Circle((0, 0), r_min, color='green', fill=False, linestyle='--')
        plt.gca().add_patch(circle)

    if r_max is not None:
        circle = plt.Circle((0, 0), r_max, color='red', fill=False, linestyle='--')
        plt.gca().add_patch(circle)

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title("GravCore Ternary Axes")
    plt.show()


# ============================================================
# 6. МОРФОЛОГИЧЕСКИЙ ОПЕРАТОР ДЛЯ ARCALANG
# ============================================================

class GravCoreTernary:
    """
    Минимальный морфологический оператор.
    Может быть подключён в ArcaLang как protoform_operator.
    """

    def __init__(self, m=8.0, k=1.0, alpha=0.6):
        self.m = m
        self.k = k
        self.alpha = alpha

    def compute(self):
        """Возвращает ветви и область наблюдателя."""
        branches = generate_ternary_branches()
        r_min, r_max = observer_radius_region(self.m, self.k, self.alpha)
        return branches, r_min, r_max

    def visualize(self):
        """Рисует график."""
        branches, r_min, r_max = self.compute()
        plot_grav_core(branches, r_min, r_max)


# ============================================================
# 7. ТЕСТ ПРИ ЗАПУСКЕ
# ============================================================

if __name__ == "__main__":
    op = GravCoreTernary(m=8.0)
    op.visualize()
