'''
6. Pattern: 

A 
B 2 
C 3 C 
D 4 D 4 
E 5 E 5 E 
'''

row=int(input('Enter No of Rows: '))

for i in range(row):
    num=65+i
    x=1+i
    for j in range(i+1):
       
        if(j%2==0):
            print(chr(num),end=' ')
           
        else:
            print(x,end=' ')
            

    print()
