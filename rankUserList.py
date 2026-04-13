from helper import mergeSort

def rankUserList(animeCache, mangaCache):
    while True:
        contentType = input("Enter ANIME or MANGA: ").strip().upper()
        if contentType == 'ANIME':
            givenCache = animeCache
            break
        elif contentType == 'MANGA':
            givenCache = mangaCache
            break
        else:
            print("Invalid input. Please enter ANIME or MANGA.\n")

    listNames = []
    for choiceList in givenCache['data']['MediaListCollection']['lists']:
        listNames.append(choiceList['name'])
    listNames.append('ALL')
    listNames.append('EXIT')
    
    while True: 
        print("\nSelect list to rank (type ALL for all lists)")
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

        rankedList = []
        for list in givenCache['data']['MediaListCollection']['lists']:
            if (list['name'] != chosenList and chosenList != 'ALL'): continue
            print(f"\n=== {list['name']} ===")
            
            for entry in list['entries']:
                title = entry['media']['title']['english']
                if title is None:
                    title = entry['media']['title']['romaji']
                rankedList.append(title)
            
            mergeSort(rankedList)
            for i in range(0, len(rankedList)):
                print(f"    {i}. {rankedList[i]}")
                