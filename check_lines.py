# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:42:42 2021

@author: Alex
"""


import glob2
import sys

total = 0


# Reading from file 
def lineNumbers (filesInDir):
    Counter = 0
    Content = filesInDir.read() 
    CoList = Content.split("\n") 
  
    for i in CoList: 
        if i: 
            Counter += 1
          
    print(filesInDir.name, '\t - ', Counter)
    return Counter


usrPath = input("Enter path to directory: ")
   
sys.stdout = open("SumOfLines.txt", "w")

    
for file in glob2.glob(usrPath+"\\**\\*.cs"):
    currentFile = file
    currentFile = open(currentFile, encoding ="utf8")
    strNumbers = lineNumbers(currentFile)
    total +=strNumbers
    
print ("Sum of lines:\t", total)
