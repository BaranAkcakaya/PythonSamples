# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:16:08 2019

@author: lenovoz
"""

import openpyxl as pyxl
ktp = pyxl.load_workbook("kitap_6.xlsx")
sheet=ktp.get_sheet_by_name("sayfa 1")
for i in range(1,21):
    for j in range(1,4):
        temp=sheet.cell(i,j)
        if(temp.value>100 and temp.value<1000):
            print(temp.value)
ktp.close()