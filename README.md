# Telegram Bot Forwarder

## Description
A Telegram bot built with Python that forwards all posts, including text, stickers, photos, videos, and other media, along with embedded buttons and text styles (bold, italic, quote) from one Telegram channel to another. If a post is edited in the source channel, the same will be updated in the destination channel. Includes Flask to handle potential "no ports detected" errors and keep the bot running.

## Installation

1. **Clone the repo:**
    ```bash
    git clone https://github.com/yourusername/telegram-bot-forwarder.git
    cd telegram-bot-forwarder
    ```

2. **Create a virtual environment and activate it (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Telegram Bot:**
   - Create a new bot with [BotFather](https://t.me/BotFather) to get your bot token.
   - Replace `YOUR_TOKEN` in `config.py` with your actual bot token.

5. **Configure API ID and API Hash:**
   - Create an application on [my.telegram.org](https://my.telegram.org) to get your API ID and API hash.
   - Replace `YOUR_API_ID` and `YOUR_API_HASH` in `config.py`.

6. **Run the bot:**
    ```bash
    python bot.py
    ```

## Configuration

Create a file named `config.py` and add your configuration settings:
```python
TOKEN = '8037292838:AAEDLk3P7KEq9s3bMuWNtcTqYxvMBnCO0tE'
SOURCE_CHANNEL_ID = -1002176961000  # Replace with your source channel ID
DESTINATION_CHANNEL_ID = -1002352652618  # Replace with your destination channel ID
API_ID = '26684254'
API_HASH = 'fc836096a68be3a4fcd7594cb3d9326f'
MESSAGE_MAP = {}
