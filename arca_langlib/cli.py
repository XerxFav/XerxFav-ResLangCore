# arca_langlib/cli.py
import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(
        description="ArcaLang CLI — управление операторами и библиотекой"
    )
    parser.add_argument("--list", action="store_true", help="Показать список доступных операторов")
    parser.add_argument("--describe", action="store_true", help="Описание ключевых операторов")
    parser.add_argument("--k", type=int, help="Параметр k для casus reducibilis")
    parser.add_argument("--b", type=int, help="Параметр b для casus reducibilis")
    parser.add_argument("--mode", choices=["auto", "trig", "cardano"], help="Режим решения")
    parser.add_argument("--all-roots", action="store_true", help="Вывести все действительные корни (casus irreducibilis)")
    parser.add_argument("--json", action="store_true", help="Вывести результат в формате JSON")

    args = parser.parse_args()

    if args.list:
        print("Доступные операторы: casus_reducibilis, resonance, protoform_operator")
        sys.exit(0)

    if args.describe:
        print("Casus Reducibilis — оператор для решения кубических уравнений (Кардано, тригонометрия).")
        print("Resonance — оператор для анализа фазовых переходов.")
        print("Protoform Operator — оператор для работы с абстрактными фазовыми структурами.")
        sys.exit(0)

    if args.k is not None and args.b is not None:
        from arca_langlib.casus_reducibilis import resolve_casus_irreducibilis, solve_cubic_trig_all, solve_cubic

        result = None
        if args.mode == "trig":
            result = solve_cubic_trig_all(args.k, args.b)
        elif args.mode == "cardano":
            result = solve_cubic(args.k, args.b)
        else:  # auto
            result = resolve_casus_irreducibilis(args.k, args.b, all_roots=args.all_roots)

        if args.json:
            print(json.dumps({"k": args.k, "b": args.b, "mode": args.mode or "auto", "roots": result}, ensure_ascii=False))
        else:
            if args.mode == "trig":
                print(f"Тригонометрическая форма: корни {result}")
            elif args.mode == "cardano":
                print(f"Кардано: корень {result}")
            else:
                if args.all_roots:
                    print(f"Все действительные корни: {result}")
                else:
                    print(f"Решение: {result}")
        sys.exit(0)

    # Если аргументы не заданы
    parser.print_help()

if __name__ == "__main__":
    main()
