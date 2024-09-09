from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram.ext import Filters, MessageHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define command handlers
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your auction bot. Use /startauction to begin.')

def startauction(update: Update, context: CallbackContext):
    update.message.reply_text('Auction started! Type /bid <amount> to place your bid.')

def bid(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    bid_amount = ' '.join(context.args)
    if bid_amount.isdigit():
        update.message.reply_text(f'Bid of {bid_amount} received from user {user_id}.')
        # Here, you would typically handle the auction logic
    else:
        update.message.reply_text('Please provide a valid bid amount.')

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater("7037927156:AAHfeEu-vsLQYOpRR5RrrbgXIBeY4bwjiHs", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("startauction", startauction))
    dp.add_handler(CommandHandler("bid", bid))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
