#546A
def budget():
    k,n,w = map(int , input().split())
    total = (w*(w+1)*k)//2
    return (total - n)
