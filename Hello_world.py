# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 20:06:05 2020

@author: kazi_031
"""

print('Hello World!')   
print('This is a python file')
i = 1

print(i)

i = i+1
print(i)

print(2**8)
print(7/3)

print(8/4)
#this gives an floating point value
print(8//4)
#this gives an integer value

numbers = [10,20,30,40,50]

for i in numbers:
    print(i,end=' ')
    

print('How\'s it going?')

print("One, 'two', \"three\", four, \\five\\ once,'I' caught a fish '//alive\\\\'") 


fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam) :
    print("index " + str(index) + ": " + str(height))
    
#we can't print strings and integers together in python
    
#for loops in string
    
for c in "family":
    print(c.capitalize(),end='')
    
j = 0
while j<10:
    print(j,end=' ')
    j = j + 1
    


b = "Hello, World!"
print(b[-5:-2])
    
length = len(fam)
print(length)

index = 0
while index < length :
    print(fam[index],end=' ')
    index += 1
