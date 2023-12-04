# -*- coding: utf-8 -*-

import pandas as pd

def create_files():
    columns = ["Hubs"]

    
    for i  in range(24):
        for j in range(60):
            if i<10 and j<10:
                columns.append("0"+ str(i)+":0"+ str(j))
            elif i<10 and j>=10:
                columns.append("0"+ str(i)+":"+ str(j))
            elif i>=10 and j<10:
                columns.append( str(i)+":0"+ str(j))
            else:
                columns.append(str(i)+":"+ str(j))
    
    
    ####### INB: MIXED BAG ##################################
    inb_mb = pd.DataFrame(columns = columns)
    hub_codes = pd.read_csv("D:/Project/workers_mhes/hub_codes.csv")
    hub_codes.dropna(inplace=True)
    
    inb_mb['Hubs'] = hub_codes['BRANCH CODE']
    
    inb_mb.fillna(0, inplace=True)
    inb_mb.to_csv("output/inb_mb.csv", index=False)
    #####################################################
    
    ####### INB: DAB ##############################
    inb_dab = pd.DataFrame(columns = columns)
    inb_dab['Hubs'] = hub_codes['BRANCH CODE']
    
    inb_dab.fillna(0, inplace=True)
    inb_dab.to_csv("output/inb_dab.csv", index=False)
    ######################################################
    
    
    ####### INB: DSB ##############################
    inb_dsb = pd.DataFrame(columns = columns)
    inb_dsb['Hubs'] = hub_codes['BRANCH CODE']
    
    inb_dsb.fillna(0, inplace=True)
    inb_dsb.to_csv("output/inb_dsb.csv", index=False)
    ######################################################
    
    ####### INB: DLB ##############################
    inb_dlb = pd.DataFrame(columns = columns)
    inb_dlb['Hubs'] = hub_codes['BRANCH CODE']
    
    inb_dlb.fillna(0, inplace=True)
    inb_dlb.to_csv("output/inb_dlb.csv", index=False)
    ######################################################
    
    ####### OUTB: DAB ##############################
    outb_dab = pd.DataFrame(columns = columns)
    outb_dab['Hubs'] = hub_codes['BRANCH CODE']
    
    outb_dab.fillna(0, inplace=True)
    outb_dab.to_csv("output/outb_dab.csv", index=False)
    ######################################################
    
    
    ####### OUTB: DSB ##############################
    outb_dsb = pd.DataFrame(columns = columns)
    outb_dsb['Hubs'] = hub_codes['BRANCH CODE']
    
    outb_dsb.fillna(0, inplace=True)
    outb_dsb.to_csv("output/outb_dsb.csv", index=False)
    ######################################################
    
    ####### OUTB: DLB ##############################
    outb_dlb = pd.DataFrame(columns = columns)
    outb_dlb['Hubs'] = hub_codes['BRANCH CODE']
    
    outb_dlb.fillna(0, inplace=True)
    outb_dlb.to_csv("output/outb_dlb.csv", index=False)
    ######################################################