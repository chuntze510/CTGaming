# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
f = open('number.txt', 'r+')
idstring=f.read()
idfind ='cd88'
idpostion=idstring.find(idfind)
f.seek(9,0)
f.write('hello')  
f.close()
"""
import os

#path = r'C:\Users\user\Desktop'
path=os.getcwd()
dirs = os.listdir(path)
print(path)
for file in dirs:
    if not file.endswith(".txt"):
        continue
    f = open(file, 'r+')
    print("start to read txt")
    #idstring = f.read()
    text = []
    for line in f:
        text.append(line)
    if text[1][0]=='#' :
       text.pop(1)
       print("開始刪除")
       f.truncate(0)
       f.seek(0)
       n=len(text)
       print('現在長度',n)
       for i in range(0,n):
           f.writelines(text[i])
    f.close()
print("complete!!!")

#teprint("共有多長:",n)

"""

"""    
 
    
    


""""    
def check all()
    for i in range(0,1):
        print(text[i])
"""    
