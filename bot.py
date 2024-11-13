import logging
from flask import Flask, request
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import commands, message, error
from config import API_ID, API_HASH, TOKEN, SOURCE_CHANNEL_ID, DESTINATION_CHANNEL_ID

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize bot forwarding status
is_forwarding = False

def main():
    global is_forwarding
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", commands.start))
    dp.add_handler(CommandHandler("help", commands.help))
    dp.add_handler(CommandHandler("start_forwarding", commands.start_forwarding))
    dp.add_handler(CommandHandler("stop_forwarding", commands.stop_forwarding))

    # Message handler
    dp.add_handler(MessageHandler(Filters.chat(SOURCE_CHANNEL_ID) & Filters.all, message.forward_message))

    # Error handler
    dp.add_error_handler(error.error)

    # Start the Bot
    updater.start_polling()
    logger.info("Bot started polling.")

    @app.route('/')
    def index():
        return 'Bot is running.'

    @app.route('/webhook', methods=['POST'])
    def webhook():
        if request.method == 'POST':
            update = request.get_json()
            updater.update_queue.put(update)
            return 'OK'
    
    app.run(port=5000)

if __name__ == '__main__':
    main()
