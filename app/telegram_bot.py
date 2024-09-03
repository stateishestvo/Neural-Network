from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters
import model

TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(TELEGRAM_TOKEN)

def set_webhook():
    bot.set_webhook("YOUR_WEBHOOK_URL")

def delete_webhook():
    bot.delete_webhook()

def process_update(data):
    update = Update.de_json(data, bot)
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.process_update(update)

def echo(update: Update, context):
    message_text = update.message.text
    response_text = model.generate_response(message_text)
    update.message.reply_text(response_text)