import logging
import requests
import os
import json
from datetime import datetime
import time

logger = logging.getLogger(__name__)

def extract(url,max_tries,dir):
    """
    This will call an api. If there's a server side issue it will retry for the specified number of times. 
    The data will be saved in the specified directory.

    Args:
        url (string): URL to call.
        max_tries (integer): Number of times to retry if there's a server side error.
        dir (string): Directory to save data to.
    """  
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')  
    response = requests.get(url)
    data = response.json()

    count = 0

    while count < max_tries:
        if 200 <= response.status_code < 300:
            
            os.makedirs(dir,exist_ok=True)
            filename = f"{dir}/{timestamp}.json"
            with open(filename, "w") as file:
                json.dump(data, file)
                    
            print(f"File {filename} was successfully created. Woohoo 🥳")
            logger.info(f"File {filename} was successfully created. Woohoo 🥳")
            return True
            break

        elif response.status_code >= 500:
            #retry after 10 seconds for these status codes
            time.sleep(10)
            count+=1
            print(f'Trying again. Attempt {count}')
            logger.info(f'Trying again. Attempt {count}')

        else:
            print(f"Error: {response.status_code} {data.get("message","no message found")}")
            logger.error(f"Error: {response.status_code} {data.get("message","no message found")}")
            break
    
    