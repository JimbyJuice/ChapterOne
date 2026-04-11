import requests

def viewAnimeList(userName):
    query = '''
    query ($type: MediaType!, $userName: String!) {
        MediaListCollection(type: $type, userName: $userName) {
            lists {
                name
                entries {
                    id
                    score
                    media {
                        id
                        title {
                            english
                            romaji
                        }
                        averageScore
                    }
                }
            }
        }
    }
    '''

    # define our query variables and values used in query request
    variables = {
        'type': 'ANIME',
        'userName': userName
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP API request
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()
    listNames = []
    for choiceList in data['data']['MediaListCollection']['lists']:
        listNames.append(choiceList['name'])
    listNames.append('ALL')
    listNames.append('EXIT')
    
    while True: 
        print("\nSelect list to view (type ALL for all lists)")
        index = 0
        for listName in listNames:
            print(f"    [{index}] {listName}")
            index += 1
    
        chosenList = listNames[int(input("> "))]
        if chosenList not in listNames:
            print("Please select a valid list")
            continue
            
        if chosenList == 'EXIT':
            break
    
        if response.status_code == 200:
            for list in data['data']['MediaListCollection']['lists']:
                if (list['name'] != chosenList and chosenList != 'ALL'): continue
                print(f"\n====== {list['name']} ======")
                
                for entry in list['entries']:
                    title = entry['media']['title']['english']
                    score = entry['score']
                    averageScore = entry['media']['averageScore']
                    if title is None:
                        title = entry['media']['title']['romaji']
                    print(f"\n* {title}")
                    print(f"    - My Score: {score * 10}")
                    print(f"    - Global Score: {averageScore}")
                
        else:
            print(f"Error: {response.status_code}")