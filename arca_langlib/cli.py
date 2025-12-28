# arca_langlib/cli.py
import argparse
import json

from arca_langlib.casus_reducibilis import (
    resolve_casus_irreducibilis,
    solve_cubic_trig_all,
    solve_cubic,
)


# ============================================================
#  CASUS EXECUTION
# ============================================================

def run_casus(
    k: float,
    b: float,
    mode: str,
    all_roots: bool,
    json_mode: bool,
    math_mode: str,
) -> str:
    """
    Единая точка выполнения casus для CLI.
    math_mode ∈ {"arca", "strict"}.
    """
    if mode == "trig":
        # В trig-режиме показываем все корни (естественно для casus).
        roots = solve_cubic_trig_all(k, b, math_mode=math_mode)
        result = roots
        header = "Тригонометрическая форма"

    elif mode == "cardano":
        result = solve_cubic(k, b, math_mode=math_mode)
        header = "Решение (формула Кардано)"

    else:  # auto
        result = resolve_casus_irreducibilis(
            k,
            b,
            all_roots=all_roots,
            math_mode=math_mode,
        )
        header = "Все действительные корни" if all_roots else "Решение"

    if json_mode:
        return json.dumps(
            {
                "k": k,
                "b": b,
                "mode": mode,
                "math_mode": math_mode,
                "result": result,
            },
            ensure_ascii=False,
        )

    return f"{header}: {result}"


# ============================================================
#  MAIN CLI PARSER
# ============================================================

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="arca",
        description="ArcaLang CLI — casus и DSL в собственной алгебре Arca",
    )

    # Глобальные опции (служебные)
    parser.add_argument(
        "--list",
        action="store_true",
        help="Показать список доступных команд",
    )
    parser.add_argument(
        "--describe",
        action="store_true",
        help="Показать описание CLI",
    )

    # Подкоманды
    sub = parser.add_subparsers(dest="cmd")

    # --------------------------------------------------------
    #  Подкоманда: casus
    # --------------------------------------------------------
    cas = sub.add_parser(
        "casus",
        help="Решение кубических уравнений (оператор casus)",
    )
    cas.add_argument(
        "--k",
        type=float,
        required=True,
        help="Параметр k в уравнении x^3 = kx + b",
    )
    cas.add_argument(
        "--b",
        type=float,
        required=True,
        help="Параметр b в уравнении x^3 = kx + b",
    )
    cas.add_argument(
        "--mode",
        choices=["auto", "trig", "cardano"],
        default="auto",
        help="Режим решения: auto / trig / cardano",
    )
    cas.add_argument(
        "--all-roots",
        action="store_true",
        help="Вернуть все действительные корни (для auto)",
    )
    cas.add_argument(
        "--json",
        action="store_true",
        help="Вывод в формате JSON",
    )
    cas.add_argument(
        "--math-mode",
        choices=["arca", "strict"],
        default="arca",
        help="Математический режим: arca (по умолчанию) или strict",
    )

    # --------------------------------------------------------
    #  Подкоманда: eval (DSL)
    # --------------------------------------------------------
    ev = sub.add_parser(
        "eval",
        help="Выполнить выражение DSL ArcaLang",
    )
    ev.add_argument(
        "expression",
        type=str,
        help='Выражение DSL, например: "casus(15,4)"',
    )
    ev.add_argument(
        "--math-mode",
        choices=["arca", "strict"],
        default="arca",
        help="Математический режим интерпретации выражения",
    )

    return parser
# ============================================================
#  MAIN DISPATCH LOGIC
# ============================================================

def main(argv=None) -> str:
    parser = build_parser()
    args = parser.parse_args(argv)

    # --- Глобальные команды ---

    if args.list:
        return (
            "Команды: casus, eval, "
            "--list, --describe"
        )

    if args.describe:
        return (
            "ArcaLang CLI (Arca-алгебра по умолчанию):\n"
            "  • casus --k K --b B [--mode ...] [--math-mode ...]\n"
            "  • eval \"EXPR\" [--math-mode ...]\n"
            "  • --list       — список команд\n"
            "  • --describe   — описание CLI\n"
        )

    # --- Подкоманда casus ---

    if args.cmd == "casus":
        return run_casus(
            k=args.k,
            b=args.b,
            mode=args.mode,
            all_roots=args.all_roots,
            json_mode=args.json,
            math_mode=args.math_mode,
        )

    # --- Подкоманда eval (DSL) ---

    if args.cmd == "eval":
        # Здесь пока примитивная заглушка DSL.
        # Позже сюда подключим настоящий парсер/evaluator ArcaLang.
        expr = args.expression.strip()

        # Простая форма: casus(k,b)
        if expr.startswith("casus(") and expr.endswith(")"):
            inner = expr[len("casus("):-1]
            parts = [p.strip() for p in inner.split(",")]
            if len(parts) >= 2:
                k = float(parts[0])
                b = float(parts[1])
                result = resolve_casus_irreducibilis(
                    k,
                    b,
                    all_roots=False,
                    math_mode=args.math_mode,
                )
                return f"DSL casus: {result}"

        # В будущем: phase algebra { x = casus(15,4) } и полноформатный DSL.
        return f"Ошибка DSL: пока поддерживается только форма casus(k,b)"

    # --- Если подкоманда не указана ---

    return parser.format_help()


# ============================================================
#  ENTRYPOINT
# ============================================================

def run():
    """Точка входа для CLI, всегда печатает вывод."""
    out = main()
    if out is not None:
        print(out)


if __name__ == "__main__":
    run()
