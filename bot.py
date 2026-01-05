import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your API Token
API_TOKEN = 8308872349:AAGCV12tdEGgqwC3g_pdoAfRbAMqwd7EdnE

# Command to start the bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your bot. How can I help you?")

# Echo back the user's message
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

# Main function to start the bot
def main():
    # Initialize Updater and Dispatcher
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    # Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()