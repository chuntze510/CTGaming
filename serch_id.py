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

# path = r'C:\Users\user\Desktop'
path = os.getcwd()
dirs = os.listdir(path)
print(path)
for file in dirs:
    if not file.endswith(".txt"):
        continue
    f = open(file, 'r+')
    print("start to read txt")
    text = []
    for line in f:
        text.append(line)
    n=len(text)
    print(n)
    for i in range(1,n):
        if text[i][0] == '1' and text[i][1] == '1':
            print('找到奇怪的字')
            text.insert(i,'11 22 33 55 66 77 99\n')
            text.pop(i+1)
            #text.remove(i)
        else:
            print('沒找到')
    f.truncate(0)
    f.seek(0)
    n=len(text)
    print('現在長度',n)
    for i in range(0,n):
        f.writelines(text[i])        
    f.close()
print("complete!!!")

# reprint("減少了一行!",n)

"""

"""

""""    
def check all()
    for i in range(0,1):
        print(text[i])
"""
