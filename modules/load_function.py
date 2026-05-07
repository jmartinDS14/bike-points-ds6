import boto3
import logging
import os

logger = logging.getLogger(__name__)

def load(AWS_KEY_ID, AWS_SECRET_KEY, bucket, data_dir):
    """
    This will load any json files in the data directory to a specified S3 bucket.

    Args:
        AWS_KEY_ID (string): The AWS access key ID attached to an IAM User, with relevant permissions.
        AWS_SECRET_KEY (string): The AWS secret access key attached to an IAM User, with relevant permissions.
        bucket (string): The name of the S3 bucket
        data_dir (string): Must be a complete filepath for the directory where the data is located e.g. Path('data')
    """    
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    files = list(data_dir.glob('*.json'))

    processed = 0

    for file in files:
        filename = os.path.basename(file)
        try:
            s3_client.upload_file(file,bucket,filename)
            logger.info(f'{file} uploaded to S3 :)')
            s3_client.head_object(Bucket=bucket,Key=filename)
            os.remove(file)
            logger.info(f'{file} deleted locally')
            processed+=1
        except Exception as e:
            logger.error(e)
        
    logger.info(f'{processed} files uploaded')