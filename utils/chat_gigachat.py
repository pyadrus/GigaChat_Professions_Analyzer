from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
from loguru import logger


def get_gigachat_response(token, prompt):
    """
    Отправляет запрос в GigaChat и возвращает ответ.

    :param token: Токен доступа GigaChat.
    :param prompt: Текст запроса для GigaChat.
    :return: Ответ от GigaChat.
    """
    try:
        # Инициализация GigaChat
        llm = GigaChat(
            credentials=token,
            scope="GIGACHAT_API_PERS",
            model="GigaChat",
            verify_ssl_certs=False,
            streaming=False,
        )

        # Формирование сообщений
        messages = [
            SystemMessage(content=prompt),
            HumanMessage(content=""),
        ]

        # Отправка запроса
        response = llm.invoke(messages)
        return response.content

    except Exception as e:
        logger.exception("Ошибка при работе с GigaChat")
        return "Ошибка при работе с GigaChat"
