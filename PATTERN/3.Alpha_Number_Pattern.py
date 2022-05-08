'''
3. Pattern: 

D4 C3 B2 A1 
D4 C3 B2 A1 
D4 C3 B2 A1 
D4 C3 B2 A1 

'''

row=int(input('Enter Rows: '))
colm=int(input('Enter Colm: '))


for i in range(row):
    num=68
    for j in range(colm):
        print(chr(num),end='')
        print(num-64,end=' ')
        num-=1

    print()
