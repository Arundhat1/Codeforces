#
def Marathon():
    t = int(input())
    ans = []
    for _ in range(t):
        (a,b,c,d) = map(int,input().split())
        in_front = 0
        if b > a:
            in_front += 1
        if c > a:
            in_front += 1
        if d > a:
            in_front += 1
        ans.append(in_front)
    for _ in ans:
        print(_)
