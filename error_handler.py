from pyrogram import errors

async def handle_peer_id_error(client, reqstr1):
    try:
        reqstr = await client.get_users(reqstr1)
        return reqstr
    except ValueError as e:
        if "Peer id invalid" in str(e):
            print("Error: Invalid peer ID.")
        else:
            print(f"Error: {e}")
        return None
        
def handle_forbidden_error(app, chat_id, photo):
    try:
        app.send_photo(chat_id, photo)
    except errors.Forbidden as e:
        if "CHAT_SEND_PHOTOS_FORBIDDEN" in str(e):
            print("Bot is not allowed to send photos in this chat.")
        else:
            print(f"Error: {e}")
