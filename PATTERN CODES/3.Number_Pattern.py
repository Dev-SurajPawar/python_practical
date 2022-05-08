'''
Enter a no of rows: 4
Enter a no of colm: 4
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 

'''

row = int(input('Enter a no of rows: '))
colm = int(input('Enter a no of colm: '))

for i in range(row):
    num = 1
    for j in range(colm):
        print(num, end=' ')
        num+=1
    print()



