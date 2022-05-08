'''
Enter a row: 4
4 3 2 1 
3 2 1 
2 1 
1

'''

row=int(input('Enter a row: '))

for i in range(row):
    num=row-i
    for j in range(row-i):
        print(num,end=' ')
        num-=1
    print()
