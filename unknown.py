def unkown():
   t = int(input())
   ans = []
   for _ in range(t):
        (n,x,k) = map(int, input().split())
        s = input()
        count = 0
        i = 0
        while i < n :
            if s[i] == 'R':
               x = x + 1
               k = k - 1
               if k < 0:
                    break
            else:
               x = x -1
               k = k - 1
               if k < 0:
                    break
            if i == (n- 1) and x != 0:
                 break
            if x == 0  and  k >= 0:
                i = 0
                count = count + 1
            elif k > 0:
                i = i + 1
        ans.append(count)
   for _ in ans:
        print(_)
