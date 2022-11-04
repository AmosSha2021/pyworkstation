import pandas as pd
import sys
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import re
import csv
import glob
def plot_tc(dir,outlier,*argv):
    print(len(argv))
    print(argv[0])
    print("************* Starting reading csvs %s *************")
    channel_antenna = []
    lower_limit = []
    upper_limit = []
    ll=0
    ul=0
    intial_cond = 1
    file_path = dir + "/*.csv"
    product_name = []
    data = []
    freq = ["6.25", "6.5","6.75"]
    ant = ["ant_3"]
    print(file_path)
    for file in glob.glob(file_path):
        print(file)
        cols1 = pd.read_csv(file, skiprows=[0, 2, 3, 6]);
        cols1.columns
        productname = pd.Series(cols1['Product'])[3]
        for i in cols1.columns:
            intial_cond = 1
            for arg in argv:
                intial_cond = (i.find(arg) != -1) and intial_cond
            if (intial_cond):
                for f in freq:
                    if (i.find(f) != -1):
                        for a in ant:
                            if (i.find(a) != -1):
                                for m in range(len(cols1[i])):
                                    if (m == 0):
                                        ll = pd.Series(cols1[i])[m]
                                        continue
                                    elif (m == 1):
                                        ul = pd.Series(cols1[i])[m]
                                        continue
                                    #if (pd.Series(cols1[i])[m] > outlier):
                                    data.append(pd.Series(cols1[i])[m])
                                    channel_antenna.append(f + '_' + a)
                                    product_name.append(productname)
                                    lower_limit.append(ll)
                                    upper_limit.append(ul)

    print(len(data))
    print(len(channel_antenna))
    print(len(product_name))
    print(len(lower_limit))
    print(len(upper_limit))
    df_data = pd.DataFrame(
        {'Product': product_name, 'Channel_Antenna': channel_antenna, argv[0]: data,'upper_limit': upper_limit,'lower_limit': lower_limit})
    filename = dir+argv[0]+'.csv'
    df_data.to_csv(filename)
    #df1 = df_data[df_data['Product'].isin(['D64 EVTM'])]
    df1 = df_data[df_data['Channel_Antenna'].isin(['6.25_ant_3', '6.5_ant_3', '6.75_ant_3'])]
    fig = plt.figure(1, figsize=(10, 7))
    tc = argv[0]
    plt.title(tc)
    bp = sns.boxplot(y=tc, x='Channel_Antenna',
                     data=df1,
                     palette="Accent",
                     hue='Product')
    plt.title("D64-ANT3 Pre Cal Tx Power")
    bp.set(xlabel='Frequency (GHz)', ylabel='Tx Power(dBm)')
    plt.grid()
    plt.tight_layout()
    fig.show(bp)

    plt.savefig('D64 SMT ANT3 CH5.png')
def plot_tc_ANT2(outlier,*argv):
    print(len(argv))
    print(argv[0])
    print("************* Starting reading csvs %s *************")
    file_loc = [
        '/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review/ACOND/Only_Pass/ANT2_CAL/D17_ANT2_Cal.csv',
        '/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review/ACOND/Only_Pass/ANT2_CAL/D63_ANT2_CAL.csv',
        '/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review/ACOND/Only_Pass/ANT2_CAL/D53P_PVTE_ANT2_CAL.csv',
        '/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review/ACOND/Only_Pass/ANT2_CAL/D53G_PVTE_ANT2_CAL.csv']

    booleans = []
    # for i in cols1.Special Build Description:
    #   if cols1.
    incl1 = []
    channel_antenna = []
    antenna = []
    intial_cond = 1
    product_name = []
    tx_power_cal = []
    rx_gain_cal = []
    freq = ["6.5GHz", "8.0GHz"]
    ant = ["ant_2"]
    # cols1.columns = [c.replace(' ', '_') for c in cols1.columns]
    # cols1[cols1['Special_Build_Description'].str.contains('2G17B')].to_csv('/Users/hindujaichapuram/Desktop/SOTA2/filtered.csv')
    # print(cols1.columns)
    incl1 = []
    for file in file_loc:
        cols1 = pd.read_csv(file, skiprows=[0, 2, 3, 4, 5, 6]);
        cols1.columns
        productname = pd.Series(cols1['Product'])[1]
        for i in cols1.columns:
            intial_cond = 1
            for arg in argv:
                intial_cond = (i.find(arg) != -1) and intial_cond
            if (intial_cond):
                for f in freq:
                    if (i.find(f) != -1):
                        for a in ant:
                            if (i.find(a) != -1):
                                for m in range(len(cols1[i])):
                                    if (pd.Series(cols1[i])[m] > outlier):
                                        tx_power_cal.append(pd.Series(cols1[i])[m])
                                        channel_antenna.append(f + '_' + a)
                                        product_name.append(productname)
    print(len(tx_power_cal))
    print(len(channel_antenna))
    print(len(product_name))
    df_txpower_cal = pd.DataFrame(
        {'Product': product_name, 'Channel_Antenna': channel_antenna, argv[0]: tx_power_cal})
    filename = '/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review /ACOND/Only_Pass/'+argv[0]+'_ANT2.csv'
    df_txpower_cal.to_csv(filename)
    df1 = df_txpower_cal[df_txpower_cal['Product'].isin(['D17', 'D53'])]
    #df1 = df1[df1['Channel_Antenna'].isin(['8.0GHz_ant_0', '8.0GHz_ant_1', '8.0GHz_ant_3', '6.5GHz_ant_3'])]
    tc = argv[0]

    fig = plt.figure(1, figsize=(10, 7))

    plt.title(tc)
    bp = sns.boxplot(y=tc, x='Channel_Antenna',
                     data=df1,
                     palette="colorblind",
                     hue='Product')

    fig.show(bp)

    df1 = df_txpower_cal[df_txpower_cal['Product'].isin(['D63', 'D53P'])]
    #df1 = df1[df1['Channel_Antenna'].isin(['8.0GHz_ant_0', '8.0GHz_ant_1', '8.0GHz_ant_3', '6.5GHz_ant_3'])]

    fig = plt.figure(2, figsize=(10, 7))
    plt.title(tc)
    bp = sns.boxplot(y = tc, x='Channel_Antenna',
                     data=df1,
                     palette="colorblind",
                     hue='Product')
    fig.show(bp)

    result = df_txpower_cal.groupby(['Product','Channel_Antenna']).agg({tc: ['mean', 'std']})
    print(result)
def Start(argv):
    print(sys.argv[1])
    string = str(sys.argv[1]) + "/*.csv"
    print(string)
    plot_tc(str(sys.argv[1]),-20,'TxPower_Test', 'subtc=rms', 'rate=pkt_type_1')
    #plot_tc(string,5,'TxPower_Cal')
    #plot_tc(string,-5,'RSSI_Error_40')
    # plot_tc(20,'_SNR')
    # plot_tc(0.5,'Mag_flatness')
    #plot_tc("/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review /ACOND/Only_Pass/Main_configs/*.csv",-50,'RSSI_Sweep','rate=pkt_type_1','dl=-45')
    #plot_tc_ANT2(5,'TxPower_Cal')
    #plot_tc_ANT2(-30,'RxGainCal_Coeff')
    #plot_tc("/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review /ACOND/Only_Pass/DOE_Vs_Main/*.csv",5,'TxPower_Cal')
    #plot_tc("/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review /ACOND/Only_Pass/DOE_Vs_Main/*.csv",-30, 'RxGainCal_Coeff')
