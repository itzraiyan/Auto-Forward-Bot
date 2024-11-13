from telegram import Update
from telegram.ext import CallbackContext

# Initialize forwarding status
is_forwarding = False

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am a forwarding bot. Use /help to see what I can do.')

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Commands:\n/start - Start the bot\n/help - Show this help message\n/start_forwarding - Start forwarding messages\n/stop_forwarding - Stop forwarding messages')

def start_forwarding(update: Update, context: CallbackContext) -> None:
    global is_forwarding
    if not is_forwarding:
        is_forwarding = True
        update.message.reply_text('Started forwarding messages.')
    else:
        update.message.reply_text('Already forwarding messages.')

def stop_forwarding(update: Update, context: CallbackContext) -> None:
    global is_forwarding
    if is_forwarding:
        is_forwarding = False
        update.message.reply_text('Stopped forwarding messages.')
    else:
        update.message.reply_text('Not currently forwarding messages.')

SOURCE_CHANNEL_ID = -1002176961000  # Replace with your source channel ID
