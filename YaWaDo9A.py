#9A
def YaWaDo():
    (y,w) = map(int,input().split())
    max = 0
    if y > w :
        max = y
    else:
        max = w
    print((6 - max +1)/6)
