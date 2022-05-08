'''
Enter row: 4
      1 
    1 2 
  1 2 3 
1 2 3 4

'''

row=int(input('Enter row: '))

for i in range(row):

    num = 1
    for j in range(row-(i+1)):
        print(' ',end=' ')

    for k in range(i+1):
        print(num,end=' ')
        num+=1

    print()


