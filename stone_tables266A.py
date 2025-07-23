#266A
def stones_tables():
    n = int(input())
    s = input()
    
    pick = 0
    for col in range(n-1):
        if s[col] == s[col+1]:
            pick += 1
    if pick == n - 1:
        return n - 1
    else:
        return pick
