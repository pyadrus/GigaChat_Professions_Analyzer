import os

from loguru import logger


def create_folder(folder_name):
    """
    Создает папку, если она не существует.

    :param folder_name: Путь к создаваемой папке.
    """
    try:
        os.makedirs(folder_name, exist_ok=True)
        logger.info(f"Папка {folder_name} успешно создана")
    except Exception as e:
        logger.error(f"Ошибка при создании папки {folder_name}: {e}")


def create_md_file(file_name, content=""):
    """
    Создает Markdown файл и записывает в него данные.

    :param file_name: Путь к файлу без расширения.
    :param content: Текст для записи в файл.
    """
    try:
        os.makedirs(os.path.dirname(f"{file_name}.md"), exist_ok=True)
        with open(f"{file_name}.md", 'w', encoding='utf-8') as f:
            f.write(content)
        logger.info(f"Файл {file_name}.md успешно создан.")
    except Exception as e:
        logger.error(f"Ошибка при создании файла {file_name}.md: {e}")
