from setuptools import setup, find_packages

setup(
    name="ArcaLang",
    version="0.1",
    description="ArcaLang — экспериментальная библиотека для фазовых операторов, протоформ и резонансных моделей",
    author="Arctur",
    packages=find_packages(include=[
        "arca_langlib*",
        "arca_core*",
        "arca_fieldcore*",
        "arca_memory*",
        "phase_agent*",
        "phases*",
        "tests*"
    ]),
    install_requires=[
        # сюда можно добавить зависимости, если они нужны
        # например: "numpy", "pytest"
    ],
    python_requires=">=3.9",
)


