#136A
def presents():
    n = int(input())
    a_list = list(map(int,input().split()))
    b_list = []
    dicti = {}
    for fri in a_list:
        dicti[fri] = a_list.index(fri) + 1
    for fri in a_list:
        b_list.append(dicti[dicti[fri]])
        
    
    return " ".join(list(map(str , b_list)))
