'''
Enter row: 4
1 
2 2 
3 3 3 
4 4 4 4 

'''

row=int(input('Enter row: '))

num=1
for i in range(row):
    for j in range(i+1):
        print(num,end=' ')

    print()
    num+=1
