"""
OctaveBridge — мост для интеграции GNU Octave с ArcaLang/Dutrimxord.
Использует библиотеку oct2py для вызова Octave-функций из Python.
"""

from oct2py import Oct2Py

class OctaveBridge:
    def __init__(self):
        # Инициализация сессии Octave
        self.oc = Oct2Py()

    def run(self, code: str):
        """
        Выполнить произвольный Octave-код.
        :param code: строка с Octave-выражением
        :return: результат выполнения
        """
        return self.oc.eval(code)

    def run_function(self, func: str, *args):
        """
        Вызвать Octave-функцию с аргументами.
        :param func: имя функции (например, 'sin')
        :param args: аргументы для функции
        :return: результат выполнения
        """
        return getattr(self.oc, func)(*args)

    def close(self):
        """Закрыть сессию Octave."""
        self.oc.exit()


# === Пример использования ===
if __name__ == "__main__":
    bridge = OctaveBridge()

    # Пример: выполнить выражение напрямую
    result_expr = bridge.run("sin(pi/4)")
    print("Результат sin(pi/4):", result_expr)

    # Пример: вызвать функцию Octave
    result_func = bridge.run_function("cos", 3.14159/3)
    print("Результат cos(pi/3):", result_func)

    bridge.close()

