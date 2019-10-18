#!/usr/bin/python3
# Excel查重
import pandas as pd
# Excel文件路径
path = '/Users/Ambert/Desktop/罗氏学会数据测试0924.xlsx'
xlsx = pd.ExcelFile(path)
df = pd.read_excel(xlsx, 'Sheet1')
# Excel列名
cols = ['hcpid','periodlevel','period','job']
df['is_duplicated'] = df.duplicated(cols)
df_dup = df.loc[df['is_duplicated'] == True]
# 乱码
# df_dup.to_csv('./dup.csv', encoding='utf-8')
df_dup.to_csv('./dup.csv', encoding='utf_8_sig')