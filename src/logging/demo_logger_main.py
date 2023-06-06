import logging
from demo_logger_lib import calculate_length

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

filename = __file__.split('.')[0] + '.log'
file_handler = logging.FileHandler(filename=filename, mode='w')
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


if __name__ == '__main__':
    logger.info('Start.')
    vectors = [(1, 2), (3, 4), (5, 6)]
    lengths = [calculate_length(*vec) for vec in vectors]
    logger.info('End.')
