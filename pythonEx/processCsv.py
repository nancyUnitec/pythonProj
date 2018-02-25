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

    target = getPIDArray()
    columns = getColumns()
    col_names = []
    for index, column in enumerate(columns):
        print(index, column) 
        col_names.append(column)

    print("\n csv files number is ",len(files))
    for i in range (len(files)):
        print("\n ",i ,files[i]) 
        file_out.write(" -----------------------------------------------------------------\n ")
        file_out.write(files[i]+" :\n ")
        # searchInCsvFile(csvFile,column,target)
        # target = "10240503"
        searchInCsvFile(files[i],target,columns,col_names)

    file_out.close()

def getPIDArray():
    fileName = "PID.csv"
    csvFile = open(fileName, "r") 
    reader = csv.reader(csvFile)
    # data = []
    # count = 0
    pid=[]
    # pid_col = -1
    for item in reader:
        patientID = item[0]
        # print("PID is: ",patientID)
        pid.append(patientID) 
        # count += 1
    return pid

def getColumns():
    fileName = "Columns.csv"
    csvFile = open(fileName, "r") 
    reader = csv.reader(csvFile)
    columns={}
    # pid_col = -1
    for item in reader:
        filename = item[0]
        columns[item[0]]=[]
        for i in range (1,len(item)):
            columns[item[0]].append(item[i])
        print("columns name is: ",columns)
        # print("columns are: ",columns)
        # pid.append(patientID) 
        # count += 1
    return columns

# def searchInCsvFile(csvFile,column,target):
def searchInCsvFile(file, targetPID, columns ,col_names):
    print("\n enter searchInCsvFile ")
    if not file in col_names:
        print("\n file is not concerned ")
        return
    path_out = "res/"+file+'_res.csv'
    # path_out = file+'_res.csv'
    outputFile = open(path_out,'w')
    for col in columns[file]:
        outputFile.write(col+",")
    outputFile.write("\n")

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
            for i in range (col_num):
                if item[i] == "PID":
                    print("\n PID column is: ",i)
                    pid_col = i
        
        elif count>1:
            if pid_col>0:
                if item[pid_col] in targetPID:
                    value = {}
                    for index in range (col_num): 
                        value[title[index]] = item[index]
                    # s = set(zip(title,item))
                    # print(s)
                    concern_col_num = len(columns[file]) 
                    for j in range (concern_col_num):
                        # if(title[j] in columns[file]):
                        # print(title[j]+":"+item[j]+", ")
                        # outputFile.write(item[j]+",")
                        outputFile.write(value[columns[file][j]]+",")
                    outputFile.write("\n")
    outputFile.close()

file_name("csv")
# pid = getPIDArray()
# print(pid)
# searchInCsvFile(file, targetPID, outputFile)
