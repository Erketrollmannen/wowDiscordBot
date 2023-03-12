import json


with open('data.json', 'r') as f:
    data = json.load(f)

#print(data)

highest3v3 = data["categories"][8]["sub_categories"][0]["statistics"][30]["quantity"]
highest2v2 = data["categories"][8]["sub_categories"][0]["statistics"][31]["quantity"]

print(highest3v3, highest2v2)
#return highest3v3, highest2v2
