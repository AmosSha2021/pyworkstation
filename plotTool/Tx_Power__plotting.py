import pandas as pd
import sys
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import re
import csv
import glob
from matplotlib import cbook
import matplotlib.patheffects as path_effects
from matplotlib.cbook import boxplot_stats
def add_median_labels(ax, fmt='.1f'):
    lines = ax.get_lines()
    boxes = [c for c in ax.get_children() if type(c).__name__ == 'PathPatch']
    lines_per_box = int(len(lines) / len(boxes))
    for median in lines[4:len(lines):lines_per_box]:
        x, y = (data.mean() for data in median.get_data())
        # choose value depending on horizontal or vertical plot orientation
        value = x if (median.get_xdata()[1] - median.get_xdata()[0]) == 0 else y
        text = ax.text(x, y, f'{value:{fmt}}', ha='center', va='center',
                       fontweight='bold', color='white')
        # create median-colored border around white text for contrast
        text.set_path_effects([
            path_effects.Stroke(linewidth=3, foreground=median.get_color()),
            path_effects.Normal(),
        ])
def ret_sub(m):
    if m:
        str = m.group(1)
    else:
        str = "NA"
    return str
def ret_eLNAState(m):
    if (m == '1'):
        str = "eLNA_Bypass"
    else:
        str = "eLNA_HG"
    return str
def plot_tc(dir,*argv):
    print(len(argv))
    print(argv[0])
    print("************* Starting reading csvs %s *************")
    ant = []
    show_outliers_in_plot = False
    intial_cond = 1
    file_path = dir + "/*.csv"
    X_axis_col = ['Antenna'];
    Pkt_type = []
    Products =[]
    data = []
    Freq_GHz = []
    Rx_Mode = []
    eLNA_State = []
    Fig_splitting_criteria = ["6.500","8.000"]
    print(file_path)
    for file in glob.glob(file_path):
        print(file)
        cols1 = pd.read_csv(file, skiprows=[0, 2, 3, 6]);
        cols1.columns
        for i in cols1.columns:
            intial_cond = 1
            for arg in argv:
                intial_cond = (i.find(arg) != -1) and intial_cond
            if (intial_cond):
                for m in range(len(cols1[i])):
                    productname = pd.Series(cols1['Product'])[m]
                    reg = re.search('ant=(.+?):', i)
                    if(not reg):
                        reg = re.search('ant=(.+?);', i)
                    antenna = ret_sub(reg)
                    reg = re.search('freq=(.+?)GHz', i)
                    freq = ret_sub(reg)
                    ant.append(antenna)
                    Freq_GHz.append(freq)
                    data.append(pd.Series(cols1[i])[m])
                    Products.append(productname)
    print(len(data))
    df_data = pd.DataFrame(
        {'Product': Products, 'Antenna': ant,'Freq': Freq_GHz,argv[0]: data})
    df_data = df_data.dropna()
    df_data = df_data[df_data['Antenna'].isin(["ant_0", "ant_2"])]
    #Data outlier removal
    #This can be used in case outliers are to be removed based on percentile
    # q_low = df_data["RxSens_Search"].quantile(0.01)
    # q_hi = df_data["RxSens_Search"].quantile(0.99)
    # df_data = df_data[(df_data["RxSens_Search"] < q_hi) & (df_data["RxSens_Search"] > q_low)]
    fig_count = 1;
    for div in Fig_splitting_criteria:
        fig, ax = plt.subplots(fig_count)
        tc = argv[0]
        #sns.set_style("darkgrid")
        df1 = df_data[df_data['Freq'].isin([div])] #Filtering happens here based on fligure splitting criteria
        df1[tc] = df1[tc].astype(float)
        bp = sns.boxplot(y=tc, x='Product',
                         data=df1,
                         palette="Accent",
                         hue='Antenna', meanline=True, showmeans=True, showfliers=show_outliers_in_plot)
        add_median_labels(bp)
        plt.title(div+"Tx Power")
        bp.set(xlabel='Product', ylabel='TxPower Cal')
        plt.grid()
        plt.tight_layout()
        fig.show(bp)
        plt.savefig(div+"_Tx.png")
def Start(argv):
    print(sys.argv[1])
    string = str(sys.argv[1]) + "/*.csv"
    print(string)
    plot_tc(str(sys.argv[1]),'TxPower_CW_PreCal','subtc=rms')
    #plot_tc(str(sys.argv[1]), 'subtc=ToF_Avg', 'eLNA=2')