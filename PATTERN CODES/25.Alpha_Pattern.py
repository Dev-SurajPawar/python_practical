'''
Enter row: 4
A A A A 
B B B 
C C 
D 

'''

row=int(input('Enter row: '))

num=65
for i in range(row):
    for j in range(row-i):
        print(chr(num),end=' ')

    print()
    num+=1
