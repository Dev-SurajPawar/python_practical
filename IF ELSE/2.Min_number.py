#2. Write program to find min among 3 numbers

num1=int(input('Enter Number: '))
num2=int(input())
num3=int(input())

if(num1<num2 and num1<num3):
    print(num1)
elif(num2<num1 and num2<num3):
    print(num2)
else:
    print(num3)
    
    #Input : 2 3 4
#Output : 2
