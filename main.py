# NOTE :
# Pour les notification : https://pushover.net/apps/agazvbkroksp5yck8e8idsdjgbmxve
# Pour le calcul d'itinéraire : https://maps.open-street.com/gui/

import os
import requests
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(dotenv_path=BASE_DIR / ".env")


def GetDistance(origin, destination):
    open_street_request = requests.get(
        "https://maps.open-street.com/api/route/",
        params={"origin": origin, "destination": destination, "mode": "driving",
                "key": os.getenv("OPENSTREET_KEY")})

    if open_street_request.json().get("total_distance") is None:
        print(f"Open Street Error with origin : {origin} and destination {destination} : {open_street_request.json()}")

    return open_street_request.json().get("total_distance")


vitemadose_request = requests.get("https://vitemadose.gitlab.io/vitemadose/77.json")

centre_disponibles = vitemadose_request.json().get("centres_disponibles", [])
rdv = []

for centre in centre_disponibles:
    url = centre.get("url")
    location = centre.get("location")
    guid = centre.get("gid")

    app_schedules = centre.get("appointment_schedules", [])
    for schedule in app_schedules:
        app_name = schedule.get('name', '')
        if app_name != "chronodose":
            continue

        total_doses = schedule.get('total')
        if total_doses > 0:
            latLong = f"{location['latitude']},{location['longitude']}"
            distance = GetDistance(os.getenv("HOME_LOCATION"), latLong)

            if distance is None:
                continue

            distance = (distance / 1000)
            if distance < int(os.getenv("DISTANCE")):
                rdv.append((guid, f"{total_doses} doses - distance : {distance} km - {url}\n"))

message = ''

for dose in rdv:
    message = message + dose[1]

if len(rdv) > 0:
    message = "Rendez-vous disponible : \n" + message
    print(message)

    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={"token": os.getenv("PUSHOVER_TOKEN"), "user": os.getenv("PUSHOVER_USER"), "message": message})
else:
    print("Pas de rendez-vous disponible sous les 30km")
