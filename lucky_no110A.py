#110A
def lucky_no():
    n = list(input())
    total = n.count('4') + n.count('7')
    if total == 4 or total == 7:
        return "YES"
    else:
        return "NO"
