import os
from dotenv import load_dotenv
from loguru import logger
from utils.data_reader import open_list_gup
from utils.file_operations import create_folder, create_md_file
from utils.chat_gigachat import get_gigachat_response

# Загрузка переменных окружения
load_dotenv(dotenv_path='settings/config.env')
GIGA_CHAT = os.getenv('GIGA_CHAT')

# Настройка логирования
logger.add("logs/app.log", format="{time} {level} {message}", level="INFO", rotation="1 MB")


def main():
    """
    Основная функция программы.
    Получает данные из Excel, отправляет запросы в GigaChat
    и сохраняет результаты в Markdown файлы.
    """
    logger.info("Запуск программы")
    try:
        # Получаем данные из Excel
        list_gup = open_list_gup('file.xlsx')

        # Обработка каждого участка и профессии
        for plot, work in list_gup:
            logger.info(f"Обработка участка: {plot}, профессии: {work}")

            # Создаем папку для участка
            folder_path = f'test/{plot}'
            create_folder(folder_path)

            # Формируем запрос к GigaChat
            system_prompt = f"Расскажите, чем занимается данная профессия на предприятии: Участок: {plot}, Профессия: {work}"
            response = get_gigachat_response(GIGA_CHAT, system_prompt)

            # Сохраняем ответ в файл
            file_path = f'{folder_path}/{work}'
            create_md_file(file_path, response)

    except Exception as e:
        logger.exception(f"Ошибка в программе: {e}")


if __name__ == "__main__":
    main()
