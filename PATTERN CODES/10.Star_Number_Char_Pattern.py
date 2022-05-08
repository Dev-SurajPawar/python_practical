'''
Enter a no of rows: 4
Enter a no of colm: 4
* * * * 
A B C D 
5 6 7 8 
* * * * 

'''

row = int(input('Enter a no of rows: '))
colm = int(input('Enter a no of colm: '))

num = 65

for i in range(row):
     
        if(i%3==0):
            for j in range(colm):
                print('*',end=' ')
            print()

        elif (i%2!=0):
            for j in range(colm):
                print(chr(num), end=' ')
                num += 1
            print()
        
        else:
            for j in range(colm):
                print(num-64,end=' ')
                num+=1
            print()
    
print()



