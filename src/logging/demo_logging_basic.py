'''Reference: 
1. https://docs.python.org/3/library/logging.html
2. https://docs.python.org/3/howto/logging.html
'''
import logging


logging.basicConfig(
    filename=f'{__file__}.log',
    filemode='w',
    level=logging.WARNING
)


def calculate_length(dx: float, dy: float) -> float:
    return (dx**2 + dy**2)**(1/2)


# Level 1: debug
dx, dy = 3.0, 4.0
length = calculate_length(dx, dy)
logging.debug(f'dx: {dx}, dy: {dy}, length: {length}')


# Level 2: info
dx, dy = 3.0, 4.0
length = calculate_length(dx, dy)
logging.info('Calculation is completed.')


# Level 3: warning
dx, dy = 3, 4
if type(dx) != float:
    logging.warning('The type of dx should be float.')
if type(dy) != float:
    logging.warning('The type of dx should be float.')
length = calculate_length(dx, dy)


# Level 4: error
dx, dy = 3.0, 4.0
length = calculate_length(dx, dy)
if length < max(dx, dy):
    logging.error(f'Calculation error!')


# Level 5: critical
dx, dy = '3', 4
try:
    length = calculate_length(dx, dy)
except Exception as e:
    logging.critical(f'{e}')
