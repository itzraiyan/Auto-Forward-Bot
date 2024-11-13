def start(update, context):
    update.message.reply_text('Hello! I am a forwarding bot. Use /help to see what I can do.')

def help(update, context):
    update.message.reply_text('Commands:\n/start - Start the bot\n/help - Show this help message')

SOURCE_CHANNEL_ID = -1002176961000  # Replace with your source channel ID
