#1669A
def division():
    t = int(input())
    answ = []
    for _ in range(t):
        rating = int(input())
        if rating >= 1900:
            answ.append("Division 4")
        elif rating < 1900 and rating >= 1600:
            answ.append("Division 3")
        elif rating < 1600 and rating >= 1400:
            answ.append("Division 2")
        else:
            answ.append("Division 1")
    for ans in answ:
        print(ans)
