import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(prog="arca", description="ArcaLang CLI — управление операторами")
    subparsers = parser.add_subparsers(dest="command")

    # casus reducibilis
    casus_parser = subparsers.add_parser("casus", help="Решение кубических уравнений")
    casus_parser.add_argument("--k", type=int, required=True)
    casus_parser.add_argument("--b", type=int, required=True)
    casus_parser.add_argument("--mode", choices=["auto", "trig", "cardano"], default="auto")
    casus_parser.add_argument("--all-roots", action="store_true")
    casus_parser.add_argument("--json", action="store_true")

    # resonance
    resonance_parser = subparsers.add_parser("resonance", help="Анализ фазовых переходов")
    resonance_parser.add_argument("--input", type=str, help="Файл с данными")

    # protoform
    proto_parser = subparsers.add_parser("protoform", help="Работа с абстрактными фазовыми структурами")
    proto_parser.add_argument("--describe", action="store_true")
    proto_parser.add_argument("--method", type=str, help="Имя метода ProtoFormOperator")
    proto_parser.add_argument("--args", type=str, help="Аргументы в формате key=value,...")
    proto_parser.add_argument("--input", type=str, help="JSON-файл с аргументами")


    args = parser.parse_args()

    if args.command == "casus":
        from arca_langlib.casus_reducibilis import resolve_casus_irreducibilis, solve_cubic_trig_all, solve_cubic
        if args.mode == "trig":
            result = solve_cubic_trig_all(args.k, args.b)
        elif args.mode == "cardano":
            result = solve_cubic(args.k, args.b)
        else:
            result = resolve_casus_irreducibilis(args.k, args.b, all_roots=args.all_roots)

        if args.json:
            print(json.dumps({"k": args.k, "b": args.b, "mode": args.mode, "roots": result}, ensure_ascii=False))
        else:
            print(f"Результат: {result}")

    elif args.command == "resonance":
        from arca_langlib.drivers.resonance import analyze_resonance
        print(analyze_resonance(args.input))

    elif args.command == "protoform":
        from arca_langlib.types.protoform_operator import ProtoFormOperator, describe_protoform

        if args.describe:
            print(describe_protoform())
    elif args.method:
            obj = ProtoFormOperator()
            method = getattr(obj, args.method, None)
            if not method:
                print(f"Метод {args.method} не найден.")
    else:
            kwargs = {}

            # 1. Если указан JSON-файл — загрузим базовые аргументы
            if args.input:
                try:
                    with open(args.input, "r", encoding="utf-8") as f:
                        kwargs = json.load(f)
                except Exception as e:
                    print(f"Ошибка чтения JSON: {e}")
                    sys.exit(1)

            # 2. Если указаны аргументы вручную — они дополняют или переопределяют JSON
            if args.args:
                for pair in args.args.split(","):
                    if "=" in pair:
                        k, v = pair.split("=")
                        v = v.strip()
                        # Автоматическое определение типа
                        if v.lower() in ("true", "false"):
                            val = v.lower() == "true"
                        else:
                            try:
                                if "." in v:
                                    val = float(v)
                                else:
                                    val = int(v)
                            except ValueError:
                                val = v
                        kwargs[k.strip()] = val

            # 3. Вызов метода
            else:       
                result = method(**kwargs)
                print(f"{args.method}({kwargs}) = {result}")
                parser.print_help()
