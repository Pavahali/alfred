# Not a cog
import settings
import logging


def log(message, level='0'):
    logging.basicConfig(filename=settings.logs, level=logging.INFO)
    levels = {
        '0': logging.info,
        '1': logging.warning,
        '2': logging.error}
    levels[level](message)
