# -*- coding: utf-8 -*-
"""
Task intro: Bangla POS tagging and stemming syetem
Created on Fri Oct  4 22:33:52 2019

@author: Shafiq, Faculty,FSKKP,University Malaysia Pahang 
"""



import xlrd

workbook = xlrd.open_workbook("BanglaPOStagging.xlsx","rb")
sheet = workbook.sheet_by_index(0)
rows = []
for i in range(sheet.nrows):
    #print("Current Row number i is ",i)
    columns = []
    for j in range(sheet.ncols):
        #print("Current Column number j is ",j)
        columns.append(sheet.cell(i, j).value)
        #print(columns)
    rows.append(columns)
    
print("sheet.nrows",sheet.nrows)
print("sheet.ncols",sheet.ncols)

#print("Row value:")
print (rows)
print("Column value:")
print("Col 0 :",columns[0])
print("Col 1 :",columns[1])

print("Row value:")
print("Row 0:",rows[0])
print("Row 1:",rows[1])
print("Row 2:",rows[2])
print("Row 00:",rows[0][0])# first elemet of the row

r=sheet.nrows
c=sheet.ncols

textinput="খেলাম"
text=textinput.split()

for w in range(r):
    if text[0] in rows[w]:
        print("Item ",text[0] ,"is found in row no    ****",w)
    else: 
       print("Item is not found")
       
for w in range(c):
    if text[0] in columns[w]:
    #if columns[w] in textinput:
        print("Item is found in column no ****",w)
        print("Item ",text[0] , "is a ",rows[0][w])
        print("Item ",text[0] , "is a person",rows[2][c-1])
        print("Item ",text[0] , "is a number",rows[2][c-2])
        print("Normal form of the word",text[0]," is",columns[1])

    else: 
       #print("Item is not found")
       print()

#from pandas import read_excel
## find your sheet name at the bottom left of your excel file and assign 
## it to sheet_name
#my_sheet = 'Sheet1'
#file_name = 'BanglaPOStagging.xlsx' # name of your excel file
#df = read_excel(file_name, sheet_name = my_sheet)
#
#print(df.head())
       
        