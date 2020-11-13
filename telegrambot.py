import logging
import paswdgen

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hello, I am a random password generator Type /paswd to generate a random password')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def paswd(update, context):
    """Echo the user message."""
    update.message.reply_text(paswdgen.keygen())


def main():
    updater = Updater("API-KEY", use_context=True)
  
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(CommandHandler("paswd",paswd))
  
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()