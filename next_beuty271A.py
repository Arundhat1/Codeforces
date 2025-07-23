#271A
def next_beuty( ):
    y = int(input( ))
    yea = y + 1
    def beauty(year):
        a_list = list(str(year))
        for dig in a_list:
            if a_list.count(dig) > 1:
                return False
        return True
    while beauty(yea) == False :
        yea += 1
    return yea
