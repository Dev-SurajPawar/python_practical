'''
5. Pattern: 

5 4 3 2 1 
D C B A 
3 2 1 
B A 
1 
'''

row=int(input('Enter Rows: '))

for i in range(row):
    num=68-i+1
    x=row-i
    for j in range(row-i):

        if(i%2==0):
            print(x,end=' ')
            x-=1

        else:
            print(chr(num),end=' ')
            num-=1

    print()
