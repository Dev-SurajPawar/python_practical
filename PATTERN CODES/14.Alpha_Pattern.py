'''
Enter no of row: 4
A 
B C 
C D E 
D E F G 

'''

row=int(input('Enter no of row: '))

for i in range(row):
    num = i+65
    for j in range(i+1):
        print(chr(num),end=' ')
        num+=1
    print()
