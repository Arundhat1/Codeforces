def trying():
    t = int(input())
    ans =  []
    for _ in range(t):
        n = int(input())
        numbs = list(map(int,input().split()))
        i_l = []
        j_l = []
        i = 0
        while i < (n-1) and j < n and len(numbs) > 0:
            j = i + 1
            if abs(numbs[i] - numbs[j]) <= 1:
                if i != j and  j not in i_l and i not in i_l :
                    i_l.append(i)
                    j_l.append(j)
            j = j + 1
            i = i + 1
    
        minim = []
        for ind in range(len(i_l)):
            minim.append(min(numbs[i_l[ind]],numbs[j_l[ind]]))
        for num in minim:
            numbs.remove(num)
        if len(numbs) == 1:
            ans.append("YES")
        else:
            ans.append("NO")
    for _ in ans:
        print(_)
        
