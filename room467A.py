#467A
def room():
    n = int(input())
    p = []
    q = []
    count = 0
    for _ in range(n):
        pa ,qa = map(int, input().strip().split())
        p.append(pa)
        q.append(qa)
    for room in range(n):
        if q[room]-p[room] > 1:
            count += 1
    return count
