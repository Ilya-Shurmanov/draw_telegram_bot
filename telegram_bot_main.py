import os
from telegram.ext import Updater, MessageHandler, filters


# Retrieve the API token from the environment variable
API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')

def handle_message(update, context):
    """Callback function for handling messages"""
    message = update.message.text
    if 'Hi' in message:
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=chat_id, text='Hello')

# Create an Updater instance using the API token
updater = Updater(token=API_TOKEN)

# Register the callback function for handling messages
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(filters.text & (~filters.command), handle_message))

# Start the bot
updater.start_polling()