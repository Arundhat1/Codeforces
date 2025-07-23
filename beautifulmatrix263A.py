#263A
def beautifulmatrix():
    for row in range(5):
        rows = list(map(int,input().split))
        if rows != [0,0,0,0,0]:
            row_exchange = abs(row - 5)
        for columns in range(5):
            if rows[columns] != 0 :
                column_exchange = abs(5- columns)
    return row_exchange + column_exchange
