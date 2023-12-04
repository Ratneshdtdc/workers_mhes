# -*- coding: utf-8 -*-


import pandas as pd

def convert():
    df1 = pd.read_csv("D:/Project/workers_mhes/model_input/inb_dab.csv")
    df2 = pd.read_csv("D:/Project/workers_mhes/model_input/inb_dlb.csv")
    df3 = pd.read_csv("D:/Project/workers_mhes/model_input/inb_dsb.csv")
    df4 = pd.read_csv("D:/Project/workers_mhes/model_input/inb_mb.csv")
    df5 = pd.read_csv("D:/Project/workers_mhes/model_input/outb_dab.csv") 
    df6 = pd.read_csv("D:/Project/workers_mhes/model_input/outb_dlb.csv") 
    df7 = pd.read_csv("D:/Project/workers_mhes/model_input/outb_dsb.csv") 
    
    
    df1.drop(['Unnamed: 0'], axis=1, inplace=True)
    df2.drop(['Unnamed: 0'], axis=1, inplace=True)
    df3.drop(['Unnamed: 0'], axis=1, inplace=True)
    df4.drop(['Unnamed: 0'], axis=1, inplace=True)
    df5.drop(['Unnamed: 0'], axis=1, inplace=True)
    df6.drop(['Unnamed: 0'], axis=1, inplace=True)
    df7.drop(['Unnamed: 0'], axis=1, inplace=True)
    
    
    df1['sum'] = df1.sum(axis=1, numeric_only=True)
    df2['sum'] = df2.sum(axis=1, numeric_only=True)
    df3['sum'] = df3.sum(axis=1, numeric_only=True)
    df4['sum'] = df4.sum(axis=1, numeric_only=True)
    df5['sum'] = df5.sum(axis=1, numeric_only=True)
    df6['sum'] = df6.sum(axis=1, numeric_only=True)
    df7['sum'] = df7.sum(axis=1, numeric_only=True)
    
    for i in range(len(df1['sum'])):
        if df1['sum'][i] == 0:
            df1.loc[i, 'sum'] = 1
        if df2['sum'][i] == 0:
            df2.loc[i, 'sum'] = 1
        if df3['sum'][i] == 0:
            df3.loc[i, 'sum'] = 1
        if df4['sum'][i] == 0:
            df4.loc[i, 'sum'] = 1
        if df5['sum'][i] == 0:
            df5.loc[i, 'sum'] = 1
        if df6['sum'][i] == 0:
            df6.loc[i, 'sum'] = 1
        if df7['sum'][i] == 0:
            df7.loc[i, 'sum'] = 1
            

    inb_dab_per = df1.loc[:,"00:00":"23:59"].div(df1["sum"], axis=0)
    inb_dlb_per = df2.loc[:,"00:00":"23:59"].div(df2["sum"], axis=0)
    inb_dsb_per = df3.loc[:,"00:00":"23:59"].div(df3["sum"], axis=0)
    inb_mb_per = df4.loc[:,"00:00":"23:59"].div(df4["sum"], axis=0)
    outb_dab_per = df5.loc[:,"00:00":"23:59"].div(df5["sum"], axis=0)
    outb_dlb_per = df6.loc[:,"00:00":"23:59"].div(df6["sum"], axis=0)
    outb_dsb_per = df7.loc[:,"00:00":"23:59"].div(df7["sum"], axis=0)
    
    inb_dab_per['Hubs'] = df1['Hubs']
    inb_dlb_per['Hubs'] = df2['Hubs']
    inb_dsb_per['Hubs'] = df3['Hubs']
    inb_mb_per['Hubs'] = df4['Hubs']
    outb_dab_per['Hubs'] = df5['Hubs']
    outb_dlb_per['Hubs'] = df6['Hubs']
    outb_dsb_per['Hubs'] = df7['Hubs']
    
    inb_dab_per.set_index(['Hubs'], inplace=True)
    inb_dlb_per.set_index(['Hubs'], inplace=True)
    inb_dsb_per.set_index(['Hubs'], inplace=True)
    inb_mb_per.set_index(['Hubs'], inplace=True)
    outb_dab_per.set_index(['Hubs'], inplace=True)
    outb_dlb_per.set_index(['Hubs'], inplace=True)
    outb_dsb_per.set_index(['Hubs'], inplace=True)

    
    inb_dab_per.to_csv("model_input/inb_dab_per.csv")
    inb_dlb_per.to_csv("model_input/inb_dlb_per.csv")
    inb_dsb_per.to_csv("model_input/inb_dsb_per.csv")
    inb_mb_per.to_csv("model_input/inb_mb_per.csv")
    outb_dab_per.to_csv("model_input/outb_dab_per.csv")
    outb_dlb_per.to_csv("model_input/outb_dlb_per.csv")
    outb_dsb_per.to_csv("model_input/outb_dsb_per.csv")