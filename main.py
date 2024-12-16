import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
from loguru import logger

load_dotenv(dotenv_path='settings/config.env')


GIGA_CHAT = os.getenv('GIGA_CHAT')
logger.info(f'GIGA_CHAT: {GIGA_CHAT}')  # GIGA_CHAT



def system_prompt(work):
    """Промт для ИИ"""

    return """Текущее время является нерабочим. Ваш запрос будет рассмотрен позже. Спасибо за понимание! 🕒📅"""


async def get_chat_completion_gigachat(message):
    """Возвращает ответ пользователя"""

    try:
        # Авторизация в GigaChat
        llm = GigaChat(credentials=GIGA_CHAT, scope="GIGACHAT_API_PERS", model="GigaChat",
                       # Отключает проверку наличия сертификатов НУЦ Минцифры
                       verify_ssl_certs=False,
                       streaming=False, )

        messages = [SystemMessage(content=system_prompt(work)), HumanMessage(content=message.text), ]

        response = llm.invoke(messages)
        print("GigaChat: ", response.content)

        return response.content
    except Exception as e:
        logger.exception(e)
