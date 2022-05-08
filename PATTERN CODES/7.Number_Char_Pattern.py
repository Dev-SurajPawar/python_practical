'''
Enter a no of rows: 4
Enter a no of colm: 4
A B C D 
5 6 7 8 
I J K L 
13 14 15 16 

'''

row = int(input('Enter a no of rows: '))
colm = int(input('Enter a no of colm: '))

num = 65

for i in range(row):
    for j in range(colm):
 
        if (i%2==0):
            print(chr(num), end=' ')
            num += 1
        
        else:
            print(num-64,end=' ')
            num+=1
    
    print()



