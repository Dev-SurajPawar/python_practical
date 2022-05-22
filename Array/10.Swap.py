#Write a program to swap two consecutive numbers in the array

import array

arr=array.array('i',[])
num = int(input('Enter No of Elements in Array: '))

for i in range(num):
    
    ele=int(input())

    arr.append(ele)

print(arr)

for i in range(0,len(arr),2):

    temp=arr[i]
    arr[i]=arr[i+1]
    arr[i+1]=temp

print(arr)

#Input : [1,2,3,4,5,6,7,8]
#Output:[2,1,4,3,6,5,8,7]
