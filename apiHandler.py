# Import requests library
import requests
import json
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()  # take environment variables from .env.

#Extracts API-endpoints for the various pvp-brackets
# the player has participated in.
def soloShufflelinks():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)#this converts to a python dictionary
            soloShuffleparticipations = []
        for bracket in data["brackets"]:
            if "shuffle" in bracket["href"]:
                soloShuffleparticipations.append(bracket["href"])
                #print(soloShuffleparticipations)
        return soloShuffleparticipations
    except KeyError:
        print("Error")
        return "Error: either 0 exp, or something went wrong"


#Extracts rating and specialization in solo shuffle,
# from the data returned from the API.
def soloShuffleSpecRating():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)#this converts to a python dictionary

        rating = data["rating"]
        specialization = data["specialization"]["name"]["en_GB"]
        #print(type(rating))
        #print(type(specialization))
        return specialization, rating

    except KeyError:
        print("Error")
        return "Error: either 0 exp, or something went wrong"


def highestArenaExp():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)

        for i in data["categories"]:
            if i["id"] == 21:
                sub_cat = i["sub_categories"]
                break
        for i in sub_cat[0]["statistics"]:
            if i["id"] == 595:
                h3v3 = i["quantity"]
            if i["id"] == 370:
                h2v2 = i["quantity"]
        #print(data)
        

        #h3v3 = data["categories"][8]["sub_categories"][0]["statistics"][30]["quantity"]
        #h2v2 = data["categories"][8]["sub_categories"][0]["statistics"][31]["quantity"]
        highest3v3 = f"Highest 3v3 exp: {h3v3}"
        highest2v2 = f"Highest 2v2 exp: {h2v2}"
        #print (f"This is from dataHandler: {highest3v3} {highest2v2}")
        return highest3v3, highest2v2
        
        #return highest3v3, highest2v2
    except KeyError:
        print("Error")
        return "Error: either 0 exp, or something went wrong"


def getData(endpoint):
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
    #endpoint = f"https://eu.api.blizzard.com/profile/wow/character/stormscale/mompets/pvp-summary?namespace=profile-eu"
    #this is the link to the summary.
    #here i can get all active brackets for the specific character.
                 #link to get summary information
                 #/profile/wow/character/{realm-slug}/{character-name}/pvp-summary
                
                #https://eu.api.blizzard.com/profile/wow/character/{server}/{username}/achievements/statistics?namespace=profile-eu&locale=en_GB
                #https://eu.api.blizzard.com/profile/wow/character/stormscale/nightsadow/pvp-bracket/shuffle-{class}-{spec}?namespace=profile-eu&locale=en_GB"

    # Define headers with access token and other parameters
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Battlenet-Namespace": "profile-eu",
        "Locale": "en_GB"
    }

    # Make a GET request to the endpoint with headers
    response = requests.get(endpoint, headers=headers)
    #print(response.text)
    # Get character data as JSON object
    character_data = response.json()

    # Print character data
    with open("data.json", "w") as f:
        f.write(json.dumps(character_data, indent=4))
    #print(character_data)

    #print(json.dumps(character_data, indent=4))


def lookup(username, server):

    pvpsummaryEndpoint = f"https://eu.api.blizzard.com/profile/wow/character/{server}/{username}/pvp-summary?namespace=profile-eu"
    pvp2v2and3v3Endpoint = f"https://eu.api.blizzard.com/profile/wow/character/{server}/{username}/achievements/statistics?namespace=profile-eu&locale=en_GB"
    getData(pvpsummaryEndpoint)
    soloShufflebrackets = soloShufflelinks()

    soloRatings = []
    try:
        for brackets in soloShufflebrackets:
            getData(brackets)
            soloRatings.append(soloShuffleSpecRating())
            #print(type(soloRatings))
        
        getData(pvp2v2and3v3Endpoint)
        arenaRatings = highestArenaExp()
    except KeyError:
        print("Error")
        return "Error: either 0 exp, or something went wrong"

    #print(soloRatings)
    #print(arenaRatings)
    return(soloRatings, arenaRatings)


def my_decorator(func):
    def wrapper():
        print("-----------------------------")
        func()
        print("-----------------------------")
    return wrapper


if __name__ == "__main__":
    lookup("mompets","stormscale")
    #lookup(str(input("insert username:")),str(input("insert server:")))
    #highestSoloExp()
    #getData("https://eu.api.blizzard.com/profile/wow/character/stormscale/nightsadow/pvp-bracket/shuffle-warrior-arms?namespace=profile-eu&locale=en_GB")
    #soloShuffleRatings()
    print("--------------------------------")
    print("Main function run")
    print("--------------------------------")