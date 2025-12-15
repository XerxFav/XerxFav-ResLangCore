# arca_langlib/examples/newton_matrix_demo.py
import math
from arca_langlib.types.memory_cell import MemoryCell

def f(x, a, b):
    return x + a * math.tan(b * x)

def fp(x, a, b):
    c = math.cos(b * x)
    if abs(c) < 1e-12:
        return float('inf')  # защищаемся от асимптот
    return 1.0 + a * b / (c * c)

def newton_matrix_cycle(a: float, b: float, x0: float, tol: float = 1e-10, max_iter: int = 30):
    """
    Мини-цикл Ньютона в стиле матрицы (Ошибка → Тень → Фаза → Ресурс),
    с записью шагов в MemoryCell. Возвращает (x, history).
    """
    mem = MemoryCell(theta=1.0)
    x = x0
    history = []  # [(iter, x, e, opcode_shadow, opcode_phase)]

    for it in range(1, max_iter + 1):
        e = f(x, a, b)

        # 1) Тень: радиус ошибки
        shadow = mem.write_shadow(f"iter{it}_P", abs(e))
        op_shadow = mem.to_opcode(shadow)  # ("SHADOW", radius, theta)

        if abs(e) < tol:
            history.append((it, x, e, op_shadow, None))
            break

        # 2) Фаза: шаг Ньютона
        d = fp(x, a, b)
        if not math.isfinite(d) or abs(d) < 1e-14:
            # если производная плоха — мягко выходим
            phase = mem.write_phase(f"iter{it}_K", abs(e) + 1e-12)
            op_phase = mem.to_opcode(phase)  # ("PHASE", radius, theta)
            history.append((it, x, e, op_shadow, op_phase))
            break

        step = -e / d
        # защитное ограничение шага, чтобы не «перепрыгнуть» через асимптоты
        if abs(step) > 1.0:
            step = math.copysign(1.0, step)

        # запись фазы как направленного шага (адресность θ=1)
        phase = mem.write_phase(f"iter{it}_K", abs(step) + 1e-12)
        op_phase = mem.to_opcode(phase)  # ("PHASE", radius, theta)

        # 3) Ресурс: новое приближение
        x_next = x + step
        history.append((it, x, e, op_shadow, op_phase))
        x = x_next

    return x, history

if __name__ == "__main__":
    # Пример: a=0.5, b=1.2, старт в безопасном интервале (k=0)
    a, b = 0.5, 1.2
    # центр интервала между асимптотами tan: ((k-0.5)π/b, (k+0.5)π/b). Возьмём середину (≈0.0)
    x0 = 0.1  # лёгкий сдвиг от 0, чтобы избежать нулевой производной в редких случаях
    x_star, hist = newton_matrix_cycle(a, b, x0)

    print(f"root ≈ {x_star:.12g}")
    for (it, x, e, op_shadow, op_phase) in hist:
        shadow_op, shadow_radius, shadow_theta = op_shadow
        if op_phase is None:
            print(f"iter {it:02d}: x={x:.9g} | e={e:.3e} | {shadow_op} r={shadow_radius:.3e} θ={shadow_theta:.3g} | PHASE: none")
        else:
            phase_op, phase_radius, phase_theta = op_phase
            print(f"iter {it:02d}: x={x:.9g} | e={e:.3e} | {shadow_op} r={shadow_radius:.3e} θ={shadow_theta:.3g} "
                  f"| {phase_op} step≈{phase_radius:.3e} θ={phase_theta:.3g}")
