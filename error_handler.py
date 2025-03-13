from pyrogram import errors

def handle_forbidden_error(app, chat_id, photo):
    try:
        app.send_photo(chat_id, photo)
    except errors.Forbidden as e:
        if "CHAT_SEND_PHOTOS_FORBIDDEN" in str(e):
            print("Bot is not allowed to send photos in this chat.")
        else:
            print(f"Error: {e}")
