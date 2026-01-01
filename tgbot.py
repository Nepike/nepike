import yaml
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from nepike_website.settings.base import BASE_DIR
import django



CONFIG_PATH = BASE_DIR/'config.yml'
with open(CONFIG_PATH) as f:
	SITE_CONFIG = yaml.safe_load(f.read())


bot = telebot.TeleBot(SITE_CONFIG["telegram_bot"]["token"])


@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message, "Бот онлайн!")


@bot.message_handler(commands=['get_chat_id'])
def get_chat_id(message):
	bot.reply_to(message, f"Chat: `{message.chat.id}`\nThread: `{message.message_thread_id}`", parse_mode="MarkdownV2")


if __name__ == "__main__":
	if SITE_CONFIG["env"] == 'dev':
		os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nepike_website.settings.dev')
	else:
		os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nepike_website.settings.prod')
	django.setup()

	bot.infinity_polling()


