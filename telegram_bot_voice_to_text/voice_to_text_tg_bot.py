import os
import telebot
import speech_recognition
from pydub import AudioSegment

# Reading the token
with open('token.txt', 'r') as token_file:
    token = token_file.readline()

bot = telebot.TeleBot(token)

def oga_to_wav(filename):
    # Convert file formats
    new_filename = filename.replace('.oga', '.wav')
    audio = AudioSegment.from_file(filename)
    audio.export(new_filename, format='wav')
    return new_filename

def recognize_speech(oga_filename):
    # Convert voice to text + delete used files
    wav_filename = oga_to_wav(oga_filename)
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.WavFile(wav_filename) as source:
        wav_audio = recognizer.record(source)

    text = recognizer.recognize_google(wav_audio, language='ru')

    if os.path.exists(oga_filename):
        os.remove(oga_filename)

    if os.path.exists(wav_filename):
        os.remove(wav_filename)

    return text

def download_file(bot, file_id):
    # Download the file sent by the user
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    filename = file_id + file_info.file_path
    filename = filename.replace('/', '_')
    with open(filename, 'wb') as f:
        f.write(downloaded_file)
    return filename

@bot.message_handler(commands=['start'])
def say_hi(message):
    # Function sending "Hello" in response to the /start command
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(content_types=['voice'])
def transcript(message):
    # Function sending text in response to a voice message
    filename = download_file(bot, message.voice.file_id)
    text = recognize_speech(filename)
    bot.send_message(message.chat.id, text)

# Run the bot.
bot.polling()
