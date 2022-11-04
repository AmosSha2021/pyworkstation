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
    #ant = ["ant_0", "ant_1", "ant_2", "ant_3"]
    ant = ["ant_3"]
    print(file_path)
    for file in glob.glob(file_path):
        print(file)
        cols1 = pd.read_csv(file, skiprows=[0, 2, 3, 6]);
        cols1.columns
        productname = pd.Series(cols1['Product'])[3]
        for arg in argv:
            after_filter=cols1.filter(regex= arg)

        for i in after_filter.columns:
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
                                channel_antenna.append(f + 'GHz')
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
    df1 = df_data[df_data['Product'].isin(['D64'])]
    #df1 = df1[df1['Channel_Antenna'].isin(['8.0GHz_ant_0', '8.0GHz_ant_1', '8.0GHz_ant_3', '6.5GHz_ant_3'])]
    fig = plt.figure(1, figsize=(10, 7))
    tc = argv[0]
    plt.title("D64-K Pre Cal Max EIRP")
    bp = sns.boxplot(y=tc, x='Channel_Antenna',
                     data=df1,
                     palette="Set2",
                     hue='Product',width=0.5,showmeans=True,meanprops={"marker": "+",
                       "markeredgecolor": "Black",
                       "markersize": "10"})
    bp.set(xlabel='Frequency (GHz)', ylabel='EIRP(dBm)')
    #colors = ['#0000FF', '#00FF00',
     #         '#FFFF00']
    #for patch, color in zip(bp['boxes'], colors):
        #patch.set_facecolor(color)
    plt.grid()
    plt.tight_layout()
    fig.show(bp)
    plt.savefig('D64-K ANT3 CH5.png')