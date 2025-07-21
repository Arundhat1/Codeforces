#1560A
def Dislikeo3():
    t = int(input())
    ans = []
    for _ in range(t):
        k = int(input())
        count = 0
        num = 0
        while count < k:
            if num % 3 != 0 and num % 10 != 3:
                count += 1
            if count == k:
                ans.append(num)
                break
            num += 1        
    for _ in range(t):
        print(ans[_])
