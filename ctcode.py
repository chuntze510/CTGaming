import pandas as pd
df1 = pd.read_excel('./cp.xlsx')
df2 = pd.read_excel('./wlft.xlsx')
df3 = pd.read_excel('./ft.xlsx')
#找出type不一致的
checktype1=pd.merge(df1,df2,on=['bin','type'],how='outer')
checktype2=pd.merge(df1,df3,on=['bin','type'],how='outer')
checktype3=pd.merge(df2,df3,on=['bin','type'],how='outer')

typemsk1 = (checktype1['bin'].duplicated()==True)  #篩選條件
typecolst1 = ['bin']
typemsk2 = (checktype2['bin'].duplicated()==True)  #篩選條件
typecolst2 = ['bin']
typemsk3 = (checktype3['bin'].duplicated()==True)  #篩選條件
typecolst3 = ['bin']

#找出type不一致的合併+刪除重複
typemerge1=checktype1.loc[typemsk1,typecolst1].append(checktype2.loc[typemsk2,typecolst2])
typemerge2=typemerge1.append(checktype3.loc[typemsk3,typecolst3])
typemerge3=typemerge2.drop_duplicates()
typemerge3.index=list(range(typemerge3.shape[0]))
typemerge3.columns = ['Risk bin']




#找出bin沒有重複出現的

out1=pd.merge(df1,df2,on=['bin'],how='outer')
out2=pd.merge(df1,df3,on=['bin'],how='outer')
out3=pd.merge(df2,df3,on=['bin'],how='outer')

#補缺失值
out1['type_x'].fillna(value=-1, inplace=True)
out2['type_x'].fillna(value=-1, inplace=True)
out3['type_x'].fillna(value=-1, inplace=True)
out1['type_y'].fillna(value=-1, inplace=True)
out2['type_y'].fillna(value=-1, inplace=True)
out3['type_y'].fillna(value=-1, inplace=True)

mask1 = (out1['type_x']==-1) | (out1['type_y']==-1)  #篩選條件
cols1 = ['bin']
mask2 = (out2['type_x']==-1) | (out2['type_y']==-1)  #篩選條件
cols2 = ['bin']
mask3 = (out3['type_x']==-1) | (out3['type_y']==-1)  #篩選條件
cols3 = ['bin']

#找出special bin合併
merge1=out1.loc[mask1,cols1].append(out2.loc[mask2,cols2])
merge2=merge1.append(out3.loc[mask3,cols3])
merge3=merge2.drop_duplicates()
merge3.index=list(range(merge3.shape[0]))


final=pd.concat([typemerge3,merge3])

#輸出excel
final.to_csv('check_bdfile.csv', index=False)