'''
Enter a no of rows: 3
Enter a no of colm: 3
17 15 13 
11 9 7 
5 3 1 

'''

row = int(input('Enter a no of rows: '))
colm = int(input('Enter a no of colm: '))

num = 17
for i in range(row):
    for j in range(colm):
        print(num, end=' ')
        num-=2
    print()



