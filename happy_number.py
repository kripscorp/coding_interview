#!/bin/python3
#Write an algorithm to determine if a number n is "happy".
#A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#Return True if n is a happy number, and False if not.
n=19
l=list()
l.append(n)
while(n!=1):
    r=0
    s=0
    while(n>0):
        r=n%10
        q=n//10
        s+=r*r
        #print(n,q,r,s)
        n=q
    n=s
    if n in l:
        break
    else:
        l.append(n)
if n==1:
    print(True)
else:
    print(False)




exit()

l=list()

while(n!=1):
    r=0
    if n not in l:
        l.append(n)
    while(n>=10):
        r=n%10
        n=n//10
        print(n,r)
    n=(r*r)+(n*n)
    print(n)
    print(l)
    if n in l:
        break
if(n==1):
    print(True)
else:
    print(False)

    

#happyNumber=False
#while happyNumber:

