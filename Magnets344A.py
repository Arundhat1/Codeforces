#344A
def Magnets():
    n = int(input())
    bars = []
    for _ in range(n):
        bars_a = input()
        bars.append(bars_a)
    groups = 1
    group = 0
    while group < n - 1:
        if bars[group] != bars[group + 1]:
            groups += 1
        group +=1
    return groups
