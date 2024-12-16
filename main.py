import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
from loguru import logger
import openpyxl as op

# Загрузка переменных окружения из файла .env
load_dotenv(dotenv_path='settings/config.env')

# Получение токена доступа к GigaChat из переменной окружения
GIGA_CHAT = os.getenv('GIGA_CHAT')
logger.info(f'GIGA_CHAT: {GIGA_CHAT}')


def open_list_gup():
    """"Открытие таблицы и чтение данных с таблицы Excel"""
    wb = op.load_workbook('file.xlsx')
    ws = wb.active
    list_gup = []

    for row in ws.iter_rows(min_row=1, max_row=68, min_col=1, max_col=2):
        row_data = [cell.value for cell in row]
        list_gup.append(row_data)
        print(row_data)

    return list_gup


def create_folder(folder_name):
    """Создание папки с указанным именем"""
    try:
        os.makedirs(folder_name)
        print(f"Папка {folder_name} успешно создана")
    except FileExistsError:
        print(f"Папка {folder_name} уже существует")


def create_md_file(file_name, content=""):
    """Создание файла с расширением .md"""
    os.makedirs(os.path.dirname(f"{file_name}.md"), exist_ok=True)  # Создаем все необходимые папки, если их нет
    with open(f"{file_name}.md", 'w', encoding='utf-8') as f:
        f.write(content)
    logger.info(f"Файл {file_name}.md создан.")


def get_chat_completion_gigachat():
    """Получение ответа от GigaChat."""

    # Получаем данные из таблицы Excel
    list_gup = open_list_gup()
    for i in list_gup:
        plot = i[0] # Участок
        work = i[1] # Профессия
        print(f"Участок: {plot}, Профессия: {work}")

        create_folder(f'test/{plot}')

        try:
            # Создание экземпляра модели GigaChat
            llm = GigaChat(
                credentials=GIGA_CHAT,
                scope="GIGACHAT_API_PERS",
                model="GigaChat",
                verify_ssl_certs=False,
                streaming=False,
            )

            system_prompt = f"Расскажите, чем занимается данная профессия на предприятии: Участок: {plot}, Профессия: {work}"  # Профессия, которую мы хотим рассмотреть

            # Формирование сообщения для отправки в модель
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=""),  # Здесь должно быть сообщение пользователя, но у вас оно пустое
            ]

            response = llm.invoke(messages)  # Отправка запроса и получение ответа

            print(response.content)
            create_md_file(f'test/{plot}/{work}', response.content)

        except Exception as e:
            logger.exception(e)


if __name__ == "__main__":
    get_chat_completion_gigachat()
