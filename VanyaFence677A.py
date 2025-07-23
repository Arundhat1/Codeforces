#677A
def VanyaFence():
    (n , h) =map(int , input().split())
    note = input().split()
    
    width = 0 
    for fri in note:
        if int(fri) > h :
            width = width + 2
        else:
            width += 1
    return width
