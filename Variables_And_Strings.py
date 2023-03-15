# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:43:32 2021

@author: kazi_031
"""


# convert fahrenheit to celsius

fer = float(input('Enter The Temperature in Fahrenheit \n >>> '))
cel = (fer-32.0)*5/9
print('The Temperature in celsius is', round(cel,4) ,'deg Celcius')