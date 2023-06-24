import logging

logger = logging.getLogger(__name__)


def calculate_length(dx: float, dy: float) -> float:
    length = (dx**2 + dy**2)**(1/2)
    logger.info(f'dx: {dx: .3f}, dy: {dy: .3f}, length: {length: .3f}')
    return length
