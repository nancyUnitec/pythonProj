# -*- coding: utf-8 -*-   
      
import os  
import logging
import hashlib

import csv
      
# readme:
# put all the csv files in the csv folder
# then put this file and the csv folder in the same path
# then in this path, run this py file, then see the result in the result.txt

def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        print(root) #当前目录路径  
        print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件

    path_out = 'result.txt'
    file_out = open(path_out,'w')

    for i in range (len(files)):
        print(i ,files[i]) 
        file_out.write(" -----------------------------------------------------------------\n ")
        file_out.write(files[i]+" :\n ")
        # searchInCsvFile(csvFile,column,target)
        target = "10240503"
        searchInCsvFile(files[i],target,file_out)

    file_out.close()

# def searchInCsvFile(csvFile,column,target):
def searchInCsvFile(file, targetPID, outputFile):
    fileName = "csv/"+file
    csvFile = open(fileName, "r") 
    reader = csv.reader(csvFile)
    # data = []
    count = 0
    pid_col = -1
    for item in reader:
        count += 1
        if count == 1:
            title = item
            col_num = len(item)
            for i in range (len(item)):
                if item[i] == "PID":
                    print("PID column is: ",i)
                    pid_col = i
        
        elif count>1:
            if pid_col>0:
                if item[pid_col] == targetPID:
                    s = set(zip(title,item))
                    print(s)
                    for j in range (col_num):
                        outputFile.write(title[j]+" : "+item[j]+" , ")
                    outputFile.write(" \n ")

file_name("csv")