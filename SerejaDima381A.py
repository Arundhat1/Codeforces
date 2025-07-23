#381A
def SerejaDima():
    n = int(input())
    cards = list(map(int,input().split()))
    sereja = 0
    dima = 0
    while len(cards) > 0:
        Se = max(cards[0],cards[-1])
        
        sereja = sereja +Se
        cards.remove(Se)
        if len(cards) != 0:
            Di = max(cards[0],cards[-1])
            dima = dima + Di
            cards.remove(Di)
            
    print(sereja , " ",dima)
