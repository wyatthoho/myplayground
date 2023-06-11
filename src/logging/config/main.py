import logging
import logging.config
from myconfig import LOGGING_CONFIG

from library import calculate_length


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('main')


if __name__ == '__main__':
    logger.info('Start.')
    vectors = [(1, 2), (3, 4), (5, 6)]
    lengths = [calculate_length(*vec) for vec in vectors]
    logger.info('End.')
