'''
Enter a no of rows: 4
Enter a no of colm: 4
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16 
Total Sum :  34

'''

row = int(input('Enter a no of rows: '))
colm = int(input('Enter a no of colm: '))

num = 1
sum = 0
for i in range(row):
    for j in range(colm):
        print(num, end=' ')
        
        if (i == j):
            sum = sum + num
        
        num+=1
    print()
print('Total Sum : ',sum)



