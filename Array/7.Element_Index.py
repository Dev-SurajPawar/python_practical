#Write a program to search a given element and prints its index

import array

arr=array.array('i',[])
num = int(input('Enter No of Elements in Array: '))

for i in range(num):
    
    ele=int(input())

    arr.append(ele)

print(arr)

num=int(input('Enter Search Element: '))
for i in range(len(arr)):
    if num==arr[i]:
        print('Index: ',i)
        
#Input : [1,2,43,5,66,87,9]
#Search = 43
#Output : index = 2
