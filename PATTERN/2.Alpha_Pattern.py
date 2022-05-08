'''
2.Pattern: 

A b C 
d E f 
G h I
'''

row=int(input('Enter Rows: '))
colm=int(input('Enter colm: '))

num=65

for i in range(row):
    for j in range(colm):

        if((i+j)%2==0):
            
            print(chr(num),end=' ')
            num+=1

        else:
            
            print(chr(num+32),end=' ')
            num+=1

    print()

'''
Enter Rows: 3
Enter colm: 3
A b C
d E f
G h I '''
