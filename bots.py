from telegram import Bot, Update
from telegram.ext import Application, ChatJoinRequestHandler

# Bot token yahan add karein
BOT_TOKEN = "7525049474:AAHzZHYDZ-nseUuhTHMWh35iHyHKrp23Yi0"

async def approve_join_request(update: Update, context):
    """Approve new join requests for groups and channels."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    print(f"Join request received from user {user_id} in chat {chat_id}")

    try:
        # Join request approve karte hain
        await context.bot.approve_chat_join_request(chat_id=chat_id, user_id=user_id)
        print(f"Approved join request for user: {user_id}")
    except Exception as e:
        print(f"Error while approving user {user_id}: {e}")

def main():
    # Application initialize karein
    application = Application.builder().token(BOT_TOKEN).build()

    # ChatJoinRequestHandler add karein
    application.add_handler(ChatJoinRequestHandler(approve_join_request))

    print("Bot is running...")
    application.run_polling()  # Directly call run_polling without asyncio.run()

if __name__ == "__main__":
    main()
