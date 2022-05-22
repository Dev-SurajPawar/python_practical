#Write a program to reverse a array

import array

arr= []
num = int(input('Enter No of Elements in Array: '))

for i in range(num):
    
    ele=int(input())

    arr.append(ele)

print(arr)

arr.reverse()

print(arr)

#input : [1,2,3,4,5]
#Output : [5,4,3,2,1]
