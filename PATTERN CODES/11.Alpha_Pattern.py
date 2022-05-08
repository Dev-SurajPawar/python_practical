'''
Enter no of row: 4
a 
a a 
a a a 
a a a a 

'''

row=int(input('Enter no of row: '))

for i in range(row):
    for j in range(i+1):
        print('a',end=' ')

    print()
