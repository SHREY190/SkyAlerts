import requests
SHEETY_ENDPOINT = "https://api.sheety.co/fd23fbb715fd5c4a137d4b1ef9e47be5/flightDeals/prices"
class DataManager:
    def __init__(self):
        self.destination_data={}
    #This class is responsible for talking to the Google Sheet.
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_data(self):
        for city in self.destination_data:
            edit_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=edit_data)
            print(response.text)
            
