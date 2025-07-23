#977A    
def WrongTanya():
    (n,k) = map(int,input().split( ))
    nu = 0
    while k > nu:
        if str(n)[-1] == '0':
            n = (n//10)
        else:
            n = n - 1
        nu = nu + 1
    return n
