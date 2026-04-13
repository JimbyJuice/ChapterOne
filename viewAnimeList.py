def viewAnimeList(animeCache):
    listNames = []
    for choiceList in animeCache['data']['MediaListCollection']['lists']:
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
    
        for list in animeCache['data']['MediaListCollection']['lists']:
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
            