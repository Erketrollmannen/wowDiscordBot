import json


def cleanup():
    with open('data.json', 'r') as f:
        data = json.load(f)

    #print(data)

    h3v3 = data["categories"][8]["sub_categories"][0]["statistics"][30]["quantity"]
    h2v2 = data["categories"][8]["sub_categories"][0]["statistics"][31]["quantity"]
    highest3v3 = f"Highest 3v3 exp: {h3v3}"
    highest2v2 = f"Highest 2v2 exp: {h2v2}"
    print (f"This is from dataHandler: {highest3v3} {highest2v2}")
    return highest3v3, highest2v2
    
    #return highest3v3, highest2v2
