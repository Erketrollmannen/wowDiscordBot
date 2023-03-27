import json


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
        print (f"This is from dataHandler: {highest3v3} {highest2v2}")
        return highest3v3, highest2v2
        
        #return highest3v3, highest2v2
    except KeyError:
        print("Error")
        return "Error: either 0 exp, or something went wrong"

def nameFormat(playerserver):
    # make all variables lower case
    server = None
    playerserver = playerserver.lower()
    player = playerserver.split("-")[0]
    server = playerserver.split("-")[1]
    
    try:

        server = server.replace(" ", "-")
        server = server.replace("'", "")
    
    finally:
        print("player:",player,"server:",server)
        return player,server

if __name__ == '__main__':
    nameFormat(str(input("insert name and server name: ")))