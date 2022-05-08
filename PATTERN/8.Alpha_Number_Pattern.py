'''
8. Pattern: 

      a 
    2 1 
  c b a 
4 3 2 1
'''

row=int(input('Enter Rows: '))


for i in range(row):

    num=97+i
    x=1+i
    for space in range(row-(i+1)):
        print(' ',end=' ')

    for j in range(i+1):

        if(i%2==0):
            print(chr(num),end=' ')
            num-=1

        else:
            print(x,end=' ')
            x-=1

    print()
