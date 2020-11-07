import logging


logging.basicConfig(
    filename='app-basic.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
