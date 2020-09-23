# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:55:04 2019

@author: mathi
"""

import pandas as pd

DataNAP=pd.read_csv(r'C:\Users\mathi\Documents\GitHub\OctWeek1Projects\TheOutnetNetaporter\DataNAP.csv')
DataTON=pd.read_csv(r'C:\Users\mathi\Documents\GitHub\OctWeek1Projects\TheOutnetNetaporter\DataTON.csv')


def check():
    Brand=input("Brand ?")
    if Brand=='Q':
        print('Bye Bye')
        return None
    Category=input("Category ?")
    if Category=='Q':
        print('Bye Bye')
        return None
    elif (Brand not in DataTON.Brand.tolist()) or (Category not in DataNAP.Category.tolist()):
        print('non valid choice')
        return check()
    a=DataTON.OriginalPrice[(DataTON.OriginalPrice[(DataTON.Brand==Brand)&(DataTON.Category==Category)].index[0])]
    b=DataNAP.OriginalPrice[(DataNAP.OriginalPrice[(DataNAP.Brand==Brand)&(DataNAP.Category==Category)].index[0])]
    if a > b*1.2:
        print('cheateeeer')
        return check()
    else :
        print("thats's ok")
        return check()
        
print('Hello,\nWelcome on the comparator.\nPlease enter :')   
check()