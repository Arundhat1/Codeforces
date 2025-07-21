#1367A
def AliceandBob():
    t = int(input())
    ans = []
    for _ in range(t):
        b = input()
        answ = b[0]
        for i in range(len(b)):
            if  i % 2 != 0:
                answ = answ + b[i]
        ans.append(answ)
    for _ in ans:
        print(_)
