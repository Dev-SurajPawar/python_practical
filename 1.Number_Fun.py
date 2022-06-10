
def Number_Multi_Operations(num):

    def Prime(num):
        count=0
        for i in range(2,num):
            if i%num==0:
                count+=1
        if count==0:
            print("Prime Number: ",num)
        else:
            print("Prime Number: ",num)

    def Palindrome(num):

        tmp=num
        rev=0
        while num>0:
            sep=num%10
            rev=rev*10+sep
            num//=10
        if tmp==rev:
            print("Palindrome Number: ",tmp)
        else:
            print("Not Palindrome Number: ",tmp)

    def Armstrong(num):

        arm=0
        tmp=num
        count=0
        var=num

        if num>0:
            count=len(str(num))
            while tmp>0:
                sep=tmp%10
                arm=sep*count+arm
                tmp//=10
            if var==arm:
                print("Armstrong Number: ",var)
            else:
                print("Not Armstrong Number: ",var)


    def Reverse(num):

        tmp=num
        rev=0
        while num>0:
            sep=num%10
            rev=rev*10+sep
            num//=10
        print("Reverse Number: ",rev)        

    return Prime,Palindrome,Armstrong,Reverse

num=int(input('Enter Number: '))
x=Number_Multi_Operations(num)

print("""What You Want To Check:
        1. Prime Number
        2. Palindrome Number
        3. Armstrong Number
        4. Reverse Number """)
Dprint=int(input("Enter Your choice: "))

if Dprint==1:
    print(x[0](num))
elif Dprint==2:
    print(x[1](num))
elif Dprint==3:
    print(x[2](num))
else:
    print(x[3](num))

