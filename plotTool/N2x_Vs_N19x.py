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
        str = "LP"
    return str
def ret_eLNAState(m):
    if (m == '1'):
        str = "eLNA_Bypass"
    else:
        str = "eLNA_HG"
    return str
def plot_tc(dir,outlier,*argv):
    print(len(argv))
    print(argv[0])
    print("************* Starting reading csvs %s *************")
    Rx_Mode = []
    show_outliers_in_plot = False
    intial_cond = 1
    file_path = dir + "/*.csv"
    product_name = []
    data = []
    Freq_GHz = []
    pkt_type = []
    ant = []
    eLNA_State = []
    Fig_splitting_criteria = ["6.5GHz","8.0GHz"]
    group_by_param= 'Rx Mode'
    X_axis = 'Product'
    red_diamond = dict(markerfacecolor='b', marker='D')
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
                    reg = re.search('ant=(.+?):', i)
                    antenna = ret_sub(reg)
                    reg = re.search('eLNA=(.+?):', i)
                    elna = ret_sub(reg)
                    reg = re.search('freq=(.+?):', i)
                    freq = ret_sub(reg)
                    reg = re.search('rx_mode=([A-Z]{1,2})', i)
                    rxmode = ret_sub(reg)
                    reg = re.search('rate=(.+?):', i)
                    pkt = ret_sub(reg)
                    pkt_type.append(pkt)
                    ant.append(antenna)
                    eLNA_State.append(ret_eLNAState(elna))
                    productname = pd.Series(cols1['Product'])[m]
                    data.append(pd.Series(cols1[i])[m])
                    Rx_Mode.append(rxmode)
                    Freq_GHz.append(freq)
                    product_name.append(productname)

    print(len(data))
    print(len(Rx_Mode))
    print(len(product_name))
    df_data = pd.DataFrame(
        {'Product': product_name, 'Freq': Freq_GHz,'Rx Mode': Rx_Mode, 'eLNA_State':eLNA_State,'pkt_type':pkt_type,argv[0]: data})
    df_data = df_data.dropna()
    # q_low = df_data["RxSens_Search"].quantile(0.01)
    # q_hi = df_data["RxSens_Search"].quantile(0.99)
    df_data = df_data[(df_data["RxSens_Search"] < 0)]
    fig_count = 1;
    df_data = df_data[df_data['Product'].isin(['X2700S', 'X2538S'])]
    df_data.loc[df_data['Product'] == "X2700S", 'Chipset'] = 'R2'
    df_data.loc[df_data['Product'] == "X2538S", 'Chipset'] = 'R1'
    #df_data['x_axis'] = df_data['Product'] + "/"+df_data['Freq']  # Knob
    unique_values = df_data[X_axis].unique()
    # value = df_data["RxSens_Search"]
    # q_low = value.quantile(0.01)
    # q_hi = value.quantile(0.99)
    # df_data = df_data[(value < q_hi) & (value > q_low)]
    # for m in unique_values:
    #     value = df_data[df_data[X_axis].isin([m])][argv[0]]
    #     q_low = value.quantile(0.01)
    #     q_high = value.quantile(0.99)
    #     df_data2 = df_data.loc[(value < q_high) & (value > q_low)]
    for div in Fig_splitting_criteria:
        fig, ax = plt.subplots(fig_count)
        tc = argv[0]
        # sns.set_style("darkgrid")
        df1 = df_data[df_data['Freq'].isin([div])]

        df1[tc] = df1[tc].astype(float)
        bp = sns.boxplot(y=tc, x='Chipset',
                         data=df1,
                         palette="Accent",
                         hue='Rx Mode', meanline=True, showmeans=True, showfliers=show_outliers_in_plot)
        add_median_labels(bp)
        plt.title("ND Packet Sensitivity - "+div)
        bp.set(xlabel='Chipset', ylabel='Sensitivity (dBm)')
        plt.grid()
        #plt.tight_layout()
        fig.show(bp)
        plt.savefig(div + " Sensitivity " + argv[2] + ' Sensitivity.png')
def Start(argv):
    print(sys.argv[1])
    string = str(sys.argv[1]) + "/*.csv"
    print(string)
    plot_tc(str(sys.argv[1]),-20,'RxSens_Search', 'subtc=Sensitivity','pkt_type_4','eLNA=1')
    #plot_tc(str(sys.argv[1]), -20, 'RxSens_Search', 'subtc=Sensitivity','eLNA=2')