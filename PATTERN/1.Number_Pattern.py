#1. Pattern :

# 1 4 7 10 
# 2 5 8 11 
# 3 6 9 12 
# 4 7 10 13

row=int(input('Enter No of Rows: '))
colm=int(input('Enter No of Colm: '))

num=1

for i in range(row):
    num=1+i
    for j in range(colm):
        print(num,end=' ')
        num+=3

    print()

#Enter No of Rows: 4
#Enter No of Colm: 4
#1 4 7 10 
#2 5 8 11 
#3 6 9 12 
#4 7 10 13
