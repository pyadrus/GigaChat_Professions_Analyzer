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




def system_prompt(work):
    """Промпт для ИИ"""
    return f"Расскажите, чем занимается данная профессия на предприятии: {work}"


def get_chat_completion_gigachat():
    """Получение ответа от GigaChat."""

    # Получаем данные из таблицы Excel
    list_gup = open_list_gup()
    for i in list_gup:
        plot = i[0]
        work = i[1]
        print(f"Участок: {plot}, Профессия: {work}")


    try:
        # Создание экземпляра модели GigaChat
        llm = GigaChat(
            credentials=GIGA_CHAT,
            scope="GIGACHAT_API_PERS",
            model="GigaChat",
            verify_ssl_certs=False,
            streaming=False,
        )

        work = "Начальник участка"  # Профессия, которую мы хотим рассмотреть

        # Формирование сообщения для отправки в модель
        messages = [
            SystemMessage(content=system_prompt(work)),
            HumanMessage(content=""),  # Здесь должно быть сообщение пользователя, но у вас оно пустое
        ]

        response = llm.invoke(messages)  # Отправка запроса и получение ответа

        return response.content

    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    answer = get_chat_completion_gigachat()
    print(answer)
