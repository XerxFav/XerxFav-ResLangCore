#!/usr/bin/env python3
import os
import subprocess
import re

# 🔍 Найти конфликтные файлы
def get_conflicted_files():
    result = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=U'], capture_output=True, text=True)
    return result.stdout.strip().split('\n')

# 🧠 Подсветить конфликтные блоки
def highlight_conflicts(file_path):
    print(f"\n🧩 Файл: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    conflict_block = []
    in_conflict = False
    for line in lines:
        if line.startswith('<<<<<<<'):
            in_conflict = True
            conflict_block = [line]
        elif line.startswith('>>>>>>>'):
            conflict_block.append(line)
            in_conflict = False
            print("🔻 Конфликт:")
            for l in conflict_block:
                print(f"  {l.strip()}")
        elif in_conflict:
            conflict_block.append(line)

# 🧩 Предложить шаблон объединения
def suggest_resolution():
    print("\n📌 Шаблоны разрешения:")
    print("  [1] Оставить HEAD (текущую версию)")
    print("  [2] Оставить входящую версию")
    print("  [3] Объединить вручную")
    print("  [4] Применить к файлу автоматически (только HEAD)")

def apply_head_version(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Удалить входящую версию и маркеры
    resolved = re.sub(r'<<<<<<< HEAD\n(.*?)\n=======\n.*?\n>>>>>>>.*?\n', r'\1\n', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(resolved)

    subprocess.run(['git', 'add', file_path])
    print(f"✅ HEAD применён к {file_path}")

# 🚀 Основной запуск
def main():
    files = get_conflicted_files()
    if not files or files == ['']:
        print("✅ Нет конфликтных файлов.")
        return

    for file in files:
        highlight_conflicts(file)
        suggest_resolution()
        choice = input(f"Выбери шаблон для {file} [1-4]: ").strip()
        if choice == '4':
            apply_head_version(file)

    print("\n📦 После разрешения всех конфликтов, запусти:")
    print("  git rebase --continue")

if __name__ == "__main__":
    main()
