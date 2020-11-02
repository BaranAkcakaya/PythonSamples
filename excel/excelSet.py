# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 18:30:02 2019

@author: lenovoz
"""
import openpyxl as pyxl
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
ktp = pyxl.load_workbook("kitap_6.xlsx")
sheet=ktp.active
sheet=ktp.get_sheet_by_name("sayfa 1")
a=sheet['A10']
b=sheet['B8']
c=sheet['C12']
a.font=Font(color=colors.YELLOW,size=20)
b.font=Font(bold=True)
#c.font=Font()
sheet.title="tablo 1"
ktp.save("kitap_6.xlsx")
ktp.close()