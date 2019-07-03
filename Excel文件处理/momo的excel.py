#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd

excel = pd.read_excel("C:/Users/Administrator/Desktop/编码/a.xlsx",skiprows=[0],skip_footer=1)
#print(excel)
phone1 = excel['手机号码']
phone2 = excel['手机号码.1']
phone3 = excel['手机号码.2']
money1 = excel['发送金额（元）']
money2 = excel['发送金额（元）.1']
money3 = excel['发送金额（元）.2']
newExcel = pd.DataFrame()
newExcel['手机号码'] = pd.concat([phone1,phone2,phone3],ignore_index=True)
newExcel['发送金额（元）'] = pd.concat([money1,money2,money3],ignore_index=True)
#print(newExcel)#
#result=pd.concat([newExcel],axis=0)
newExcel.to_excel('C:/Users/Administrator/Desktop/编码/b.xlsx',index=False)
