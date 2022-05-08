'''
9. Pattern: 

      a 
    1 2 
  a b c 
1 2 3 4 
'''

row=int(input('Enter Rows: '))


for i in range(row):
    num=97
    x=1
    for space in range(row-(i+1)):
        print(' ',end=' ')

    for j in range(i+1):

        if(i%2==0):
            print(chr(num),end=' ')
            num+=1

        else:
            print(x,end=' ')
            x+=1

    print()
