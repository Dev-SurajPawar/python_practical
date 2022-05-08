'''
Enter a row: 4
* * * * 
* * * 
* * 
* 

'''

row=int(input('Enter a row: '))

for i in range(row):
    for j in range(row-i):
        print('*',end=' ')
    print()
