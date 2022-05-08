'''
Enter no of row: 4
* 
* * 
* * * 
* * * * 

'''

row=int(input('Enter no of row: '))

for i in range(row):
    for j in range(i+1):
        print('*',end=' ')

    print()
