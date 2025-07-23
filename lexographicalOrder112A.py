#112A
def lexographicalOrder():
    m = input().lower()
    n = input().lower()
    i = 0
    status = '0'
    while status == '0' and i < len(m):
        if m[i]== n[i]:
            status = '0'
        elif m[i] < n[i]:
            status = '-1'
        elif m[i] > n[i]:
            status = '1'
        i = i + 1
    return status
