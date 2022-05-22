#Write a program to sum alternate number from the given array

import array

arr=array.array('i',[])
num = int(input('Enter No of Elements in Array: '))

for i in range(num):
    
    ele=int(input())

    arr.append(ele)

print(arr)
sum=0
for ele in arr:

    if arr.index(ele)%2==0:
        sum=sum+ele
print(sum)

#Input : [1,2,3,4,5,6,7]
#Output : 16 // 1 + 3 + 5 + 7
