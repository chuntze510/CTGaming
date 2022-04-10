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
 # -*- coding: utf-8 -*-
"""
用來搜尋標頭修改後面字串的TOOL BY均澤 20210813
"""
import os
import pandas as pd

def _main():
    path = os.getcwd()
    dirs = os.listdir(path)
    serch_id(dirs)
    print("Complete!!!Please double check!! ^_^")

def serch_id(my_dirs):
    for file in my_dirs:
        if not file.endswith(".txt"):
            continue
        f = open(file, 'r+')
        print("Start to read txt檔")
        text = []
        for line in f:
            text.append(line)
        n=len(text)
        print('初始行數為:',n)
        print('佩佩豬開始平移')
        for i in range(2,n):
                atemp=int(text[i][0:4])
                atemp=atemp+13
                atemp=str(atemp)
                atemp=atemp.rjust(4)
                text.insert(i,atemp+text[1][4:])
                text.pop(i+1)
            #text.remove(i)
        f.truncate(0)
        f.seek(0)
        n=len(text)
        print('現在行數一樣為:',n,"(若不一樣檔案可能有錯誤請小心檢查!)")
        #check_all
        for i in range(0,n):
            print(text[i])
        #寫入更改後的字
        for i in range(0,n):
            f.writelines(text[i]) 
        

        f.close()
    

if __name__ == '__main__':
    _main()
    
    


""""    

"""    
