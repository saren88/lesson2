from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
from datetime import datetime
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Enter planet name.'
    logging.info(text)
    update.message.reply_text(text)


def planet_constellation(bot, update):
    msg = update.message.text
    if msg == 'Jupiter':
        jupiter = ephem.Jupiter(datetime.now())
        jupiter_constellation = "Planet {}" \
                                " now in {} " \
                                "constellation.".format(msg,
                                                        ephem.constellation(
                                                            jupiter)
                                                        )
        update.message.reply_text(jupiter_constellation)
    elif msg == 'Mars':
        mars = ephem.Mars(datetime.now())
        mars_constellation = "Planet {}" \
                             " now in {} " \
                             "constellation.".format(msg,
                                                     ephem.constellation(
                                                         mars)
                                                     )
        update.message.reply_text(mars_constellation)
    elif msg == 'Uranus':
        uranus = ephem.Uranus(datetime.now())
        uranus_constellation = "Planet {}" \
                               " now in {} " \
                               "constellation.".format(msg,
                                                       ephem.constellation(
                                                           uranus)
                                                       )
        update.message.reply_text(uranus_constellation)
    logging.info(msg)


def main():
    my_bot = Updater(settings.API_KEY,
                     request_kwargs=settings.PROXY
                     )
    logging.info('Bot launching')

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('planet', greet_user))
    dp.add_handler(MessageHandler(Filters.text, planet_constellation))

    my_bot.start_polling()
    my_bot.idle()


main()
