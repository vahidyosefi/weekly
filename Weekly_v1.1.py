# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:09:46 2021

@author: vahid
"""

import pandas as pd
import numpy as np
import datetime
import os
import time

import datetime as dt

start = time.time() 


df0 = pd.DataFrame()
total = pd.DataFrame()

##### input data

df1 = pd.read_excel(r'D:\python\Weekly\input\weekly\10\sepher_1401_01_03.xlsx')
# df1 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\Aio-1400_09.xlsx')
# df2 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\telewebion_1400_09.xlsx')

df2 = pd.read_excel(r'D:\python\Weekly\input\weekly\10\lenz_1401_01_03.xlsx')
# df3_lenz = pd.read_csv(r'D:\python\Weekly\input\weekly\5\Statistic EPG Program viewing_2022-02-02_10-31-49.csv', header=None)
# df4 = pd.read_excel(r'D:\python\EPG_vahid\input\source\sample\tva_1400_09.xlsx')

df3 = pd.read_excel(r'D:\python\Weekly\input\weekly\10\iranseda_1400_12.xlsx')

#python -W ignore your_script_name.py


df2.dtypes

df2['Begin Time']=df2['Begin Time'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

df2['ttt']= df2['Begin Time'].astype(str)
df2['t1'] = df2['ttt'].str.replace('-','/')
df2['Begin Time'] = df2['t1'].str[:16]

del df2['ttt']
del df2['t1']





# df3_lenz.to_excel(r'D:\python\Weekly\input\weekly\5\lenz_14001113.xlsx', index=False)

from func_get_and_transfer_week_v1 import *


df_pross = func_get_and_transfer_week_v1(df1,df2,df3)



# path_month= r'D:\python\EPG_vahid\input\source\Estandard\astandard_out.xlsx'


### input date

# Azar_1400

start_date = '04-06-2022-23:59:59'
end_date = '04-12-2022-23:59'


print('Get Date and Radif')

## input  ردیف 

""" for divide file , sarsari , ostani , radio , ekhtesasi """
from func_sarsari_weekly_v2 import *

[ostani,radio,bronmarzi,ekhtesasi]= func_sarsari_weekly_v2(df_pross,start_date,end_date,53)

#ostani.to_excel( 'test.xlsx', index=False)

from Func_Mekanizeh_ostani_weekly import *
#Func_Mekanizeh_ostani (df50)
number =Func_Mekanizeh_ostani_weekly (ostani)
print('چاپ شبکه استانی به تفکیک انجام گرفته است',number)


print ('فراخوانی تابع رادیویی جهت تفکیک شبکه های رادیویی')
from Func_Mekanizeh_radio_weekly import *
number =Func_Mekanizeh_radio_weekly (radio)
print('چاپ شبکه رادیویی به تفکیک انجام گرفته است',number)

print ('فراخوانی تابع رادیویی جهت تفکیک شبکه های برون مرزی')
from Func_Mekanizeh_bronmarzi_weekly import *
number =Func_Mekanizeh_bronmarzi_weekly (bronmarzi)
print('چاپ شبکه برون مرزی به تفکیک انجام گرفته است',number)

print ('فراخوانی تابع اختصاصی جهت تفکیک شبکه های اختصاصی')
from Func_Mekanizeh_ekhtesasi_weekly import *
number =Func_Mekanizeh_ekhtesasi_weekly (ekhtesasi)
print('چاپ شبکه اختصاصی به تفکیک انجام گرفته است',number)


# ostani.tfunctoolsexcel
# excel(r'D:\python\EPG_vahid\input\source\sample\tva_1400_08.xlsx')


""" for delete files in outin the folder """

vahid = 1    
for vahid in range(50):
#     vahid = 13
    print("number of chanel sarasari", vahid)
    
    ch= vahid+1
    
    clean1 = r'D:\python\Weekly\progress\channel\sarasari\out\{}.xlsx'.format(ch)
    try:
        os.remove(clean1)
    except:
        pass
    clean2 = r'D:\python\Weekly\progress\channel\radio\out\{}.xlsx'.format(ch)
    try:
        os.remove(clean2)
    except:
        pass
    clean3 = r'D:\python\Weekly\progress\channel\ostani\out\{}.xlsx'.format(ch)
    try:
        os.remove(clean3)
    except:
        pass
    clean4 = r'D:\python\Weekly\progress\channel\ekhtesasi\out\{}.xlsx'.format(ch)
    try:
        os.remove(clean4)
    except:
        pass
    
    clean5 = r'D:\python\Weekly\progress\channel\bronmarzi\out\{}.xlsx'.format(ch)
        
                   
    try:
        os.remove(clean5)
    except:
        pass

print('فولدرها پاک شده ')

""" clean system """



from func_epg_clean_v20 import *

vahid = 1    
for vahid in range(25):
#     vahid = 13
    print("number of chanel sarasari", vahid)
    
    ch= vahid+1
    
    vorodi  = r'D:\python\Weekly\progress\channel\sarasari\in\{}.xlsx'.format(ch)
    khoroji = r'D:\python\Weekly\progress\channel\sarasari\out\{}.xlsx'.format(ch)
    try:
        d= func_epg_clean_v20(vorodi,khoroji,ch)
    except:
        pass
print('out tabehe',d)


vahid = 1    
for vahid in range(20):
#     vahid = 13
    print("number of chanel radio", vahid)
    
    ch= vahid+1
    
    vorodi  = r'D:\python\Weekly\progress\channel\radio\in\{}.xlsx'.format(ch)
    khoroji = r'D:\python\Weekly\progress\channel\radio\out\{}.xlsx'.format(ch)
    try:
        d= func_epg_clean_v20(vorodi,khoroji,ch)
    except:
        pass
print('out tabehe',d)

vahid = 1    
for vahid in range(50):
#     vahid = 13
    print("number of chanel ostani", vahid)
    
    ch= vahid+1
    
    vorodi  = r'D:\python\Weekly\progress\channel\ostani\in\{}.xlsx'.format(ch)
    khoroji = r'D:\python\Weekly\progress\channel\ostani\out\{}.xlsx'.format(ch)
    try:
        d= func_epg_clean_v20(vorodi,khoroji,ch)
    except:
        pass
print('out tabehe',d)


vahid = 1    
for vahid in range(50):
#     vahid = 13
    print("number of chanel bronmarzi", vahid)
    
    ch= vahid+1
    
    vorodi  = r'D:\python\Weekly\progress\channel\bronmarzi\in\{}.xlsx'.format(ch)
    khoroji = r'D:\python\Weekly\progress\channel\bronmarzi\out\{}.xlsx'.format(ch)
    try:
        d= func_epg_clean_v20(vorodi,khoroji,ch)
    except:
        pass
print('out tabehe',d)

vahid = 1    
for vahid in range(50):
#     vahid = 13
    print("number of chanel ekhtesasi", vahid)
    
    ch= vahid+1
    
    vorodi  = r'D:\python\Weekly\progress\channel\ekhtesasi\in\{}.xlsx'.format(ch)
    khoroji = r'D:\python\Weekly\progress\channel\ekhtesasi\out\{}.xlsx'.format(ch)
    try:
        d= func_epg_clean_v20(vorodi,khoroji,ch)
    except:
        pass
print('out tabehe',d)





""" merge , sarsari , ostani , radio , ekhtesasi """ 



from func_merge  import *

vorodi =r'D:\python\Weekly\progress\channel\sarasari\out\*.xlsx'
khoji   = r'D:\python\Weekly\progress\merge\Type_merge\sarasari.xlsx'


func_merge(vorodi,khoji)

print('سراسری')

vorodi =r'D:\python\Weekly\progress\channel\radio\out\*.xlsx'
khoji   = r'D:\python\Weekly\progress\merge\Type_merge\radio.xlsx'

func_merge(vorodi,khoji)
print('رادیویی')

vorodi =r'D:\python\Weekly\progress\channel\ostani\out\*.xlsx'
khoji   = r'D:\python\Weekly\progress\merge\Type_merge\ostani.xlsx'


func_merge(vorodi,khoji)
print('استانی')

vorodi =r'D:\python\Weekly\progress\channel\bronmarzi\out\*.xlsx'
khoji   = r'D:\python\Weekly\progress\merge\Type_merge\bronmarzi.xlsx'


func_merge(vorodi,khoji)
print('استانی')

""" delete file mabaghi ekhtesasti """

os.remove(r'D:\python\Weekly\progress\channel\ekhtesasi\out\43.xlsx')


vorodi =r'D:\python\Weekly\progress\channel\ekhtesasi\out\*.xlsx'
khoji   = r'D:\python\Weekly\progress\merge\Type_merge\ekhtesasi.xlsx'

func_merge(vorodi,khoji)

print('اختصاصی')


#vorodi =r'D:\python\EPG_vahid\progress\merge\marge\*.xlsx'
#khoji   = r'D:\python\EPG_vahid\progress\merge\total.xlsx'

#func_merage(vorodi,khoji)

#print('ادغام کل')

##  for moien

i_radio= pd.read_excel (r'D:\python\Weekly\progress\merge\Type_merge\radio.xlsx')
i_radio['نوع'] = 'رادیویی'
i_bronmarzi= pd.read_excel (r'D:\python\Weekly\progress\merge\Type_merge\bronmarzi.xlsx')
i_bronmarzi['نوع'] = 'برون مرزی'
i_ostani= pd.read_excel (r'D:\python\Weekly\progress\merge\Type_merge\ostani.xlsx')
i_ostani['نوع'] = 'استانی'
i_ekhtesasi= pd.read_excel (r'D:\python\Weekly\progress\merge\Type_merge\ekhtesasi.xlsx')
i_ekhtesasi['نوع'] = 'اختصاصی'
i_sarasari= pd.read_excel (r'D:\python\Weekly\progress\merge\Type_merge\sarasari.xlsx')
i_sarasari['نوع'] = 'سراسری'

total=total.append(i_radio)
total=total.append(i_bronmarzi)
total=total.append(i_ostani)
total=total.append(i_ekhtesasi)
total=total.append(i_sarasari)


total.to_excel(r'D:\python\Weekly\progress\merge\total__.xlsx', index=False)


from func_change_Weekly  import *

[o_radio,o_bronmarzi,o_ostani,o_ekhtesasi,o_sarasari]=func_change_Weekly(i_radio,i_bronmarzi,i_ostani,i_ekhtesasi,i_sarasari)



#input_sarasari.to_excel(r'D:\python\EPG_vahid\progress\merage\total_moien_1.xlsx', index=False)

o_radio = o_radio.append(o_bronmarzi)
o_ostani = o_ostani.append(o_radio)
o_ekhtesasi = o_ekhtesasi.append(o_ostani)
o_sarasari = o_sarasari.append(o_ekhtesasi)



o_sarasari.to_excel(r'D:\python\Weekly\progress\merge\total_EPG.xlsx', index=False)

print('ادغام کل با ذکر حوزه')

from func_match_weekly  import *

func_match_weekly(o_sarasari)

print('match item with total data')

end = time.time()
# total time taken
mo = (end - start)/60
print ('مدت زمان اجرا برنامه به دقیقه',mo)
print(f"Runtime of the program is {end - start}")

