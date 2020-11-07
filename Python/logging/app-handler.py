import logging
import logging.handlers


# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('handler.log')
time_rotating_handler = logging.handlers.TimedRotatingFileHandler('time-rotating-handler.log')

# Create formatters
console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(levelname)s - %(message)s')
time_rotating_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the format for handlers
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)
time_rotating_handler.setFormatter(time_rotating_format)

# Set the log level for handlers
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
time_rotating_handler.setLevel(logging.INFO)

# Get a logger
logger = logging.getLogger(__name__)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(time_rotating_handler)

if __name__ == "__main__":
    logger.info('info')
    logger.warning('warning')
