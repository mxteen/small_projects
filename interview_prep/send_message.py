import logging
from random import choice
from secrets import CHAT_ID, TOKEN, QSTN_PATH, LOG_PATH
import requests

# SETTING UP LOGGER
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler(LOG_PATH)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def send_message(params: dict[str, str]) -> None:
    """
    Sends message with random python interview question to telegram chat.

    Args:
        text (str): _description_
        params (dict[str, str]): _description_
    """
    telegram_api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(telegram_api_url, params=params)
    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")

# Getting the questions
with open(QSTN_PATH) as f:
    questions = f.readlines()
question = choice(questions)

# Sending random question
send_message(params = {"chat_id": CHAT_ID, "text": question})
logger.info(question)
