#266B    
def bog_queue():
    (n,t) = map(int,input().strip().split())
    s = list(input())
    time = 0
    while time < t:
        line = 0
        while line < (n -1):
            if s[line] == "B" and s[line + 1] == "G":
                s[line] = "G"
                s[line + 1] = "B"
                line += 2
            else:
                line += 1 
        time += 1
    return "".join(s)
