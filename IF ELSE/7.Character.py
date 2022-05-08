#7. Program 3: Write a Program to Find whether the character is an alphabet, a digit or a special character

num=input('Enter : ')

if(num>='A' and num<='Z'):
    print(num,'Capital Alphabet')

elif(num>='a' and num<='z'):
    print(num,'Small Alphabet')

elif(num>='0' and num<='9'):
    print(num,'Number')

else:
    print(num,'Special Character')
