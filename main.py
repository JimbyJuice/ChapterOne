from helper import fetchAnimeList, fetchMangaList
from viewAnimeList import viewAnimeList
from viewMangaList import viewMangaList
from rankUserList import rankUserList

print("====== Welcome to ChapterOne ======")
userName = input("Enter your AniList username: ")

animeCache = fetchAnimeList(userName)
mangaCache = fetchMangaList(userName)

while (1):
    print(f"\nEnter an option to continue:")
    print(f"    [1] View my Anime List")
    print(f"    [2] View my Manga List")
    print(f"    [3] Rank my List")
    print(f"    [4] Refresh Cache")
    print(f"    [5] Quit")
    choice = int(input("> "))

    match choice:
        case 1:
            viewAnimeList(animeCache)
        case 2:
            viewMangaList(mangaCache)
        case 3:
            rankUserList(animeCache, mangaCache)
        case 4:
            animeCache = fetchAnimeList(userName)
            mangaCache = fetchMangaList(userName)
        case 5:
            break
        case _:
            print("Please select a valid option")

print("Thank you for using ChapterOne!")