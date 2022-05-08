'''
4. Pattern: 

d c b a 
c b a 
b a 
a 
'''

row=int(input('Enter Rows: '))

for i in range(row):
    num=100-i
    for j in range(row-i):

        print(chr(num),end=' ')
        num-=1

    print()
