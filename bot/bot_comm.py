import os
import glob
import time


from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)


from get_temp import main as get_temp

categories_keyboard = [['Температура', 'Влажность', 'Освещенность']]
categories_markup = ReplyKeyboardMarkup(categories_keyboard)


class BotCommand(object):
    def __init__(self, dp):
        self.add_update_handlers(dp)

    def add_update_handlers(self, dp):
        dp.add_handler(CommandHandler('start', self._start))
        dp.add_handler(RegexHandler('^(Температура)$',
                                    self._temperature))
        dp.add_handler(CommandHandler('cancel', self._cancel, pass_user_data=True))

        return dp

    @staticmethod
    def _start(bot, update):
        """Beginning of communication between the bot and the user.
        Args:
            bot (:obj:`str`): This object represents a Telegram Bot.
            update (:class:`telegram.Update`): Incoming telegram update.
        """

        update.effective_message.reply_text("Go!", reply_markup=categories_markup)

    @staticmethod
    def _cancel(bot, update, user_data):
        bot.send_message(update.message.chat_id,
                         '/start',
                         reply_markup=categories_markup)
        user_data.clear()

    @staticmethod
    def _temperature(bot, update):
        bot.send_message(update.message.chat_id,
                         '{}°C'.format(get_temp()),
                         reply_markup=categories_markup)
