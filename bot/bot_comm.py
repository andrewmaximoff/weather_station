from threading import Thread

from time import sleep
from gpiozero import InputDevice

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

from bot.bar import barometer
from bot.temp import temperature, humidity


categories_keyboard = [['Температура', 'Влажность', 'Атмосферное давление'],
                       ['Уведомление о дожде'],
                       ['Refresh']]
categories_markup = ReplyKeyboardMarkup(categories_keyboard)


class BotCommand(object):
    def __init__(self, dp):
        self.add_update_handlers(dp)

    def add_update_handlers(self, dp):
        dp.add_handler(CommandHandler('start', self._start))
        dp.add_handler(RegexHandler('^(Температура)$',
                                    self._temperature))
        dp.add_handler(RegexHandler('^(Влажность)$',
                                    self._humidity))
        dp.add_handler(RegexHandler('^(Атмосферное давление)$',
                                    self._barometer))
        dp.add_handler(RegexHandler('^(Уведомление о дожде)$',
                                    self._rain))
        dp.add_handler(RegexHandler('^(Refresh)$', self._cancel, pass_user_data=True))

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
                         '{}'.format(temperature()),
                         reply_markup=categories_markup)

    @staticmethod
    def _humidity(bot, update):
        bot.send_message(update.message.chat_id,
                         '{}'.format(humidity()),
                         reply_markup=categories_markup)

    @staticmethod
    def _barometer(bot, update):
        bot.send_message(update.message.chat_id,
                         '{}'.format(barometer()),
                         reply_markup=categories_markup)

    def _rain(self, bot, update):
        Thread(target=self.send_async_mass, args=(bot, update)).start()

    @staticmethod
    def send_async_mass(bot, update):
        no_rain = InputDevice(18)
        while True:
            if not no_rain.is_active:
                bot.send_message(update.message.chat_id,
                                 '{}'.format("It's raining - get the washing in!"),
                                 reply_markup=categories_markup)
                break
            sleep(1)


