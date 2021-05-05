# Program that writes data from an API to a CSV file.

import requests
import csv

url = "https://api.spacexdata.com/v3/launches"

class SpacexHttpError(Exception):
    pass

def fetch_spacex_data(url):
    try:
        response = requests.get(url)  # Data download.
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise SpacexHttpError('Fail to fetch spacex data')
    return response.json()

data = fetch_spacex_data(url)

with open("flights.csv", mode='w') as flights_file:
    csv_w = csv.writer(flights_file)

    csv_w.writerow([         #Save strings in a CSV file.
    "flight_number:", 
    "mission_name:",
    "rocket_id:",
    "rocket_number:", 
    "launch_date_utc:", 
    "video_link: "
    ])

    for informations in data:  #Loop that saves data in a CSV file.
    
        csv_w.writerow([
            informations["flight_number"],
            informations["mission_name"], 
            informations["rocket"]["rocket_id"],
            informations["rocket"]['rocket_name'],
            informations["launch_date_utc"],
            informations["links"]["video_link"]
            ])