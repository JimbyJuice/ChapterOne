import requests

LEFT = 1
RIGHT = 2
GRADE = ['S', 'A', 'B', 'C', 'D' 'F']

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

def mergeSort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    
    left_arr = arr[:length//2]
    right_arr = arr[length//2:]

    mergeSort(left_arr)
    mergeSort(right_arr)
    
    # merge
    i = 0
    j = 0
    k = 0
    while i < len(left_arr) and j < len(right_arr):
        while True:
            try:
                print(f"\nWhich do you prefer?")
                print(f"    [1] {left_arr[i]}")
                print(f"    [2] {right_arr[j]}")
                
                choice = int(input("> "))
                
                if choice != LEFT and choice != RIGHT:
                    raise ValueError("Not a valid option")
            
            except ValueError:
                print("Please pick either 1 or 2")
                continue
            
            break
                
        if choice == LEFT:
            arr[k] = left_arr[i]
            i += 1
        elif choice == RIGHT:
            arr[k] = right_arr[j]
            j += 1
            
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
        
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    return arr

def fetchAnimeList(userName):
    # define our query variables and values used in query request
    variables = {
        'type': 'ANIME',
        'userName': userName
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP API request
    response = requests.post(url, json={'query': query, 'variables': variables})
    
    if response.status_code == 200:
        return response.json()
        
    else:
        print(f"Error: {response.status_code}")

def fetchMangaList(userName):
    # define our query variables and values used in query request
    variables = {
        'type': 'MANGA',
        'userName': userName
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP API request
    response = requests.post(url, json={'query': query, 'variables': variables})
    
    if response.status_code == 200:
        return response.json()
        
    else:
        print(f"Error: {response.status_code}")