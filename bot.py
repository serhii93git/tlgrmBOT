import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Updater, Application, ContextTypes

#  load and get the environment variables from the .env file
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


# '/start' command handler
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello!')


# '/help' command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Help text here')


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()

    # Command handlers list
    handlers = [
        CommandHandler('start', start_command),
        CommandHandler('help', help_command),
    ]

    # Register command handlers
    app.add_handlers(handlers)

    # Starting the bot
    app.run_polling()


if __name__ == '__main__':
    main()
