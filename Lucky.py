#1676A
def Lucky():
    t = int(input())
    answ = []
    for _ in range(t):
        (a,b,c,d,e,f) = map(int,list(input()))
        if a + b + c == d + e + f:
            answ.append("YES")
        else:
            answ.append("NO")
    for ans in answ:
        print(ans)
