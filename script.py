import os
from git import Repo

# Укажите путь к вашему git репозиторию
repo_path = os.getcwd()


# Укажите пути к файлам для сохранения результатов
structure_file = 'structure.txt'
content_file = 'content.txt'

def save_structure_and_content(repo_path, structure_file, content_file):
    # Инициализация репозитория
    repo = Repo(repo_path)
    
    # Проверка, что это git репозиторий
    if repo.bare:
        print("Это не git репозиторий")
        return
    
    with open(structure_file, 'w') as sf, open(content_file, 'w') as cf:
        for root, dirs, files in os.walk(repo_path):
            # Исключаем .git директорию
            if '.git' in root:
                continue
            
            # Записываем структуру каталогов и файлов
            level = root.replace(repo_path, '').count(os.sep)
            indent = ' ' * 4 * level
            sf.write(f'{indent}{os.path.basename(root)}/\n')
            
            for f in files:
                sf.write(f'{indent}    {f}\n')
                
                # Записываем содержимое файлов
                file_path = os.path.join(root, f)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    cf.write(f'File: {file_path}\n')
                    cf.write(content)
                    cf.write('\n\n')

if __name__ == "__main__":
    save_structure_and_content(repo_path, structure_file, content_file)
