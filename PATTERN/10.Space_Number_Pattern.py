'''
10. Pattern: 

       1 
     2 4 
  3  6 9 
4 8 12 16 
'''
row=int(input('Enter Rows: '))

for i in range(row):
    num = 1+i
    for space in range(row-(i+1)):
        print(' ',end=' ')

    for j in range(i+1):
            print(num,end=' ')
            num=num+i+1

    print()

