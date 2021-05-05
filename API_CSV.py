# Program that writes data from an API to a CSV file.

import requests
import csv

url = "https://api.spacexdata.com/v3/launches"

response = requests.get(url)  # Data download.

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


    for informations in response.json():  #Loop that saves data in a CSV file.
    
        csv_w.writerow([
            informations["flight_number"],
            informations["mission_name"], 
            informations["rocket"]["rocket_id"],
            informations["rocket"]['rocket_name'],
            informations["launch_date_utc"],
            informations["links"]["video_link"]
            ])

     



