#1399A
def removesmall():
    t = int(input())
    ans = []
    for _ in range(t):
        n = int(input())
        numbs = list(map(int,input().split()))
 
        i = 0
        while i < n-1 and len(numbs) > 1 and j < (n-1) :
            num = numbs[i]
            j = i + 1
            if abs(num - numbs[j]) >= 1 :
                numbs.remove(min(num,numbs[j]))
                break
            else:
                    j = j + 1
                    
            i = i + 1
        print(numbs)      
        if len(numbs)  == 1:
            ans.append("YES")
        else:
            ans.append("NO")
    for answ in range(t):
        print(ans[answ])
