import os
import json
from pathlib import Path

def load_gitignore(path='.gitignore'):
    """Загружает и возвращает список игнорируемых путей из .gitignore."""
    ignore_list = []
    if os.path.exists(path):
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_list.append(line)
    return ignore_list

def is_ignored(file_path, ignore_list):
    """Проверяет, игнорируется ли файл или директория."""
    for pattern in ignore_list:
        if Path(file_path).match(pattern):
            return True
    return False

def is_text_file(file_path):
    """Проверяет, является ли файл текстовым."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read(1024)
        return True
    except Exception:
        return False

def analyze_project(directory='.', exclude_dirs=None, exclude_extensions=None):
    """Анализирует все файлы в каталоге проекта и возвращает их в JSON-структуре."""
    if exclude_dirs is None:
        exclude_dirs = []
    if exclude_extensions is None:
        exclude_extensions = []

    ignore_list = load_gitignore()
    project_files = []

    for root, dirs, files in os.walk(directory):
        # Исключаем указанные каталоги
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]

        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), directory)
            file_extension = file.split('.')[-1]

            # Пропускаем файлы с указанными расширениями
            if file_extension in exclude_extensions:
                continue

            if not is_ignored(file_path, ignore_list):
                full_path = os.path.join(root, file)
                if is_text_file(full_path):
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()  # Читаем все содержимое текстового файла
                else:
                    content = None  # Не включаем содержимое двоичных файлов
                project_files.append({
                    "path": file_path,
                    "type": file_extension,
                    "content": content
                })

    return {
        "projectName": os.path.basename(os.path.abspath(directory)),
        "files": project_files
    }

if __name__ == "__main__":
    # Укажите каталоги, которые нужно исключить из обработки
    exclude_dirs = ['node_modules', 'dist', '.git']
    # Укажите расширения файлов, которые нужно исключить из обработки
    exclude_extensions = ['png', 'jpg', 'exe', 'json', 'map', 'env']

    project_structure = analyze_project(exclude_dirs=exclude_dirs, exclude_extensions=exclude_extensions)
    with open('project_structure.json', 'w', encoding='utf-8') as json_file:
        json.dump(project_structure, json_file, ensure_ascii=False, indent=4)
    print("Проект успешно проанализирован и сохранен в project_structure.json")
