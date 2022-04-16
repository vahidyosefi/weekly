#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 03:22:35 2019

@author: vahid
"""

#from IPython import get_ipython
#get_ipython().magic('reset -sf')


def func_get_and_transfer_week_v1 (df1,df2,df3):
    
    
    import pandas as pd
    # import numpy as np
    # import datetime

    df0=pd.DataFrame()


##### input data
#df2 = pd.read_excel('telewebion_99_09.xlsx')
#df3 = pd.read_excel('lenz-99-09.xlsx')
#df4 = pd.read_excel('tva_99_09.xlsx')

######## sepeher **************

    dfsp1= df1

    dfsp1['dur'] = dfsp1['dur']/60

    dfsp1 = dfsp1.rename(columns={'channel': 'ch', 'Name_Item': 'نام برنامه', 'Time_Play': 'TIME','EP':'تاریخ پایان','visit': 'تعداد بازدید','dur':'مدت بازدید'})
#        df1["تاریخ پایان"] = ""
    # dfsp1["مدت بازدید"] = ""
    dfsp1["اپراتور"] = "سپهر" 
    
    # del dfsp1['@timestamp']
    
    del dfsp1['u_visit']
    del dfsp1['Time_Play_x']
    del dfsp1['ID_Day_Item']
    del dfsp1['Dec_Summary']
    del dfsp1['DTDay']
    del dfsp1['Length']

    dfsp1 = dfsp1[['ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','اپراتور']]
    dfsp1.to_excel(r'D:\python\Weekly\progress\Prepross\Estandard\sepeher_Sv1.xlsx',index=False)
    print('سپهر')






#lenz***************

#    f_input1=len(df3.index)
#
#    print ('تعداد کل سطرهای ورودی لنز',f_input1)
#
#    try:
#        df3 = df3.drop(columns=8)
#    except:
#        pass   
##bb = aa.drop(columns='Unnamed: 8')
#	
#			
#    df3.columns =['Channel ID','Channel Name','Program Name','Begin Time','End Time','Total duration(Hour)','Total Access times','Recorded times']
#
#    df3['Channel ID'] = df3['Channel ID'].astype(str)
#    df3 = df3[~df3['Channel ID'].str.contains('Avg')]
    
#    del remove blank in Channel ID

    df2["اپراتور"] = "لنز" 
    df2.columns=['nm','ch', 'نام برنامه','TIME','تاریخ پایان','مدت بازدید','تعداد بازدید','نامشخص','اپراتور']
    del df2['nm']
    del df2['نامشخص']
    # df3['مدت بازدید'] = df3['مدت بازدید'] *60
    df2.to_excel(r'D:\python\Weekly\progress\Prepross\Estandard\lenz_Sv1.xlsx', index=False)
    print('لنز')
#***********************
#iranseda**************************
    
    df3["اپراتور"] = "ایران صدا" 
    # del df4['Subtitle']
    # del df4['Users']
    df3["مدت بازدید"] = ""
    # df4.loc[(df4['Avg. Duration (sec)'].isnull()),'Avg. Duration (sec)'] = "0"
    # df4['Avg. Duration (sec)'] = df4['Avg. Duration (sec)']/3600
    df3 = df3.rename(columns={'t_name': 'ch','c_name': 'نام برنامه', 'year_': 'TIME', 'visit': 'تعداد بازدید'})
    df3 = df3.rename(columns={'h_time': 'ساعت'})
    df3 = df3[['ch', 'نام برنامه','TIME','ساعت','مدت بازدید','تعداد بازدید','اپراتور']]
    # df4.loc[(df4['مدت بازدید'].isnull()),'مدت بازدید'] = "0"
    df3.to_excel(r'D:\python\Weekly\progress\Prepross\Estandard\iranseda_Sv1.xlsx', index=False)
    print('ایران صدا')
    
    
    
    
    
    
    
#*********************** extract date



  
    dfsp1 ['TIME'] = pd.to_datetime(dfsp1.TIME)
    dfsp1['سال'] = dfsp1['TIME'].dt.year
    dfsp1['ماه'] = dfsp1['TIME'].dt.month
    dfsp1['ماه'] = dfsp1['ماه'].apply(lambda x: '{0:0>2}'.format(x))
    dfsp1['روز'] = dfsp1['TIME'].dt.day
    dfsp1['روز'] = dfsp1['روز'].apply(lambda x: '{0:0>2}'.format(x))
    dfsp1['ساعت'] = dfsp1['TIME'].dt.hour
    dfsp1['ساعت'] = dfsp1['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
    dfsp1['تاریخ'] = dfsp1[dfsp1.columns[7:]].apply(
        lambda x: ''.join(x.dropna().astype(str).astype(str)),
        axis=1)
 
    
    
    df2['TIME'] = pd.to_datetime(df2.TIME)
    df2['سال'] = df2['TIME'].dt.year
    df2['ماه'] = df2['TIME'].dt.month
    df2['ماه'] = df2['ماه'].apply(lambda x: '{0:0>2}'.format(x))
    df2['روز'] = df2['TIME'].dt.day
    df2['روز'] = df2['روز'].apply(lambda x: '{0:0>2}'.format(x))
    df2['ساعت'] = df2['TIME'].dt.hour
    df2['ساعت'] = df2['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
    df2['تاریخ'] = df2[df2.columns[7:]].apply(
        lambda x: ''.join(x.dropna().astype(str).astype(str)),
        axis=1)
    
    
    
    df3['TIME'] = pd.to_datetime(df3.TIME)
    df3['سال'] = df3['TIME'].dt.year
    df3['ماه'] = df3['TIME'].dt.month
    df3['ماه'] = df3['ماه'].apply(lambda x: '{0:0>2}'.format(x))
    df3['روز'] = df3['TIME'].dt.day
    df3['روز'] = df3['روز'].apply(lambda x: '{0:0>2}'.format(x))
    # df5['ساعت'] = df5['TIME'].dt.hour
    
    df3 = df3[['ch','نام برنامه','TIME','اپراتور','تعداد بازدید','مدت بازدید','سال','ماه','روز','ساعت']]
    
    df3['ساعت'] = df3['ساعت'].apply(lambda x: '{0:0>2}'.format(x))
    df3['تاریخ'] = df3[df3.columns[6:]].apply(
        lambda x: ''.join(x.dropna().astype(str).astype(str)),
        axis=1)
    
    # del df5['تاریخ']
    df3.to_excel(r'D:\python\Weekly\progress\Prepross\Estandard\iranseda_2_Sv1.xlsx', index=False)
    print('ایران صدا') 
    
    
    
    
    
    
    
    
    """change channel name sepeher """  
    try:
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'یک': 'شبکه 1'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'دو': 'شبکه 2'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'سه': 'شبکه 3'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'چهار': 'شبکه 4'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'تهران': 'شبکه 5'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'پنج': 'شبکه 5'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کودک': 'پویا'})
        
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'جام‌جم ۱': 'جام جم 1'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما آوا': 'رادیو آوا'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما ورزش': 'رادیو ورزش'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما ایران': 'رادیو ایران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما پیام': 'رادیو پیام'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما تهران': 'رادیو تهران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما جوان': 'رادیو جوان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'رادیونما گفتگو': 'رادیو گفتگو '})
        
        
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'آبادان': 'استانی آبادان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'آذربایجان غربی': 'استانی آذربایجان غربی'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'اصفهان': 'استانی اصفهان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'افلاک': 'استانی افلاک'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'البرز': 'استانی البرز'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'ایلام': 'استانی ایلام'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'گیلان - باران': 'استانی باران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'بوشهر': 'استانی بوشهر'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'یزد - تابان': 'استانی تابان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خراسان رضوی': 'استانی خراسان رضوی'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خوزستان': 'استانی خوزستان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'دنا': 'استانی دنا'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'سبلان': 'استانی سبلان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'سهند': 'استانی سهند'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'فارس': 'استانی فارس'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'قزوین': 'استانی قزوین'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کردستان': 'استانی کردستان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'مازندران - تبرستان': 'استانی مازندران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'مازندران': 'استانی مازندران'})
        
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'سیستان و بلوچستان - هامون': 'استانی هامون'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'هامون': 'استانی هامون'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'همدان - سینا': 'استانی همدان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'همدان': 'استانی همدان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خراسان شمالی - اترک': 'استانی خراسان شمالی -اترک'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خراسان جنوبی - خاوران': 'استانی خراسان جنوبی -خاوران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خراسان جنوبی': 'استانی خراسان جنوبی -خاوران'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'زنجان - اشراق': 'استانی زنجان-اشراق'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'اشراق': 'استانی زنجان-اشراق'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'زاگرس': 'استانی کرمانشاه-زاگرس'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'آفتاب': 'استانی مرکزی-آفتاب'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'مرکزی - آفتاب': 'استانی مرکزی-آفتاب'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'شبکه ایلام': 'استانی ایلام'})
#    df1['ch'] = df1['ch'].replace({'دنا': 'استانی کهگیلویه و بویر احمد - دنا'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'تابان': 'استانی تابان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'چهارمحال‌بختیاری': 'استانی چهار محال بختیاری - جهان بین'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'چهار محال بختیاری - جهان بین': 'استانی چهار محال بختیاری - جهان بین'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'چهارمحال بختیاری': 'استانی چهار محال بختیاری - جهان بین'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'جهان بین': 'استانی چهار محال بختیاری - جهان بین'})
        
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'هرمزگان - خلیج فارس': 'استانی خلیج فارس'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'خلیج فارس': 'استانی خلیج فارس'})
        
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'گلستان - سبز': 'استانی گلستان-سبز'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'گلستان': 'استانی گلستان-سبز'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'سمنان': 'استانی سمنان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'قم - نور': 'استانی قم-نور'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'نور': 'استانی قم-نور'})

        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کرمان': 'استانی کرمان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'مهاباد': 'استانی مهاباد'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'العالم سوریه': 'العالم'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'آذربایجان شرقی - سهند': 'استانی آذربایجان شرقی - سهند'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'اردبیل - سبلان': 'استانی اردبیل - سبلان'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'آی فیلم فارسی':'آی فیلم'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'لرستان - افلاک':'استانی لرستان - افلاک'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کهگیلویه و بویر احمد - دنا':'استانی کهگیلویه و بویر احمد - دنا'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کرمانشاه - زاگرس':'استانی کرمانشاه - زاگرس'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کرمانشاه':'استانی کرمانشاه - زاگرس'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({'کیش':'استانی کیش'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({ 'قران':'قرآن'})
        dfsp1 ['ch'] = dfsp1 ['ch'].replace({ 'سحر - اردو':'سحر اردو'})
        
        
        
        dfsp1.loc[(dfsp1['ch'].isnull()),'ch'] = "سایر"
        
        # df1.to_excel(r'D:\python\Clean_offline\input\source\data_database\out\sepeher.xlsx',index=False)
    except:
        pass 
    
    dfsp1['نببت'] = dfsp1['نام برنامه']  

    # df1['نببت'] = df1['نام برنامه']
 
    df2['نببت'] = df2['نام برنامه']
    df3['نببت'] = df3['نام برنامه']
    # df4['نببت'] = df4['نام برنامه']
    
        
    """ change chanel name in iranseda """
    
    df3['ch'] = df3['ch'].replace({'آوا ': 'رادیو آوا'})
    df3['ch'] = df3['ch'].replace({'ورزش':'رادیو ورزش'})
    df3['ch'] = df3['ch'].replace({'ايران ': 'رادیو ایران'})
    df3['ch'] = df3['ch'].replace({'پیام': 'رادیو پیام'})
    df3['ch'] = df3['ch'].replace({'تهران': 'رادیو تهران'})
    df3['ch'] = df3['ch'].replace({'جوان': 'رادیو جوان'})
    # df1['ch'] = df1['ch'].replace({'رادیونما گفتگو': 'رادیو گفتگو '})


    


#    del df000

#df0=df0.append(df1)


    df0=df0.append(dfsp1)
    df0=df0.append(df3)
    df0=df0.append(df2)
    
#    df0['نببت']=df0['نام برنامه']

    df0.to_excel(r'D:\python\Weekly\progress\Prepross\Estandard\stadard_1.xlsx', index=False)
    print('ادغام')
#    df000 = df0
    

    df0 = df0.rename(columns={'TIME': 'تاریخ شروع'})
    del df0['ماه']
    del df0['روز']
    del df0['سال']


    df0['ch'] = df0['ch'].str.replace('شبکه ','')
    df0['ch'] = df0['ch'].str.replace('ي','ی') 
    df0['نام برنامه'] = df0['نام برنامه'].str.replace('سریال ','مجموعه ')
    df0['نام برنامه'] = df0['نام برنامه'].str.replace(' سریال',' مجموعه')
    df0['نام برنامه'] = df0['نام برنامه'].str.replace('سریال','مجموعه ')     
    df0 = df0.rename(columns={'نام برنامه': 'Name'})

    df0['Name'] = df0['Name'].astype(str)
    df0['Name'] = df0['Name'].str.replace('ي','ی')
    df0['Name'] = df0['Name'].str.replace('قسمت','قسمت ')    

    df0 = df0[~df0['Name'].str.contains('اذان')]
    df0 = df0[~df0['Name'].str.contains('میان برنامه')]
    df0 = df0[~df0['Name'].str.contains('میانبرنامه')]
    df0 = df0[~df0['Name'].str.contains('میان‌برنامه')]
    df0 = df0[~df0['Name'].str.contains('بازرگانی')]
    df0 = df0[~df0['Name'].str.contains('آگهی')]
    df0 = df0[~df0['Name'].str.contains('اگهی')]
    df0 = df0[~df0['Name'].str.contains('وله')]
    df0 = df0[~df0['Name'].str.contains('ارم استیشن')]
    df0 = df0[~df0['Name'].str.contains('آرم استیشن')]
    df0 = df0[~df0['Name'].str.contains('ارم تایم')]
    df0 = df0[~df0['Name'].str.contains('آرم تایم')]
    df0 = df0[~df0['Name'].str.contains('برنامه بعدی')]
    df0 = df0[~df0['Name'].str.contains('اعلام برنامه')]
    df0 = df0[~df0['Name'].str.contains('معرفی برنامه')]
    df0 = df0[~df0['Name'].str.contains('نماهنگ')]
    df0 = df0[~df0['Name'].str.contains('کپشن')]
    df0 = df0[~df0['Name'].str.contains('مولودی')]
    df0 = df0[~df0['Name'].str.contains('آنونس')]
    df0 = df0[~df0['Name'].str.contains('انونس')]
    df0 = df0[~df0['Name'].str.contains('تیتراژ')]
    df0 = df0[~df0['Name'].str.contains('تیزر')]
    df0 = df0[~df0['Name'].str.contains('هم خوانی')]
    df0 = df0[~df0['Name'].str.contains('همخوانی')]
    df0 = df0[~df0['Name'].str.contains('هم‌خوانی')]
    df0 = df0[~df0['Name'].str.contains('ارتباط مستقیم')]
    df0 = df0[~df0['Name'].str.contains('کلیپ')]
    df0 = df0[~df0['Name'].str.contains('آگهی قبل ')]
    df0 = df0[~df0['Name'].str.contains('ذکر')]
    df0 = df0[~df0['Name'].str.contains('دعا')]
    df0 = df0[~df0['Name'].str.contains('تقدیم برنامه')]
    df0 = df0[~df0['Name'].str.contains('برنامه از')]
    df0 = df0[~df0['Name'].str.contains('حسنی')]
    df0 = df0[~df0['Name'].str.contains('پیش پرده')]
    df0 = df0[~df0['Name'].str.contains('اکنون')]
    df0 = df0[~df0['Name'].str.contains('نشان برنامه')]

  

    df0['ch'] = df0['ch'].astype(str)
    df0['ch1']=df0.loc[(df0.ch == 'دو'), 'ch'] = 'شبکه 2' 
    df0['ch1']=df0.loc[(df0.ch == 'سه'), 'ch'] = 'شبکه 3'
    df0['ch1']=df0.loc[(df0.ch == 'چهار'), 'ch'] = 'شبکه 4'
    df0['ch1']=df0.loc[(df0.ch == 'تهران'), 'ch'] = 'شبکه 5'
    df0['ch1']=df0.loc[(df0.ch == 'یک'), 'ch'] = 'شبکه 1'

    df0['ch1']=df0.loc[(df0.ch == '۱'), 'ch'] = 'شبکه 1' 
    df0['ch1']=df0.loc[(df0.ch == '۲'), 'ch'] = 'شبکه 2'
    df0['ch1']=df0.loc[(df0.ch == '۳'), 'ch'] = 'شبکه 3'
    df0['ch1']=df0.loc[(df0.ch == '۴'), 'ch'] = 'شبکه 4'
    df0['ch1']=df0.loc[(df0.ch == '۵'), 'ch'] = 'شبکه 5'
    df0['ch1']=df0.loc[(df0.ch == '3 HD'), 'ch'] = 'شبکه 3'
    df0['ch1']=df0.loc[(df0.ch == 'ورزش HD'), 'ch'] = 'ورزش'
    df0['ch1']=df0.loc[(df0.ch == '1 HD'), 'ch'] = 'شبکه 1'
    df0['ch1']=df0.loc[(df0.ch == 'آی فیلم HD'), 'ch'] = 'آی فیلم'
    df0['ch1']=df0.loc[(df0.ch == 'نسیم HD'), 'ch'] = 'نسیم'
    df0['ch1']=df0.loc[(df0.ch == 'مستند HD'), 'ch'] = 'مستند'  
    df0['ch1']=df0.loc[(df0.ch == 'HDTV3'), 'ch'] = 'شبکه 3'
    
    
    df0['ch1']=df0.loc[(df0.ch == 'بازار'), 'ch'] = 'ایران کالا'
    df0['ch1']=df0.loc[(df0.ch == 'ifilm'), 'ch'] = 'آی فیلم'
    df0['ch1']=df0.loc[(df0.ch == 'Press TV'), 'ch'] = 'پرس تی وی'
    df0['ch1']=df0.loc[(df0.ch == 'اچ دی تماشا'), 'ch'] = 'تماشا'
    
    df0['ch1']=df0.loc[(df0.ch == '1'), 'ch'] = 'شبکه 1' 
    df0['ch1']=df0.loc[(df0.ch == '2'), 'ch'] = 'شبکه 2'
    df0['ch1']=df0.loc[(df0.ch == '3'), 'ch'] = 'شبکه 3'
    df0['ch1']=df0.loc[(df0.ch == '4'), 'ch'] = 'شبکه 4'
    df0['ch1']=df0.loc[(df0.ch == '5'), 'ch'] = 'شبکه 5'

    df0['ch1']=df0.loc[(df0.ch == 'تماشا HD'), 'ch'] = 'تماشا'
    df0['ch1']=df0.loc[(df0.ch == 'سه HD'), 'ch'] = 'شبکه 3'
    df0['ch1']=df0.loc[(df0.ch == 'پنج'), 'ch'] = 'شبکه 5'

#    df0000 = df0
#### part tag
    df0.loc[df0['ch'].str.contains('پویا'), 'tag'] = 'کودک'
    df0.loc[df0['ch'].str.contains('ورزش'), 'tag'] = 'ورزشی'
    df0.loc[df0['ch'].str.contains('دیجتون'), 'tag'] = 'کودک'
    df0.loc[df0['ch'].str.contains('تیوا کودک'), 'tag'] = 'کودک'
    df0.loc[df0['ch'].str.contains('شاپرک'), 'tag'] = 'کودک'
    
    df0.loc[df0['Name'].str.contains('خبر'), 'tag'] = 'اخبار'
    df0.loc[df0['Name'].str.contains('فوتبال'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('والیبال'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('فوتسال'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains(' کشتی فرنگی'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('کشتی آزاد'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('لیگ برتر کشتی'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('خانه کشتی'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('ورزش'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('اسکی'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('هاکی'), 'tag'] = 'ورزشی'
    
    df0.loc[df0['Name'].str.contains('مجموعه'), 'tag'] = 'مجموعه تلویزیونی'
    df0.loc[df0['Name'].str.contains('فیلم'), 'tag'] = 'فیلم سینمایی'
    df0.loc[df0['Name'].str.contains('اخبار'), 'tag'] = 'اخبار'
    df0.loc[df0['Name'].str.contains('سینمایی'), 'tag'] = 'فیلم سینمایی'
    df0.loc[df0['ch'].str.contains('اخبار ورزشی'), 'tag'] = 'ورزشی'
    df0.loc[df0['Name'].str.contains('موسیقی فیلم'), 'tag'] = 'سایر'
    df0.loc[df0['Name'].str.contains('کودک'), 'tag'] = 'کودک'
    df0.loc[df0['Name'].str.contains('انیمیشن'), 'tag'] = 'کودک'
    df0.loc[df0['Name'].str.contains('مستند'), 'tag'] = 'مستند'

    
    df0 = df0[~df0['ch'].str.contains('سایر')]
    df0 = df0[~df0['ch'].str.contains('_بدون عنوان')]    
    
   
#df0.loc[df0['Name'].str.contains('خبر'), 'tag'] = 'اخبار'
#df0.loc[df0['tag'].str.contains(''), 'tag'] = 'سایر'

    
### change the number

    df0['Name'] = df0['Name'].str.replace('0', '۰')
    df0['Name'] = df0['Name'].str.replace('1', '۱')
    df0['Name'] = df0['Name'].str.replace('2', '۲')
    df0['Name'] = df0['Name'].str.replace('3', '۳')
    df0['Name'] = df0['Name'].str.replace('4', '۴')
    df0['Name'] = df0['Name'].str.replace('5', '۵')
    df0['Name'] = df0['Name'].str.replace('6', '۶')
    df0['Name'] = df0['Name'].str.replace('7', '۷')
    df0['Name'] = df0['Name'].str.replace('8', '۸')
    df0['Name'] = df0['Name'].str.replace('9', '۹')

    df0['Name'] = df0['Name'].str.replace('٠', '۰')
    df0['Name'] = df0['Name'].str.replace('١', '۱')
    df0['Name'] = df0['Name'].str.replace('٢', '۲')
    df0['Name'] = df0['Name'].str.replace('٣', '۳')
    df0['Name'] = df0['Name'].str.replace('٤', '۴')
    df0['Name'] = df0['Name'].str.replace('٥', '۵')
    df0['Name'] = df0['Name'].str.replace('٦', '۶')
    df0['Name'] = df0['Name'].str.replace('٧', '۷')
    df0['Name'] = df0['Name'].str.replace('٨', '۸')
    df0['Name'] = df0['Name'].str.replace('٩', '۹')


    df0 = df0.rename(columns={'ch': 'نام شبکه'})
    df0 = df0.rename(columns={'Name': 'نام برنامه'})
    df0 = df0.rename(columns={'tag': 'جنس'})
    
    
    df0['نام شبکه'] = df0['نام شبکه'].replace({'اصفهان': 'استانی اصفهان'})

    df0['نام شبکه'] = df0['نام شبکه'].replace({'باران': 'استانی باران'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'خراسان رضوی': 'استانی خراسان رضوی'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'خوزستان': 'استانی خوزستان'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'سهند': 'استانی سهند'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'فارس': 'استانی فارس'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'کردستان': 'استانی کردستان'})
    

############# for maybe mistake in dictation
    df0['نام شبکه'] = df0['نام شبکه'].replace({'استانی ابادان': 'استانی آبادان'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'استانی آذریایجان غربی': 'استانی آذربایجان غربی'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'افلاک': 'استانی افلاک'})


    df0['نام شبکه'] = df0['نام شبکه'].replace({'قرآن و معارف اسلامی': 'قرآن'})
    df0['نام شبکه'] = df0['نام شبکه'].replace({'IFilm': 'آی فیلم'})

    df0['نام شبکه'] = df0['نام شبکه'].replace({'شتاب (اقتصاد و بورس)': 'شتاب'})
    df0.loc[(df0['جنس'] .isnull()) , 'جنس'] = "سایر"    
#df0["avg"] = ""
#df0[['تعداد بازدید']].where(df0[['نام شبکه']].values == 'شبکه 1').stack().mean()
    del df0['ch1']
#df0['avg']=df0[['تعداد بازدید']].where(df0[['نام شبکه']].values == 'تماشا').stack().mean()
#df0['avg1']=df0['تماشا']['avg']



    df0.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\astandard_out.xlsx', index=False)
    
#    df0000.to_excel(r'D:\python\EPG_vahid\input\source\Estandard\astandard_out_test.xlsx', index=False)
    print('استاندارد سازی و یکپارچه سازی داده ها تمام شد ')
    
    print('تفکیک شبکه ها و استانی در مرحله بعدی انجام خواهد گرفت')
    
    return df0
#************


