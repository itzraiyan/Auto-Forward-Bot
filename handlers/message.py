from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from config import SOURCE_CHANNEL_ID, DESTINATION_CHANNEL_ID, MESSAGE_MAP

def forward_message(update, context):
    message = update.message
    if message.chat.id == SOURCE_CHANNEL_ID:
        forwarded_message = None
        if message.text:
            forwarded_message = context.bot.send_message(
                chat_id=DESTINATION_CHANNEL_ID,
                text=message.text,
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=message.reply_markup
            )
        elif message.sticker:
            forwarded_message = context.bot.send_sticker(
                chat_id=DESTINATION_CHANNEL_ID,
                sticker=message.sticker.file_id
            )
        elif message.photo:
            forwarded_message = context.bot.send_photo(
                chat_id=DESTINATION_CHANNEL_ID,
                photo=message.photo[-1].file_id,
                caption=message.caption,
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=message.reply_markup
            )
        elif message.video:
            forwarded_message = context.bot.send_video(
                chat_id=DESTINATION_CHANNEL_ID,
                video=message.video.file_id,
                caption=message.caption,
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=message.reply_markup
            )
        elif message.document:
            forwarded_message = context.bot.send_document(
                chat_id=DESTINATION_CHANNEL_ID,
                document=message.document.file_id,
                caption=message.caption,
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=message.reply_markup
            )
        elif message.audio:
            forwarded_message = context.bot.send_audio(
                chat_id=DESTINATION_CHANNEL_ID,
                audio=message.audio.file_id,
                caption=message.caption,
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=message.reply_markup
            )
        elif message.voice:
            forwarded_message = context.bot.send_voice(
                chat_id=DESTINATION_CHANNEL_ID,
                voice=message.voice.file_id,
                caption=message.caption,
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=message.reply_markup
            )
        elif message.video_note:
            forwarded_message = context.bot.send_video_note(
                chat_id=DESTINATION_CHANNEL_ID,
                video_note=message.video_note.file_id,
                reply_markup=message.reply_markup
            )
        
        if forwarded_message:
            MESSAGE_MAP[message.message_id] = forwarded_message.message_id

def edit_message(update, context):
    edited_message = update.edited_message
    if edited_message.chat.id == SOURCE_CHANNEL_ID:
        dest_message_id = MESSAGE_MAP.get(edited_message.message_id)

        if dest_message_id:
            if edited_message.text:
                context.bot.edit_message_text(
                    chat_id=DESTINATION_CHANNEL_ID,
                    message_id=dest_message_id,
                    text=edited_message.text,
                    parse_mode=ParseMode.MARKDOWN_V2,
                    reply_markup=edited_message.reply_markup
                )
            elif edited_message.caption:
                context.bot.edit_message_caption(
                    chat_id=DESTINATION_CHANNEL_ID,
                    message_id=dest_message_id,
                    caption=edited_message.caption,
                    parse_mode=ParseMode.MARKDOWN_V2,
                    reply_markup=edited_message.reply_markup
                )
