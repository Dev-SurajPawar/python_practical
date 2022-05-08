'''
Enter row: 4
A 
B B 
C C C 
D D D D 

'''

row=int(input('Enter row: '))

num=65
for i in range(row):
    for j in range(i+1):
        print(chr(num),end=' ')

    print()
    num+=1
