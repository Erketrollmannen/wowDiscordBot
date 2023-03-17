# Import requests library
import requests
import json
import os
from dotenv import load_dotenv
from dataHandler import cleanup

# Load environment variables
#from oxBot import username, server

load_dotenv()  # take environment variables from .env.

def getData(username, server):

    # Define client id and client secret
    client_id = os.getenv("bnetClientID")
    client_secret = os.getenv("bnetClientSecret")

    # Get access token from Blizzard API
    url = "https://us.battle.net/oauth/token"
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, data=data, auth=(client_id, client_secret))
    access_token = response.json()["access_token"]

    # Define character profile summary endpoint
    #username = input("Enter your username: ")
    #server = input("Enter your server: ")
    endpoint = f"https://eu.api.blizzard.com/profile/wow/character/{server}/{username}/achievements/statistics?namespace=profile-eu&locale=en_GB"
                 #https://eu.api.blizzard.com/profile/wow/character/stormscale/nightsadow/pvp-bracket/shuffle-warrior-arms?namespace=profile-eu&locale=en_GB"
    # Define headers with access token and other parameters
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Battlenet-Namespace": "profile-eu",
        "Locale": "en_GB"
    }

    # Make a GET request to the endpoint with headers
    response = requests.get(endpoint, headers=headers)

    # Get character data as JSON object
    character_data = response.json()

    # Print character data
    with open("data.json", "w") as f:
        f.write(json.dumps(character_data, indent=4))
    #print(character_data)
    cleanData = cleanup()
    return cleanData
    #print(json.dumps(character_data, indent=4))