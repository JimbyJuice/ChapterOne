import requests
from mergeSort import mergeSort

userName = input("Enter your AniList username: ")
contentType = input("Enter ANIME or MANGA: ")
listType = input("Enter list to be sorted (Watching, Paused...) ")

query = '''
query ($type: MediaType!, $userName: String!) {
    MediaListCollection(type: $type, userName: $userName) {
        lists {
            name
            entries {
                id
                media {
                    id
                    title {
                        english
                    }
                }
            }
        }
    }
}
'''

# define our query variables and values used in query request
variables = {
    'type': contentType,
    'userName': userName
}

url = 'https://graphql.anilist.co'

# Make the HTTP API request
response = requests.post(url, json={'query': query, 'variables': variables})
 
if response.status_code == 200:
    rankedList = []
    data = response.json()
    for list in data['data']['MediaListCollection']['lists']:
        print(f"\n=== {list['name']} ===")
        
        for entry in list['entries']:
            title = entry['media']['title']['english']
            rankedList.append(title)
            print(f"- {title}")
        
        mergeSort(rankedList)
        print(rankedList)
        
else:
    print(f"Error: {response.status_code}")