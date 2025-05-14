import logging

def setup_logger():
    logging.basicConfig(
        filename='bot.log',# Logs will be saved to file bot.log.
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
