#2009A
def Minimize():
    t = int(input())
    ans = []
    for _ in range(t):
        all_ans = []
        (a,b) = map(int,input().split())
        for num in list(range(a,b+1)):
            c = num
            out = (c-a) + (b-c)
            all_ans.append(out)
        ans.append(min(all_ans))
    for _ in ans:
        print(_)
