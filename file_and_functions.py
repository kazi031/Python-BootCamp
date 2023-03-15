# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:24:27 2021

@author: kazi_031
"""

# WRITE A FILE

# f = open('Output.txt','w')
# print(type(f))

# f.write('My name is Kazi Rafid Raiyan\nI study at Military Institute of Science and Technology\n')
# f.write('I am currently a final year Student\n')
# f.close()

# READ A FILE

# f = open('Output.txt','r')
# print(type(f))

# print(f.read())
# f.close()

# readline method

# print(f.readline())
# f.close()

# contents = f.readlines()
# f.close()

# ------------------------Function

# def hello():
#     print('Hello,world!')
    
# hello()

# def hello(name):
#     # print(f'Hello,{name}!')
#     print('Hello',name,'!')
    
# hello('Kazi')

# with default parameter
def hello(name='Giles'):
    # print(f'Hello,{name}!')
    print('Hello',name,'!')
    return name
hello('Kazi')
k = hello()
print(k)