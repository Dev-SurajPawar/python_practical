'''
Enter no of row: 4
A 
A B 
A B C 
A B C D 

'''

row=int(input('Enter no of row: '))

for i in range(row):
    num = 65
    for j in range(i+1):
        print(chr(num),end=' ')
        num+=1
    print()
