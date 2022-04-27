# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:41:28 2022
a
@author: Semir
"""
import csv
    

"reads a list of the the data from rastagrid in rows"
rowlist = []
"creates a list of the environment"
environment = []
    
"open the rastergrid text file from folder"

with open('raster_grid.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        environment.append(row)
        for value in row:
            rowlist.append(value)
            
            
#Testing environment data is being read in correctly 
# print (environment)




