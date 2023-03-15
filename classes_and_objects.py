# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:01:31 2021

@author: kazi_031
"""

class patient(object):
    status = 'patient' #class variable
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        

steve = patient('Steve Mccornel','Male')

print(steve.status)


