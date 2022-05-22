#Write a program to find duplicates from the array

import array

arr= []
num = int(input('Enter No of Elements in Array: '))

for i in range(num):
    
    ele=int(input())

    arr.append(ele)

print(arr)

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):

        if(arr[i]==arr[j]):
            print(arr[j])

#Input : [1,1,3,4,5,6,6]
#Output : 1 6

