#9. Write a Program that takes angles of a triangle from the user and print whether that triangle is valid or not. {Note: Addition of #angles of triangle has to be 180 in order to consider it as a valid one}

num1=int(input('Enter angle'))
num2=int(input())
num3=int(input())

if(num1+num2==num3):
    print('The Triangle with angle ',num1,num2,'and',num3,' is a valid one')

else:

    print('The Triangle with angle ',num1,num2,'and',num3,' is a invalid one')


S
