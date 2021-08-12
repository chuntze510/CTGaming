# -*- coding: utf-8 -*-
"""
用來搜尋標頭修改後面字串的TOOL BY均澤 20210813
"""
import os

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
        for i in range(1,n):
            if text[i][0] == '1' and text[i][1] == '1':
                print('第',i+1,'行找到奇怪的字')
                text.insert(i,'11 22 33 55 66 77 99\n')
                text.pop(i+1)
            #text.remove(i)
            else:
                print('沒找到')
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





