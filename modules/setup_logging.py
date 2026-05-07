import os
from datetime import datetime
import logging

def setup_logging(log_dir):
    """
    This function sets up the logging for all modules. Means we repeat ourselves less.

    Args:
        log_dir (string): The filepath that you want the log files to save to.
    """    
    os.makedirs(log_dir,exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_filename = f'{log_dir}/{timestamp}.log'

    logging.basicConfig(
        filename=log_filename,
        format= '%(asctime)s - %(name)s -  %(levelname)s - %(message)s',
        level=logging.INFO
    )

    return logging.getLogger('main')