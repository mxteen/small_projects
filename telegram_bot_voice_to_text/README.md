# Telegram Voice-to-Text Bot

This is a simple Telegram bot that converts voice messages into text using the Google Speech Recognition API. The bot is implemented in Python and utilizes the Telebot, SpeechRecognition, and Pydub libraries.

## Prerequisites

Before running the bot, make sure you have the required Python libraries installed. You can install them using the following command:

```bash
pip install pyTelegramBotAPI SpeechRecognition pydub
```

or

```bash
pip install -r requirements.txt
```

Also, ensure that you have a Telegram bot token. You can obtain one by talking to [@BotFather](https://t.me/BotFather) on Telegram.

## Setup

1. Clone this repository:

2. Create a file named `token.txt` in the project directory and paste your Telegram bot token into it.

3. Run the bot.

## Usage

1. Start a conversation with the bot on Telegram.

2. Send a voice message to the bot.

3. The bot will convert the voice message to text and reply with the transcribed text.

## Important Note

This bot uses the Google Speech Recognition API, which requires an internet connection. Ensure that your device is connected to the internet for the bot to work properly.

## Disclaimer

This bot is provided as-is, and the developers are not responsible for any misuse or damage caused by its use. Make sure to comply with Telegram's [terms of service](https://telegram.org/tos) and policies when using this bot.
