#!/bin/python3
#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
nums=[0,1,0,3,12]
list1=list()
count=0
len1=len(nums)

for i in nums:
    if(i==0):
        count+=1
    else:
        list1.append(i)

for i in range(count):
    list1.append(0)

nums=list1
print(list1)
print(nums)
