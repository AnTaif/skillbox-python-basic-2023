rows = 6
columns = 6

for row in range(rows):
    for column in range(columns):
        n = row + column * 2
        print(n, end='\t')
    
    print('')
