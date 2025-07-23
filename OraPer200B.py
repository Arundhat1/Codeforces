#200B
def OraPer():
    n = int(input())
    pi = list(map(int , input().strip().split()))
    total = 0 
    for per in range(n):
        total += pi[per]
    return total / n
