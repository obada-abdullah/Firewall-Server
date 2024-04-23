import logging

# Configure logging
logging.basicConfig(filename='firewall.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def log_info(message):
    """Log an informational message."""
    logging.info(message)

def log_warning(message):
    """Log a warning message."""
    logging.warning(message)

def log_error(message):
    """Log an error message."""
    logging.error(message)

def log_debug(message):
    """Log a debug message."""
    logging.debug(message)
