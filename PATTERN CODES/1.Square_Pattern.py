'''
Enter a no of rows: 4
Enter a no of colm: 4
1 4 9 16 
25 36 49 64 
81 100 121 144 
169 196 225 256 

'''

row = int(input('Enter a no of rows: '))
colm = int(input('Enter a no of colm: '))

num = 1
for i in range(row):
    for j in range(colm):
        print(num*num, end=' ')
        num+=1
    print()



