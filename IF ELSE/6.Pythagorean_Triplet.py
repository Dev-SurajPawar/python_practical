#6. WAP to check whether the given input is a Pythagorean triplet or not
# Note: Pythagorean triplet means if given three numbers
# a b and c follows this pattern c*c = a*a + b*b

num1=int(input('Enter Number'))
num2=int(input())
num3=int(input())

if((num1*num1)+(num2*num2)==(num3*num3)):

    print('Its Pythagorean Triplet')

else:
    
    print('Not Pythagorean Triplet')

