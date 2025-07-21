#1472B
def FairDiv():
    t = int(input())
    ans= []
    for _ in range(t):
        n = int(input())
        a_list = list(input().split())
        if a_list.count(1) % 2 == 0:
            ans.append("YES")
        else:
            ans.append("NO")
    for _ in range(t):
        print(ans[_])
