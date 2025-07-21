def SpyDetected():
    t = int(input())
    ans = []
    for _ in range(t):
        n = int(input())
        nums = list(map(int,input().split()))
        a = min(nums)
        b = max(nums)
        if nums.count(a) > nums.count(b):
            ans.append(nums.index(b) + 1)
        else:
            ans.append(nums.index(a) + 1)
    for answ in ans:
        print(answ)
