from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
from datetime import datetime
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)


def greet_user(bot, update):
    text = 'Enter planet name.'
    logging.info(text)
    update.message.reply_text(text)


def planet_constellation(bot, update):
    msg = update.message.text
    if hasattr(ephem, msg.capitalize()):
        planet = getattr(ephem, msg.capitalize())(datetime.now())
        planet_message = "Planet {} now in {} constellation.".format(
            msg,
            ephem.constellation(planet)
        )
        update.message.reply_text(planet_message)
    logging.info(msg)


def main():
    my_bot = Updater(
        settings.API_KEY,
        request_kwargs=settings.PROXY
                     )
    logging.info('Bot launching')

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('planet', greet_user))
    dp.add_handler(MessageHandler(Filters.text, planet_constellation))

    my_bot.start_polling()
    my_bot.idle()

if __name__ == '__main__':
    main()
