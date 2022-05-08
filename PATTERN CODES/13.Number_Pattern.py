'''
Enter no of row: 4
1 
2 3 
3 4 5 
4 5 6 7 

'''
row=int(input('Enter no of row: '))

for i in range(row):
    num = i+1
    for j in range(i+1):
        print(num,end=' ')
        num+=1
    print()
