'''
Enter row: 4
A B C D 
A B C 
A B 
A

'''

row=int(input('Enter row: '))

for i in range(row):
    num = 65
    for j in range(row-i):
        print(chr(num),end=' ')
        num+=1
    print()
