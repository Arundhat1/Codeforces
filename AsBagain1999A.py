#1999A
def AsBagain():
    t = int(input())
    answ = []
    for _ in range(t):
        n = (input())
        suma = 0
        for chara in n:
            suma = suma + int(chara)
        answ.append(suma)
    for _ in range(t):
        print(answ[_]) 
