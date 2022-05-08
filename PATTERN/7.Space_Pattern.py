'''
7. Pattern:

         9 
      18 27 
   36 45 54 
63 72 81 90 
'''
row=int(input('Enter Rows: '))

num = 9
for i in range(row):

    for space in range(row-(i+1)):
        print(' ',end='  ')

    for j in range(i+1):
        print(num,end=' ')
        num=num+9

    print()

