#734A
def AntonDanik():
    n = int(input())
    s = input()
    win ={"A": 0,"D":0}
    for game in s:
        if game == "A":
            win["A"] += 1
        elif game == "D":
            win["D"] += 1
   
    if win["A"] > win["D"]:
        return("Anton")
    elif win["A"] < win["D"]:
        return("Danik")
    elif win["A"] == win["D"]:
        return("Friendship")
