# import pandas as pd
# import sys
# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# import re
# import csv
# import glob
# from matplotlib import cbook
# import matplotlib.patheffects as path_effects
# from matplotlib.cbook import boxplot_stats
# def add_median_labels(ax, fmt='.1f'):
#     lines = ax.get_lines()
#     boxes = [c for c in ax.get_children() if type(c).__name__ == 'PathPatch']
#     lines_per_box = int(len(lines) / len(boxes))
#     for median in lines[4:len(lines):lines_per_box]:
#         x, y = (data.mean() for data in median.get_data())
#         # choose value depending on horizontal or vertical plot orientation
#         value = x if (median.get_xdata()[1] - median.get_xdata()[0]) == 0 else y
#         text = ax.text(x, y, f'{value:{fmt}}', ha='center', va='center',
#                        fontweight='bold', color='white')
#         # create median-colored border around white text for contrast
#         text.set_path_effects([
#             path_effects.Stroke(linewidth=3, foreground=median.get_color()),
#             path_effects.Normal(),
#         ])
# def ret_sub(m):
#     if m:
#         str = m.group(1)
#     else:
#         str = "NA"
#     return str
# def ret_eLNAState(m):
#     if (m == '1'):
#         str = "eLNA_Bypass"
#     else:
#         str = "eLNA_HG"
#     return str
# def plot_tc(dir,*argv):
#     print(len(argv))
#     print(argv[0])
#     print("************* Starting reading csvs %s *************")
#     ant = []
#     show_outliers_in_plot = False
#     intial_cond = 1
#     file_path = dir + "/*.csv"
#     X_axis_col = ['Antenna'];
#     Pkt_type = []
#     Products =[]
#     data = []
#     Rx_Mode = []
#     eLNA_State = []
#     dl_level = []
#     Fig_splitting_criteria = ["1","2"]
#     print(file_path)
#     for file in glob.glob(file_path):
#         print(file)
#         cols1 = pd.read_csv(file, skiprows=[0, 2, 3, 6]);
#         cols1.columns
#         for i in cols1.columns:
#             intial_cond = 1
#             for arg in argv:
#                 intial_cond = (i.find(arg) != -1) and intial_cond
#             if (intial_cond):
#                 for m in range(len(cols1[i])):
#                     reg = re.search('ant=(.+?):', i)
#                     antenna = ret_sub(reg)
#                     reg = re.search('eLNA=(.+?):', i)
#                     elna = ret_sub(reg)
#                     reg = re.search('rate=(.+?):', i)
#                     pkt = ret_sub(reg)
#                     reg = re.search('rx_mode=(.+?):', i)
#                     rxmode = ret_sub(reg)
#                     reg = re.search('dl=([1-9]{1,2})', i)
#                     dl = ret_sub(reg)
#                     ant.append(antenna)
#                     Rx_Mode.append(rxmode)
#                     eLNA_State.append(elna)
#                     data.append(pd.Series(cols1[i])[m])
#                     dl_level.append(dl)
#                     Pkt_type.append(pkt)
#                     productname = pd.Series(cols1['Product'])[m]
#                     Products.append(productname)
#     print(len(data))
#     df_data = pd.DataFrame(
#         {'Product': Products,Freq'Rx_Mode': Rx_Mode, 'eLNA_State': eLNA_State,'dl_level':dl_level,'Pkt':Pkt_type,argv[0]: data})
#     df_data = df_data.dropna()
#     #Data outlier removal
#     #This can be used in case outliers are to be removed based on percentile
#     # q_low = df_data["RxSens_Search"].quantile(0.01)
#     # q_hi = df_data["RxSens_Search"].quantile(0.99)
#     # df_data = df_data[(df_data["RxSens_Search"] < q_hi) & (df_data["RxSens_Search"] > q_low)]
#     fig_count = 1;
#     for div in Fig_splitting_criteria:
#         fig, ax = plt.subplots(fig_count)
#         tc = argv[0]
#         #sns.set_style("darkgrid")
#         df1 = df_data[df_data['eLNA_State'].isin([div])] #Filtering happens here based on fligure splitting criteria
#         df1[tc] = df1[tc].astype(float)
#         bp = sns.boxplot(y=tc, x='Product',
#                          data=df1,
#                          palette="Accent",
#                          hue='Rx_Mode', meanline=True, showmeans=True, showfliers=show_outliers_in_plot)
#         add_median_labels(bp)
#         title = ret_eLNAState(div)
#         plt.title(title)
#         bp.set(xlabel='Frequency (GHz)', ylabel='Sensitivity (dBm)')
#         plt.grid()
#         plt.tight_layout()
#         fig.show(bp)
#         plt.savefig(div)
# def Start(argv):
#     print(sys.argv[1])
#     string = str(sys.argv[1]) + "/*.csv"
#     print(string)
#     plot_tc(str(sys.argv[1]),'RSSI_Sweep', 'subtc=RxRSSI')
#     #plot_tc(str(sys.argv[1]), 'subtc=ToF_Avg', 'eLNA=2')