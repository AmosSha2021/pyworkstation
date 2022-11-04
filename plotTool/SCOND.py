import pandas as pd
import sys
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import re
import csv
import glob
def plot_tc(dir,*argv):
    print(len(argv))
    print(argv[0])
    print("************* Starting the script to generate key for XL file %s *************")
    file_path = dir + "/*.csv"
    lower_limit = []
    upper_limit = []
    ll=0
    ul=0
    intial_cond = 1
    product_name = []
    tx_power_cal = []
    tech = ["STOCKHOLM", "FURY"]
    technology = []

    for file in glob.glob(file_path):
        cols1 = pd.read_csv(file, skiprows=[0, 2, 3, 6]);
        cols1.columns
        productname = pd.Series(cols1['Product'])[3]
        for i in cols1.columns:
            intial_cond = 1
            for arg in argv:
                intial_cond = (i.find(arg) != -1) and intial_cond
            if (intial_cond):
                for t in tech:
                    if (i.find(t) != -1):
                        for m in range(len(cols1[i])):
                        #print(pd.Series(cols1[i])[m])
                            if (m == 0):
                                ll = pd.Series(cols1[i])[m]
                                continue
                            elif (m == 1):
                                ul = pd.Series(cols1[i])[m]
                                continue
                            tx_power_cal.append(pd.Series(cols1[i])[m])
                            product_name.append(productname)
                            lower_limit.append(ll)
                            upper_limit.append(ul)
                            technology.append(t)

    print(len(tx_power_cal))
    print(len(product_name))
    print(len(lower_limit))
    print(len(upper_limit))
    df_txpower_cal = pd.DataFrame(
        {'Product': product_name, 'Technology': technology,argv[0]: tx_power_cal,'upper_limit': upper_limit,'lower_limit': lower_limit})
    print("the directory is")
    filename = dir+argv[0]+'.csv'
    df_txpower_cal.to_csv(filename)
    df1 = df_txpower_cal[df_txpower_cal['Product'].isin(['D17', 'D53'])]
    fig = plt.figure(1, figsize=(10, 7))
    tc = argv[0]
    plt.title(tc)
    bp = sns.boxplot(y=tc, x='Technology',
                     data=df1,
                     palette="colorblind",
                     hue='Product')
    fig.show(bp)
    df1 = df_txpower_cal[df_txpower_cal['Product'].isin(['D63', 'D53P'])]
    print((df_txpower_cal[df_txpower_cal['Product'].isin(['D63'])])['lower_limit'])
    fig = plt.figure(2, figsize=(10, 7))
    plt.title(tc)
    bp = sns.boxplot(y = tc, x='Technology',
                     data=df1,
                     palette="colorblind",
                     hue='Product')

    fig.show(bp)
def plot_CM(file_path,*argv):
    print(len(argv))
    print(argv[0])
    print("************* Starting the script to generate key for XL file %s *************")
    lower_limit = []
    upper_limit = []
    ll=0
    ul=0
    intial_cond = 1
    product_name = []
    data = []
    type_rate = []
    types = ["type=B","type=A","type=F"]
    rates = ["106kbps","212kbps","424kbps"]

    incl1 = []
    for file in glob.glob(file_path):
        cols1 = pd.read_csv(file, skiprows=[0, 2, 3, 6]);
        cols1.columns
        productname = pd.Series(cols1['Product'])[3]
        for i in cols1.columns:
            intial_cond = 1
            for arg in argv:
                intial_cond = (i.find(arg) != -1) and intial_cond
            if (intial_cond):
                for type in types:
                    if (i.find(type) != -1):
                        for rate in rates:
                            if (i.find(rate) != -1):
                                for m in range(len(cols1[i])):
                                #print(pd.Series(cols1[i])[m])
                                    if (m == 0):
                                        ll = pd.Series(cols1[i])[m]
                                        continue
                                    elif (m == 1):
                                        ul = pd.Series(cols1[i])[m]
                                        continue
                                    data.append(pd.Series(cols1[i])[m])
                                    product_name.append(productname)
                                    lower_limit.append(ll)
                                    upper_limit.append(ul)
                                    type_rate.append(type + '_' + rate)

    print(len(data))
    print(len(product_name))
    print(len(lower_limit))
    print(len(upper_limit))
    df_data = pd.DataFrame(
        {'Product': product_name, 'Type_Rate': type_rate,argv[0]: data,'upper_limit': upper_limit,'lower_limit': lower_limit})
    filename = dir+argv[0]+'.csv'
    df_data.to_csv(filename)
    df1 = df_data[df_data['Product'].isin(['D17', 'D53'])]
    plt.figure(1, figsize=(10, 7))
    tc = argv[0]
    plt.title(tc)
    bp = sns.boxplot(y=tc, x='Type_Rate',
                     data=df1,
                     palette="colorblind",
                     hue='Product')
    plt.plot([2,3,4])
    plt.show()
    df1 = df_data[df_data['Product'].isin(['D63', 'D53P'])]
    print((df_data[df_data['Product'].isin(['D63'])])['lower_limit'])
    fig = plt.figure(2, figsize=(10, 7))
    plt.title(tc)
    bp = sns.boxplot(y = tc, x='Type_Rate',
                     data=df1,
                     palette="colorblind",
                     hue='Product')

    fig.show(bp)
def Start(argv):

    # plot_tc("/Users/hindujaichapuram/Downloads/Data_Review/*.csv",'Resonance_frequency_CF')
    # plot_tc("/Users/hindujaichapuram/Downloads/Data_Review/*.csv", 'Field_Strength','RM_Unloaded')
    # plot_tc("/Users/hindujaichapuram/Downloads/Data_Review/*.csv", 'Curr_Val', 'Tx_Clock_Ext_Reader')
    #plot_tc("/Users/hindujaichapuram/Downloads/Data_Review/*.csv", 'VP2P_VRMS_AC ', 'Tx_Clock_Ext_Reader')
    plot_tc(str(sys.argv[1]),'Resonance_frequency_CF')
    plot_tc(str(sys.argv[1]), 'Field_Strength','RM_Unloaded')
    plot_tc(str(sys.argv[1]), 'Curr_Val', 'Tx_Clock_Ext_Reader')
    plot_tc(str(sys.argv[1]), 'VP2P_VRMS_AC ', 'Tx_Clock_Ext_Reader')
    #argv+"/*"
    #plot_CM(str,'Card_Mode:','ScopeMeas','subsubtc=Vp2p ')