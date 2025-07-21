#490A
def Olympiad_team():
    n = int(input())
    t = list(map(int,input().split()))
    one = []
    two = []
    three = []
    w ,p,c,m = 0,0,0,0
    for i in range(n):
        if t[i] == 1:
            one.append(i+1)
            c = c +1
        elif t[i] == 2:
            two.append(i+1)
            m = m + 1
        elif t[i] == 3:
            three.append(i+1)
            p = p + 1
    w = min(p,c,m)
    if w != 0 :
        print(w)
        for _ in range(w):
            print(one[_],two[_],three[_])
    else:
        print(0)
