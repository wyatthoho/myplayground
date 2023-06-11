import logging
from library import calculate_length

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename='info.log', mode='w')
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt='%(asctime)s,%(msecs)03d [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


if __name__ == '__main__':
    logger.info('Start.')
    vectors = [(1, 2), (3, 4), (5, 6)]
    lengths = [calculate_length(*vec) for vec in vectors]
    logger.info('End.')
