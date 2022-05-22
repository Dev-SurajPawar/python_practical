#Write a program to find min and max from the given array

import array

arr=array.array('i',[])
num = int(input('Enter No of Elements in Array: '))

for i in range(num):
    
    ele=int(input())

    arr.append(ele)

print(arr)
print('Min: ',min(arr))
print('Max: ',max(arr))

#Input : [1,43,65,71,89,55]
#Output : min = 1
#	  max = 89
