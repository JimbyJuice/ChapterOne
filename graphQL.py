import requests

query = '''
query ($search: String) {
    Media (search: $search, type: ANIME) {
        id
        title {
            romaji
            english
        }
        coverImage {
            large
        }
    }
}
'''

# define our query variables and values used in query request
variables = {
    'search': 'Solo Leveling'
}

url = 'https://graphql.anilist.co'

# Make the HTTP API request
response = requests.post(url, json={'query': query, 'variables': variables})

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")