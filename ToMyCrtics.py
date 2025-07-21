
def ToMyCritics():
    t = int(input())
    ans =[]
    for _ in range(t):
        (a,b,c) = map(int,input().split())
        if (a+b) > 10 or (b+c) > 10 or (a+c) > 10:
            ans.append("YES")
        else:
            ans.append("NO")
    for _ in range(t):
        print(ans[_])
