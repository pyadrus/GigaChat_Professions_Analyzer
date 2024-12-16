import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
from loguru import logger

# Загрузка переменных окружения из файла .env
load_dotenv(dotenv_path='settings/config.env')

# Получение токена доступа к GigaChat из переменной окружения
GIGA_CHAT = os.getenv('GIGA_CHAT')
logger.info(f'GIGA_CHAT: {GIGA_CHAT}')


def system_prompt(work):
    """Промпт для ИИ"""
    return f"Расскажите, чем занимается данная профессия на предприятии: {work}"


def get_chat_completion_gigachat():
    """Получение ответа от GigaChat."""
    try:
        # Создание экземпляра модели GigaChat
        llm = GigaChat(
            credentials=GIGA_CHAT,
            scope="GIGACHAT_API_PERS",
            model="GigaChat",
            verify_ssl_certs=False,
            streaming=False,
        )

        # Профессия, которую мы хотим рассмотреть
        work = "Начальник участка"

        # Формирование сообщения для отправки в модель
        messages = [
            SystemMessage(content=system_prompt(work)),
            HumanMessage(content=""),  # Здесь должно быть сообщение пользователя, но у вас оно пустое
        ]

        # Отправка запроса и получение ответа
        response = llm.invoke(messages)
        logger.debug(response.content)

        return response.content

    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    answer = get_chat_completion_gigachat()
    print(answer)