# Not a cog
import logging


def log(message, level='0'):
    logging.basicConfig(filename='logs.log', level=logging.INFO)
    levels = {
        '0': logging.info,
        '1': logging.warning,
        '2': logging.error}
    levels[level](message)
