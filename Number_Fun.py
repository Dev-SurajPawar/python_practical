

def Number_Multi_Operations(num):

    def Prime(num,i):
        if i==1:
            return 1
        if num%i==0:
            return 0
        return Prime(num,i-1)

    def Palindrome(num,rev):
        if num==0:
            return rev
        rev=rev*10+num%10
        return Palindrome(num//10,rev)

    def Armstrong(num):

        arm=0
        tmp=num
        count=0
        var=num

        if num>0:
            count=len(str(num))
            while tmp>0:
                sep=tmp%10
                arm=sep**count+arm
                tmp//=10
                Armstrong(tmp)
            if var==arm:
                print("Armstrong Number: ",var)
            else:
                print("Not Armstrong Number: ",var)


    def Reverse(num,tmp):
        if num==0:
            return tmp
        
        return Reverse(num//10,tmp*10+num%10)

    return Prime,Palindrome,Armstrong,Reverse

num=int(input('Enter Number: '))
x=Number_Multi_Operations(num)

print("""What You What To Check:
        1. Prime Number
        2. Palindrome Number
        3. Armstrong Number
        4. Reverse Number """)
Dprint=int(input("Enter Your choice(1-4): "))

if Dprint==1:
    p=x[0](num,num//2)
    if p==1:
        print("Prime Number: ",num)
    else:
        print("Not Prime Number: ",num)
elif Dprint==2:
    rev=x[1](num,0)
    if num==rev:
        print("Palindrome Number: ",num)
    else:
        print("Not Palindrome Number: ",num)
elif Dprint==3:
    print(x[2](num))
elif Dprint==4:
    rev=x[3](num,0)
    print("Reverse Number: ",rev)
else:
    print("Enter valid choice")

Do=input("Do You Want To check again Y or N: ")
if Do=='y' or do=='Y':

    print("""What You What To Check:
        1. Prime Number
        2. Palindrome Number
        3. Armstrong Number
        4. Reverse Number """)
    Dprint=int(input("Enter Your choice(1-4): "))

    if Dprint==1:
        p=x[0](num,num//2)
        if p==1:
            print("Prime Number: ",num)
        else:
            print("Not Prime Number: ",num)
    elif Dprint==2:
        rev=x[1](num,0)
        if num==rev:
            print("Palindrome Number: ",num)
        else:
            print("Not Palindrome Number: ",num)
    elif Dprint==3:
        print(x[2](num))
    elif Dprint==4:
        rev=x[3](num,0)
        print("Reverse Number: ",rev)
    else:
        print("Enter valid choice")
else:
    print("Thank You")

