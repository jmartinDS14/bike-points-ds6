from dotenv import load_dotenv
import os
import boto3

load_dotenv()

AWS_KEY_ID = os.getenv('AWS_KEY_ID')
AWS_SECRET_KEY=os.getenv('AWS_SECRET_KEY')
bucket=os.getenv('bucket')

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_KEY
)

data = 'data/2026-05-05_10-33-25.json'
filename = '2026-05-05_10-33-25.json'

s3_client.upload_file(data,bucket,filename)
