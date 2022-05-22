#Write a program to find even numbers from the array

import array

arr=array.array('i',[])
num = int(input('Enter No of Elements in Array: '))

for i in range(num):
    
    ele=int(input())

    arr.append(ele)

print(arr)

for ele in arr:

    if ele%2==0:
        print(ele)

#Input : [1,2,3,4,6,8,10]
#Output : 2 4 6 8 10
