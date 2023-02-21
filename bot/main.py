import telebot
from googletrans import Translator
from gtts import gTTS
import os

# Replace the API_TOKEN with your own Telegram bot token
bot = telebot.TeleBot('6049623024:AAHNCkJ85dlPPIQFLf9uYvbhVwiV67MkwAM')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "أكتب أي شيء بالعربية، وانتظر قليلاً")

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    if message.text:
        translator = Translator()
        text_to_translate = message.text
        translated_text = translator.translate(text_to_translate, src='ar', dest='ja').text
        
        # Generate an audio file for the translated text
        tts = gTTS(text=translated_text, lang='ja')
        tts.save('audio.mp3')
        
        # Send the audio file as a voice message to the user along with the translated text
        audio_file = open('audio.mp3', 'rb')
        bot.send_voice(message.chat.id, audio_file, caption=translated_text)
        audio_file.close()
        
        # Delete the audio file from disk
        os.remove('audio.mp3')

bot.polling()
