import logging
import logging.config
from myconfig import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('library')


def calculate_length(dx: float, dy: float) -> float:
    length = (dx**2 + dy**2)**(1/2)
    logger.info(f'dx: {dx: .3f}, dy: {dy: .3f}, length: {length: .3f}')
    return length
