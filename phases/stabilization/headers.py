# headers.py — фазовые заголовки и метаописания ядра

MODULES = {
    "chronotope": {
        "description": "Фазовая модель времени и пространства",
        "phase": "temporal-spatial",
        "dependencies": [],
        "author": "Arctur",
    },
    "phase": {
        "description": "Базовая логика фаз и переходов",
        "phase": "logical-core",
        "dependencies": ["chronotope"],
        "author": "Arctur",
    }
}

def get_module_header(name):
    return MODULES.get(name, {})
