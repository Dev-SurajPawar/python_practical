'''
Enter no of row: 4
A 
2 1 
C B A 
4 3 2 1 

'''

row=int(input('Enter no of row: '))

for i in range(row):
    if(i%2==0):
        num=i+65
        for j in range(i+1):
            print(chr(num),end=' ')
            num-=1
        print()

    else:
        num=i+1 
        for j in range(i+1):
            print(num,end=' ')
            num-=1
        print()
