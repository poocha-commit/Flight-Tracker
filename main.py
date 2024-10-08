#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
SHEETY_ENDPOINT="https://api.sheety.co/72328dfa80ffb8b0ca222168d5328989/flightDeals/prices"

from data_manager import DataManager

import requests
dataManager=DataManager()
sheet_data=dataManager.get_data()['prices']

print(sheet_data)



# load_dotenv()
# # print(response.json())
# from pprint import pprint
# print()



for i in sheet_data:
    
    if i["iataCode"]=="":

        from flight_search import FlightSearch
        flight_search=FlightSearch()
        i["iataCode"]=flight_search.get_destination_code(i["city"])

print(f"sheet data:{sheet_data}")

dataManager.destination_data=sheet_data
dataManager.update_data()



    
# dataManager=DataManager()
# dataManager.addIata(sheet_data)
