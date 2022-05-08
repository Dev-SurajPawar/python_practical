#3. WAP to take numerical input from the user and find whether the number is divisible by 5 and 11.

num=int(input('Enter Number: '))

if(num%5==0 and num%11==0):
    print(num,'Divisible by 5 and 11')
else:
    print(num,'Not Divisible by 5 and 11')
    
#input: 55
#output: 55 Divisible by 5 and 11
