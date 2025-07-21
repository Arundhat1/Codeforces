def TwoIntegers():
    t = int(input())
    k = [1,2,3,4,5,6,7,8,9,10]
    answ = []
    for _ in range(t):
        (a,b) = map(int,input().split())
        steps = 0
        diff = abs(b - a)
        if diff % 10 == 0:
            steps = diff /10
        else:
            steps = (diff // 10) + 1
        answ.append(int(steps))
    for ans in answ:
        print(ans)
