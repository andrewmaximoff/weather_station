import logging
import os

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler)

from bot.bot_comm import BotCommand


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, err):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, err)


class Bot(BotCommand):
    def __init__(self, TOKEN):
        self.TOKEN = TOKEN or os.environ.get('TOKEN')
        self.updater = Updater(self.TOKEN)

        dp = self.updater.dispatcher

        super().__init__(dp)

        # log all errors
        dp.add_error_handler(error)

    def start(self):
        logging.info('Bot start polling!')
        self.updater.start_polling()
        self.updater.idle()


if __name__ == '__main__':
    bot = Bot()
    bot.start()
