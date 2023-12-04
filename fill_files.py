# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import math
from preprocessing import code_break
import warnings
warnings.filterwarnings("ignore")

def fill_op_files():
    
    inb_mb = pd.read_csv("D:/Project/workers_mhes/output/inb_mb.csv")
    
    #for i in range(1,23):

    #file_name = "D:/Project/workers_mhes/input/"+ str(i)+ ".csv"
    
    file_name = "D:/Project/workers_mhes/input/Fullmday.csv"
    df1 = pd.read_csv(file_name, encoding='cp1252')
    df1 = df1.iloc[1:,:]
    df1 = code_break(df1)
    
    rbc_sur = pd.read_csv("D:/Project/workers_mhes/input/Branch_hub_surface.csv")
    rbc_air_inb = pd.read_csv("D:/Project/workers_mhes/input/Branch_hub_air_inb.csv")
    rbc_air_outb = pd.read_csv("D:/Project/workers_mhes/input/Branch_hub_air_outb.csv")
    
    
    
    ########### INB_MB file filling ###################
    ###################################################
    print("Filling for Mixed Bags from", file_name,"...")
    failed = []
    df1["Unnamed: 77"] = df1["Unnamed: 77"].astype(str)
    df1["Unnamed: 23"] = df1["Unnamed: 23"].astype(str)
    for i in inb_mb['Hubs']:
        print("Filling of ", i, "Hub Started")
        df_target = df1[df1['BAG DEST CODE'] == i]
        
        #df_target.to_csv("trash/shbcuaesbfhw.csv")
        
        times = []
        df_target.reset_index(inplace=True)
        
        rbc1 = list()
        try:
            rbc_temp = list(rbc_sur[i].values)
            rbc1.extend(rbc_temp)
            rbc_temp = list(rbc_air_inb[i].values)
            rbc1.extend(rbc_temp)
        except:
            try:
                rbc_temp = list(rbc_air_inb[i].values)
                rbc1.extend(rbc_temp)
            except:
                rbc_temp = list(rbc_sur[i].values)
                rbc1.extend(rbc_temp)
            
            
        #rbc2 = list(rbc_air_inb[i].values)
        #rbc1 = list(rbc_sur[i].values)
        #rbc2 = list(rbc_air_inb[i].values)
        #rbc1.extend(rbc2)
        #print(rbc1)
# =============================================================================
#         count1=0
#         count2 =0
#         count3=0
#         count4=0
#         count5=0
#         count7=0
# =============================================================================
        for k in range(len(df_target["Unnamed: 77"])):
            ### 77 not null and 23 null
            if df_target["Unnamed: 77"][k].lower() != 'nan':
                if df_target["Unnamed: 23"][k].lower() == 'nan':
                    if df_target["BAG ORIGIN CODE"][k] in rbc1:
                        times.append(df_target["Unnamed: 77"][k])
                    else:
                        times.append(df_target["Unnamed: 77"][k])
                        #count1 = count1+1
            
            ### 77 null and 23 not null
            if df_target["Unnamed: 77"][k].lower() == 'nan':
                if df_target["Unnamed: 23"][k].lower() != 'nan':
                    if df_target["BAG ORIGIN CODE"][k] in rbc1:
                        times.append(df_target["Unnamed: 23"][k])
                        #count2 = count2+1
        
            ### 77 not null and not 23 null
            if df_target["Unnamed: 77"][k].lower() != 'nan':
                if df_target["Unnamed: 23"][k].lower() != 'nan':
                    if df_target["Unnamed: 23"][k] == df_target["Unnamed: 77"][k]:
                        times.append(df_target["Unnamed: 77"][k])
                        #count3 = count3+1
                    else:
                        ### BAG ORIGIN CODE is rbc
                        if df_target["BAG ORIGIN CODE"][k] in rbc1:
                            times.append(df_target["Unnamed: 23"][k])
                            
                        else:
                            times.append(df_target["Unnamed: 77"][k])
                            #count4 = count4+1

        
        index = inb_mb[inb_mb['Hubs'] == str(i)].index.tolist()[0]
        for t in times:
            try:
                # index = inb_mb[inb_mb['Hubs'] == str(i)].index.tolist()[0]
                #index = inb_mb.index[inb_mb['Hubs'] == str(i)].tolist()
                value = inb_mb.loc[index,t]
                inb_mb.loc[index, t] = value+1
                #inb_mb.at[index,t] = inb_mb.at[index,t] + 1
            except:
                failed.append(t)
        

 
    inb_mb.to_csv("model_input/inb_mb.csv")
    print("--" *10)
    ####################################################
    ########### DAB files filling ###################
    inb_dab = pd.read_csv("D:/Project/workers_mhes/output/inb_dab.csv")
    outb_dab = pd.read_csv("D:/Project/workers_mhes/output/outb_dab.csv")
    print("Filling for Direct Air Bags from", file_name,"...")
    failed = []
    df1["Unnamed: 23"] = df1["Unnamed: 23"].astype(str)
    df1["Unnamed: 41"] = df1["Unnamed: 41"].astype(str)
    df1["Unnamed: 59"] = df1["Unnamed: 59"].astype(str)
    df1["Unnamed: 77"] = df1["Unnamed: 77"].astype(str)
    df1["Unnamed: 28"] = df1["Unnamed: 28"].astype(str)
    df1["Unnamed: 46"] = df1["Unnamed: 46"].astype(str)
    df1["Unnamed: 64"] = df1["Unnamed: 64"].astype(str)
    
    for i in inb_dab['Hubs']:
        print("Filling of ", i, "Hub Started")
        # Condition 1: dest_code != i
        df_target = df1[df1['BAG DEST CODE'] != i]
        # condition 2
        df_target = df_target[(df_target['Unnamed: 3']== "AIR") |(df_target['Unnamed: 3']== "AIR CARGO") ]
        # condition 3
        df_target = df_target.loc[(df_target["OH CD ORIGIN CODE"] ==i)|(df_target["T1 CD ORIGIN CODE"] ==i)|(df_target["T2 CD ORIGIN CODE"] ==i) ]

        df_target.reset_index(inplace=True)
        
        times_inb = []
        times_outb = []
        
        
        for ts in range(len(df_target["Unnamed: 23"])):
            # INB                   #Outb
            # X: Unnamed: 23        # AC: Unnamed: 28
            # AP:Unnamed: 41        # AU: Unnamed: 46
            # BH:Unnamed: 59        # BM: Unnamed: 64
            
            ####### inb ###############
            if df_target['OH CD ORIGIN CODE'][ts] == i:
                if df_target["Unnamed: 23"][ts].lower() != 'nan':
                    times_inb.append(df_target["Unnamed: 23"][ts])
                    times_outb.append(df_target["Unnamed: 28"][ts])
            if df_target['T1 CD ORIGIN CODE'][ts] == i:
                if df_target["Unnamed: 41"][ts].lower() != 'nan':
                    times_inb.append(df_target["Unnamed: 41"][ts]) 
                    times_outb.append(df_target["Unnamed: 46"][ts])
            if df_target['T2 CD ORIGIN CODE'][ts] == i:
                if df_target["Unnamed: 59"][ts].lower() != 'nan':
                    times_inb.append(df_target["Unnamed: 59"][ts]) 
                    times_outb.append(df_target["Unnamed: 64"][ts])
            #if df_target["Unnamed: 77"][ts].lower() != 'nan':
                #times_inb.append(df_target["Unnamed: 77"][ts]) 
                
        #print(len(times_inb))
        index = inb_dab[inb_dab['Hubs'] == str(i)].index.tolist()[0]
        for t in times_inb:
            try:
                # index = inb_mb[inb_mb['Hubs'] == str(i)].index.tolist()[0]
                #index = inb_mb.index[inb_mb['Hubs'] == str(i)].tolist()
                value = inb_dab.loc[index,t]
                inb_dab.loc[index, t] = value+1
                #inb_mb.at[index,t] = inb_mb.at[index,t] + 1
            except:
                failed.append(t) 
                         
        #print(len(times_outb))
        index = outb_dab[outb_dab['Hubs'] == str(i)].index.tolist()[0]
        for t in times_outb:
            try:
                # index = inb_mb[inb_mb['Hubs'] == str(i)].index.tolist()[0]
                #index = inb_mb.index[inb_mb['Hubs'] == str(i)].tolist()
                value = outb_dab.loc[index,t]
                outb_dab.loc[index, t] = value+1
                #inb_mb.at[index,t] = inb_mb.at[index,t] + 1
            except:
                failed.append(t)  
                
                
        
     
    inb_dab.to_csv("model_input/inb_dab.csv")
    outb_dab.to_csv("model_input/outb_dab.csv")
    print("--" *10)


    ####################################################
    ########### DSB files filling ###################
    inb_dsb = pd.read_csv("D:/Project/workers_mhes/output/inb_dsb.csv")
    outb_dsb = pd.read_csv("D:/Project/workers_mhes/output/outb_dsb.csv")
    inb_dlb = pd.read_csv("D:/Project/workers_mhes/output/inb_dlb.csv")
    outb_dlb = pd.read_csv("D:/Project/workers_mhes/output/outb_dlb.csv")
    print("Filling for Direct Surface Bags from", file_name,"...")
    failed = []
    
    
    #rbc_sur 
    #rbc_air_inb 
    #rbc_air_outb
    rbc_sur = pd.read_csv("D:/Project/workers_mhes/input/Branch_hub_surface.csv")


    times_local_in = []
    times_local_out = []
    # INB                   #Outb
    # X: Unnamed: 23        # AC: Unnamed: 28
    # AP:Unnamed: 41        # AU: Unnamed: 46
    # BH:Unnamed: 59        # BM: Unnamed: 64
    
    for i in inb_dsb['Hubs']:
        rbc1 = list()
        for c in range(len(rbc_sur[i])):
            #if rbc_sur[i][c].lower() != 'nan':
            rbc1.append(rbc_sur[i][c])

        
        print("Filling of ", i, "Hub Started")
        # Condition 1: dest_code != i
        df_target = df1[df1['BAG DEST CODE'] != i]
        # condition 2
        df_target = df_target[(df_target['Unnamed: 3']== "SURFACE")|(df_target['Unnamed: 3']== "TRAIN") ]
        # condition 3
        df_target = df_target.loc[(df_target["OH CD ORIGIN CODE"] ==i)|(df_target["T1 CD ORIGIN CODE"] ==i)|(df_target["T2 CD ORIGIN CODE"] ==i) ]
        
        df_target.reset_index(inplace=True)
        #print(df_target.shape)
        times_sur_in = []
        times_sur_out = []
        
        for ts in range(len(df_target['BAG DEST CODE'])):
            # condition 4
            if df_target['BAG DEST CODE'][ts] not in rbc1:
                if df_target['OH CD ORIGIN CODE'][ts] == i:
                    if df_target["Unnamed: 23"][ts].lower() != 'nan':
                        times_sur_in.append(df_target["Unnamed: 23"][ts])
                        times_sur_out.append(df_target["Unnamed: 28"][ts])
                if df_target['T1 CD ORIGIN CODE'][ts] == i:
                    if df_target["Unnamed: 41"][ts].lower() != 'nan':
                        times_sur_in.append(df_target["Unnamed: 41"][ts]) 
                        times_sur_out.append(df_target["Unnamed: 46"][ts])
                if df_target['T2 CD ORIGIN CODE'][ts] == i:
                    if df_target["Unnamed: 59"][ts].lower() != 'nan':
                        times_sur_in.append(df_target["Unnamed: 59"][ts]) 
                        times_sur_out.append(df_target["Unnamed: 64"][ts])
            
        index = inb_dsb[inb_dsb['Hubs'] == str(i)].index.tolist()[0]
        for t in times_sur_in:
             try:
                 # index = inb_mb[inb_mb['Hubs'] == str(i)].index.tolist()[0]
                 #index = inb_mb.index[inb_mb['Hubs'] == str(i)].tolist()
                 value = inb_dsb.loc[index,t]
                 inb_dsb.loc[index, t] = value+1
                 #inb_mb.at[index,t] = inb_mb.at[index,t] + 1
             except:
                 failed.append(t)  
                 
        for t in times_sur_out:
             try:
                 # index = inb_mb[inb_mb['Hubs'] == str(i)].index.tolist()[0]
                 #index = inb_mb.index[inb_mb['Hubs'] == str(i)].tolist()
                 value = outb_dsb.loc[index,t]
                 outb_dsb.loc[index, t] = value+1
                 #inb_mb.at[index,t] = inb_mb.at[index,t] + 1
             except:
                 failed.append(t) 
                 
    inb_dsb.to_csv("model_input/inb_dsb.csv")
    outb_dsb.to_csv("model_input/outb_dsb.csv")
    print("--" *10)
    
    ####################################################
    ########### DLB files filling ###################
    
    inb_dlb = pd.read_csv("D:/Project/workers_mhes/output/inb_dlb.csv")
    outb_dlb = pd.read_csv("D:/Project/workers_mhes/output/outb_dlb.csv")
    print("Filling for Direct Local Bags from", file_name,"...")
    failed = []
    
    
    #rbc_sur 
    #rbc_air_inb 
    #rbc_air_outb
    rbc_sur = pd.read_csv("D:/Project/workers_mhes/input/Branch_hub_surface.csv")


    times_local_in = []
    times_local_out = []
    # INB                   #Outb
    # X: Unnamed: 23        # AC: Unnamed: 28
    # AP:Unnamed: 41        # AU: Unnamed: 46
    # BH:Unnamed: 59        # BM: Unnamed: 64
    
    for i in inb_dlb['Hubs']:
        rbc1 = list()
        for c in range(len(rbc_sur[i])):
            #if rbc_sur[i][c].lower() != 'nan':
            rbc1.append(rbc_sur[i][c])

        
        print("Filling of ", i, "Hub Started")
        # Condition 1: dest_code != i
        df_target = df1[df1['BAG DEST CODE'] != i]
        # condition 2
        df_target = df_target[(df_target['Unnamed: 3']== "SURFACE")|(df_target['Unnamed: 3']== "TRAIN") ]
        # condition 3
        df_target = df_target.loc[(df_target["OH CD ORIGIN CODE"] ==i)|(df_target["T1 CD ORIGIN CODE"] ==i)|(df_target["T2 CD ORIGIN CODE"] ==i) ]
        
        df_target.reset_index(inplace=True)
        #print(df_target.shape)
        times_sur_in = []
        times_sur_out = []
        
        for ts in range(len(df_target['BAG DEST CODE'])):
            # condition 4
            if df_target['BAG DEST CODE'][ts] in rbc1:
                if df_target['OH CD ORIGIN CODE'][ts] == i:
                    if df_target["Unnamed: 23"][ts].lower() != 'nan':
                        times_sur_in.append(df_target["Unnamed: 23"][ts])
                        times_sur_out.append(df_target["Unnamed: 28"][ts])
                if df_target['T1 CD ORIGIN CODE'][ts] == i:
                    if df_target["Unnamed: 41"][ts].lower() != 'nan':
                        times_sur_in.append(df_target["Unnamed: 41"][ts]) 
                        times_sur_out.append(df_target["Unnamed: 46"][ts])
                if df_target['T2 CD ORIGIN CODE'][ts] == i:
                    if df_target["Unnamed: 59"][ts].lower() != 'nan':
                        times_sur_in.append(df_target["Unnamed: 59"][ts]) 
                        times_sur_out.append(df_target["Unnamed: 64"][ts])
            
        index = inb_dlb[inb_dlb['Hubs'] == str(i)].index.tolist()[0]
        for t in times_sur_in:
             try:
                 # index = inb_mb[inb_mb['Hubs'] == str(i)].index.tolist()[0]
                 #index = inb_mb.index[inb_mb['Hubs'] == str(i)].tolist()
                 value = inb_dlb.loc[index,t]
                 inb_dlb.loc[index, t] = value+1
                 #inb_mb.at[index,t] = inb_mb.at[index,t] + 1
             except:
                 failed.append(t)  
                 
        for t in times_sur_out:
             try:
                 # index = inb_mb[inb_mb['Hubs'] == str(i)].index.tolist()[0]
                 #index = inb_mb.index[inb_mb['Hubs'] == str(i)].tolist()
                 value = outb_dlb.loc[index,t]
                 outb_dlb.loc[index, t] = value+1
                 #inb_mb.at[index,t] = inb_mb.at[index,t] + 1
             except:
                 failed.append(t) 
                 
    inb_dlb.to_csv("model_input/inb_dlb.csv")
    outb_dlb.to_csv("model_input/outb_dlb.csv")
    print("--" *10)
    
    print("= "*10)
        

    
