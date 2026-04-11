import requests
import json

print("====== Welcome to ChapterOne ======")

while (1):
    print(f"\nEnter an option to continue:")
    print(f"    [1] View my Anime List")
    print(f"    [2] View my Manga List")
    print(f"    [3] Rank my List")
    print(f"    [4] Quit")
    choice = int(input("> "))
    
    match choice:
        case '1':
            print()
        case '2':
            def
        case '3':
            def
        case '4':
            break
        case _:
            print("Please select a valid option")

print("Thank you for using ChapterOne!")

# query = '''
# query ($type: MediaType!, $userName: String!) {
#     MediaListCollection(type: $type, userName: $userName) {
#         lists {
#             name
#             entries {
#                 id
#                 score
#                 media {
#                     id
#                     countryOfOrigin
#                     type
#                     source
#                     title {
#                         english
#                         romaji
#                     }
#                     popularity
#                     averageScore
#                 }
#             }
#         }
#     }
# }
# '''


# userName = input("Enter your AniList username: ")
# contentType = input("Enter ANIME or MANGA: ")
# listType = input("Enter list to be sorted (Watching, Paused...) ")