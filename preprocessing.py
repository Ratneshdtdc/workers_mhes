# -*- coding: utf-8 -*-

import pandas as pd

def code_break(df):
    
    
    df['BAG ORIGIN CODE'] = pd.Series(df['Unnamed: 1'].str.extract('.*\((.*)\).*')[0])
    df['BAG DEST CODE'] = pd.Series(df['Unnamed: 2'].str.extract('.*\((.*)\).*')[0])
    df['BR ORIGIN CODE'] = pd.Series(df['BRANCH DETAILS'].str.extract('.*\((.*)\).*')[0])
    df['BR DEST CODE'] = pd.Series(df['Unnamed: 8'].str.extract('.*\((.*)\).*')[0])
    df['OH CD ORIGIN CODE'] = pd.Series(df['ORG HUB DETAILS'].str.extract('.*\((.*)\).*')[0])
    df['OH CD DEST CODE'] = pd.Series(df['Unnamed: 21'].str.extract('.*\((.*)\).*')[0])
    df['T1 CD ORIGIN CODE'] = pd.Series(df['VIA HUB DETAILS'].str.extract('.*\((.*)\).*')[0])
    df['T1 CD DEST CODE'] = pd.Series(df['Unnamed: 39'].str.extract('.*\((.*)\).*')[0])
    df['T2 CD ORIGIN CODE'] = pd.Series(df['VIA2 HUB DETAILS'].str.extract('.*\((.*)\).*')[0]) 
    df['T2 CD DEST CODE'] = pd.Series(df['Unnamed: 57'].str.extract('.*\((.*)\).*')[0])
    #df['DH CD ORIGIN CODE'] = pd.Series(df['DEST HUB DETAILS'].str.extract('.*\((.*)\).*')[0]) 
    #df['DH CD DEST CODE'] = pd.Series(df['Unnamed: 75'].str.extract('.*\((.*)\).*')[0])
    
    #print("cnskjfcbhisenbfisk")
# =============================================================================
#     df['BAG ORIGIN CODE'] = df['Unnamed: 1'].str[-4:-1]  
#     df['BAG DEST CODE'] = df['Unnamed: 2'].str[-4:-1]  
#     df['BR ORIGIN CODE'] = df['BRANCH DETAILS'].str[-4:-1]  
#     df['BR DEST CODE'] = df['Unnamed: 8'].str[-4:-1]
#     df['OH CD ORIGIN CODE'] = df['ORG HUB DETAILS'].str[-4:-1]  
#     df['OH CD DEST CODE'] = df['Unnamed: 21'].str[-4:-1] 
#     df['T1 CD ORIGIN CODE'] = df['VIA HUB DETAILS'].str[-4:-1]  
#     df['T1 CD DEST CODE'] = df['Unnamed: 39'].str[-4:-1] 
#     df['T2 CD ORIGIN CODE'] = df['VIA2 HUB DETAILS'].str[-4:-1]  
#     df['T2 CD DEST CODE'] = df['Unnamed: 57'].str[-4:-1] 
#     df['DH CD ORIGIN CODE'] = df['DEST HUB DETAILS'].str[-4:-1]  
#     df['DH CD DEST CODE'] = df['Unnamed: 75'].str[-4:-1] 
# =============================================================================
    
    return df
   
    
