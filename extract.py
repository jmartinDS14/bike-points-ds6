import requests
import json
import os
import time
from datetime import datetime

count = 0
number_of_tries = 3
url = 'https://api.tfl.gov.uk/BikePoint'
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

while count < number_of_tries:
    response = requests.get(url,timeout=10)
    response_code = response.status_code
    if response_code==200:
        response_json = response.json()

        #We need to check if the directory exists and make it if not
        dir = 'data'
        os.makedirs(dir, exist_ok=True)

        filepath = f'{dir}/{timestamp}.json'

        try:
            with open(filepath,'w') as file:
                json.dump(response_json, file)
            print(f'Download successful at {timestamp} 😊')
        except Exception as e:
            print(e)
        
        break

    elif response_code>499 or response_code<200:
        #retry
        print(response.reason)
        time.sleep(10)
        count+=1
    else:
        print(response.reason)
        break