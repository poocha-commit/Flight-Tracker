import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
SHEETY_PRICE_ENDPOINT="https://api.sheety.co/72328dfa80ffb8b0ca222168d5328989/flightDeals/prices"


class DataManager:
    def __init__(self):
        self._user=os.environ.get("SHEETY_USERNAME")
        self._password=os.environ.get("SHEETY_PASSWORD")
        self._authorization= HTTPBasicAuth(self._user,self._password)
        self.destination_data={}
        self.params={}
        

    def get_data(self):
        response=requests.get(url=SHEETY_PRICE_ENDPOINT)
        data=response.json()
        self.destination_data=data['prices']
        return data
    def update_data(self):

        for i in self.destination_data:
            params={
                
                "iataCode":i["iataCode"]}
            
            url=f"{SHEETY_PRICE_ENDPOINT}/{i["id"]}"
            response=requests.put(url=url,json=params)
            # print(response.text)

