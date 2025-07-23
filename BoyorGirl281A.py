#281A
def Boy_or_Girl():
    name = input()
    value = len(set(name))
    if value % 2 == 0:
        print("CHAT WITH HER!")
    else :
        print("IGNORE HIM!")
