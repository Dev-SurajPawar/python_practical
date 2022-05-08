'''
Enter row: 4
1 
2 1 
3 2 1 
4 3 2 1

'''

row=int(input('Enter row: '))

for i in range(row):
    num=1+i
    for j in range(i+1):
        print(num,end=' ')
        num-=1

    print()
