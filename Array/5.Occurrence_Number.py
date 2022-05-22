#Write a program to find the occurrence of a given number from the array

import array

arr=array.array('i',[])
num = int(input('Enter No of Elements in Array: '))

for i in range(num):
    
    ele=int(input())

    arr.append(ele)

print(arr)
num=int(input())
count=0
for i in arr:

        if num==i :
            count+=1
print('Occurrence of ',num,' ',count)

#Input : [1,2,3,4,4,5,6,7]
#Occurrence count of number = 4
#Output: 2
