#116A
def Tram():
    n = int(input())
    a = []
    b = []
    capacity = []

    for _ in range(n):
        a_on, b_off = map(int, input().strip().split())
        a.append(a_on)
        b.append(b_off)
    a_total = 0
    b_total = 0
    capacity = []
    for stop in range(n):
        a_total += a[stop]
        b_total += b[stop]
        capacity.append(b_total - a_total)
        
      
    return max(capacity)
