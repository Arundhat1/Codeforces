#1030A
def Findeasy():
    n = int(input())
    s = input()
    for opi in s:
        if opi == "1":
            return "HARD"
    return "EASY"
