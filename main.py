import requests


def card_search(endpoint, endpoint2):
    url = "https://omgvamp-hearthstone-v1.p.mashape.com/cards/{}/{}".format(endpoint,endpoint2)
    response = requests.get(url,
      headers={
        "X-Mashape-Key": "bGq2SWXpg1mshSXiqfwvJlEfBt1sp13QHjMjsnV1yYDx2h1beo",
        "Accept": "application/json"
      }
    )

    json_result = response.json()
    categories = ["name","cardSet", 'cost', 'attack', 'health', 'rarity','text']
    for item in json_result:
        for category in categories:
            try:
                print ("{} : {}".format(category, item[category]))
            except KeyError:
                print("{} : n/a".format(category))
        print ("___________")

    #url = json_result["next"]



def card_info():
    url = "https://omgvamp-hearthstone-v1.p.mashape.com/info/"
    response = requests.get(url,
      headers={
        "X-Mashape-Key": "bGq2SWXpg1mshSXiqfwvJlEfBt1sp13QHjMjsnV1yYDx2h1beo",
        "Accept": "application/json"
      }
    )

    json_result = response.json()
    for key, value in json_result.items():
        print(key, value)


while True:
    print ("""
    To search for a specfic card, enter(search), then the card name. To veiw all
    cards for a class, set, or race, enter(classes/sets/races), then the name.
    """
    )
    value1 = input("search parameter: ")
    if value1 != 'info':
        value2 = input("Name: ")
        card_search(value1,value2)
    else:
        card_info()
