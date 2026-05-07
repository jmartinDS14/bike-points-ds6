from modules.setup_logging import setup_logging
from modules.extract_function import extract
from modules.load_function import load
from pathlib import Path
from dotenv import load_dotenv
import os

logger = setup_logging('logs')
logger.info('Logger initialised')

url = "https://api.tfl.gov.uk/BikePoint/"

load_dotenv()
AWS_KEY_ID = os.getenv('AWS_KEY_ID')
AWS_SECRET_KEY=os.getenv('AWS_SECRET_KEY')
bucket=os.getenv('bucket')

if extract(url, 3, 'data'):
    data_dir = Path('data')
    load(AWS_KEY_ID, AWS_SECRET_KEY, bucket, data_dir)
    logger.info('Script ran successfully')
else:
    logger.error('Extract failed so script stopped.')