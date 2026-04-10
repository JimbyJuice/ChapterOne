import requests
from mergeSort import mergeSort

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
    'type': 'MANGA',
    'userName': 'AquaticSalmon'
}

url = 'https://graphql.anilist.co'

# Make the HTTP API request
response = requests.post(url, json={'query': query, 'variables': variables})

# if response.status_code == 200:
#     myAnimeList = []
#     data = response.json()
#     for list in data['data']['MediaListCollection']['lists']:
#         if list['name'] != 'Paused': continue
#         print(f"\n=== {list['name']} ===")
        
#         for entry in list['entries']:
#             title = entry['media']['title']['english']
#             myAnimeList.append(title)
#             print(f"- {title}")
        
#         mergeSort(myAnimeList)
#         print(myAnimeList)
        
#     # print(response.json())
# else:
#     print(f"Error: {response.status_code}")
    
    

if response.status_code == 200:
    myAnimeList = []
    data = response.json()
    for list in data['data']['MediaListCollection']['lists']:
        print(f"\n=== {list['name']} ===")
        
        for entry in list['entries']:
            title = entry['media']['title']['english']
            myAnimeList.append(title)
            print(f"- {title}")
        
        mergeSort(myAnimeList)
        print(myAnimeList)
        
else:
    print(f"Error: {response.status_code}")