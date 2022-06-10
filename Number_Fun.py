

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
                arm=sep*count+arm
                tmp//=10
                Armstrong(tmp)
            if var==arm:
                print("Armstrong Number: ",var)
            else:
                print("Not Armstrong Number: ",var)


    def Reverse(num):
        
        if num<10:
            return num
        else:
            return int(str(num%10)+str(Reverse(num//10)))

    return Prime,Palindrome,Armstrong,Reverse

num=int(input('Enter Number: '))
x=Number_Multi_Operations(num)

print("""What You What To Check:
        1. Prime Number
        2. Palindrome Number
        3. Armstrong Number
        4. Reverse Number """)
Dprint=int(input("Enter Your choice: "))

if Dprint==1:
    p=x[0](num)
elif Dprint==2:
    rev=x[1](num,0)
    if num==rev:
        print("Palindrome Number: ",num)
    else:
        print("Not Palindrome Number: ",num)
elif Dprint==3:
    print(x[2](num))
else:
    rev=x[3](num)
    print("Reverse Number: ",rev)

