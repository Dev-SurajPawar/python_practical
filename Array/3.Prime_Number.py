#Write a program to find prime number from the given array

import array

arr=array.array('i',[])
num = int(input('Enter No of Elements in Array: '))

for i in range(num):
    
    ele=int(input())

    arr.append(ele)

print(arr)

for ele in arr:

        flag=0    
        for i in range(1,ele//2+1):
                if ele%i==0:
                    flag+=1
        if flag==1:
            print(ele)

#input : [1,3,2,7,9,10,12]
#Output : 2 3 7
