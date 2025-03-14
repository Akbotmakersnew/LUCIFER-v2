from pyrogram import errors
import logging

logging.basicConfig(level=logging.ERROR)

async def handle_peer_error(client, reqstr1) -> None:
    try:
        reqstr = await client.get_users(reqstr1)
        return reqstr
    except ValueError as e:
        logging.error(f"Error: {e}")
        if "Peer id invalid" in str(e):
            print("Error: Invalid peer ID.")
        return None

def handle_photo_send_error(app, chat_id, photo) -> None:
    try:
        app.send_photo(chat_id, photo)
    except errors.Forbidden as e:
        logging.error(f"Error: {e}")
        if "CHAT_SEND_PHOTOS_FORBIDDEN" in str(e):
            print("Bot is not allowed to send photos in this chat.")
