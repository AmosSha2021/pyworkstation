import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import setp
import csv

# Ranging Error

# file_dir = "/Users/shaamos/PycharmProjects/pyworkstation/ACOND_Range.csv"
#
# df = pd.read_csv(file_dir)
#
# data_a = [
# df['tech=ARROW;ant=ant_1_1;rate=pkt_type_4;freq=8.0GHz;rx_mode=HL;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW;ant=ant_1_1;rate=pkt_type_4;freq=8.0GHz;rx_mode=LN;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW;ant=ant_1_2;rate=pkt_type_4;freq=8.0GHz;rx_mode=HL;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW;ant=ant_1_2;rate=pkt_type_4;freq=8.0GHz;rx_mode=LN;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW;ant=ant_2_1;rate=pkt_type_4;freq=8.0GHz;rx_mode=HL;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW;ant=ant_2_1;rate=pkt_type_4;freq=8.0GHz;rx_mode=LN;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW;ant=ant_2_2;rate=pkt_type_4;freq=6.5GHz;rx_mode=HL;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW;ant=ant_2_2;rate=pkt_type_4;freq=6.5GHz;rx_mode=LN;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW;ant=ant_2_2;rate=pkt_type_4;freq=8.0GHz;rx_mode=HL;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW;ant=ant_2_2;rate=pkt_type_4;freq=8.0GHz;rx_mode=LN;tc=Cond_Range;subtc=ToF_Avg']
# ]
#
# data_b = [ df['tech=ARROW_MMS;ant=ant_1_1;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW_MMS;ant=ant_1_1;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW_MMS;ant=ant_1_2;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW_MMS;ant=ant_1_2;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW_MMS;ant=ant_2_1;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW_MMS;ant=ant_2_1;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW_MMS;ant=ant_2_2;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=HL;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW_MMS;ant=ant_2_2;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=LN;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW_MMS;ant=ant_2_2;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'],
# df['tech=ARROW_MMS;ant=ant_2_2;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg']
# ]
#
#
# print(data_b)
#
# ticks = ['HL: ant_1_1','LN: ant_1_1','HL: ant_1_2','LN: ant_1_2','HL: ant_2_1','LN: ant_2_1','HL: ant_2_2(CH5)','LN: ant_2_2(CH5)','HL: ant_2_2(CH9)','LN: ant_2_2(CH9)']
#
# def set_box_color(bp, color):
#     plt.setp(bp['boxes'], color=color)
#     plt.setp(bp['whiskers'], color=color)
#     plt.setp(bp['caps'], color=color)
#     plt.setp(bp['medians'], color=color)
#
# plt.figure()
#
# bpa = plt.boxplot(data_a, positions=np.array(range(len(data_a)))*2.0-0.2, sym='', widths=0.3)
# bpb = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0+0.2, sym='', widths=0.3)
#
# set_box_color(bpa, '#3182bd') # colors are from http://colorbrewer2.org/
# set_box_color(bpb, '#D7191C') # colors are from http://colorbrewer2.org/
#
# # draw temporary red and blue lines and use them to create a legend
# plt.plot([], c='#3182bd', label='Legacy')
# plt.plot([], c='#D7191C', label='NBA_MMS')
# plt.legend()
#
# plt.xticks(range(0, len(ticks) * 2, 2), ticks)
# #plt.xlim(-2, len(ticks)*2)
# plt.ylim(0, 350)
# #plt.tight_layout()
# #plt.savefig('boxcompare.png')
# plt.grid(linestyle='dotted')
# plt.ylabel('ToF_Error: ps')
# plt.title('ToF Comparison')
# plt.legend(loc='upper left')
# plt.xticks(rotation=15)
# plt.show()

# Ranging Sigma

file_dir = "/Users/shaamos/PycharmProjects/pyworkstation/ACOND_Range.csv"

df = pd.read_csv(file_dir)

data_a = [
df['tech=ARROW;ant=ant_1_1;rate=pkt_type_4;freq=8.0GHz;rx_mode=HL;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW;ant=ant_1_1;rate=pkt_type_4;freq=8.0GHz;rx_mode=LN;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW;ant=ant_1_2;rate=pkt_type_4;freq=8.0GHz;rx_mode=HL;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW;ant=ant_1_2;rate=pkt_type_4;freq=8.0GHz;rx_mode=LN;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW;ant=ant_2_1;rate=pkt_type_4;freq=8.0GHz;rx_mode=HL;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW;ant=ant_2_1;rate=pkt_type_4;freq=8.0GHz;rx_mode=LN;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW;ant=ant_2_2;rate=pkt_type_4;freq=6.5GHz;rx_mode=HL;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW;ant=ant_2_2;rate=pkt_type_4;freq=6.5GHz;rx_mode=LN;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW;ant=ant_2_2;rate=pkt_type_4;freq=8.0GHz;rx_mode=HL;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW;ant=ant_2_2;rate=pkt_type_4;freq=8.0GHz;rx_mode=LN;tc=Cond_Range;subtc=ToF_Std']
]

data_b = [ df['tech=ARROW_MMS;ant=ant_1_1;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW_MMS;ant=ant_1_1;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW_MMS;ant=ant_1_2;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW_MMS;ant=ant_1_2;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW_MMS;ant=ant_2_1;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW_MMS;ant=ant_2_1;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW_MMS;ant=ant_2_2;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=HL;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW_MMS;ant=ant_2_2;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=LN;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW_MMS;ant=ant_2_2;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'],
df['tech=ARROW_MMS;ant=ant_2_2;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ANT_2_2;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std']
]


print(data_b)

ticks = ['HL: ant_1_1','LN: ant_1_1','HL: ant_1_2','LN: ant_1_2','HL: ant_2_1','LN: ant_2_1','HL: ant_2_2(CH5)','LN: ant_2_2(CH5)','HL: ant_2_2(CH9)','LN: ant_2_2(CH9)']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpa = plt.boxplot(data_a, positions=np.array(range(len(data_a)))*2.0-0.2, sym='', widths=0.3)
bpb = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0+0.2, sym='', widths=0.3)

set_box_color(bpa, '#3182bd') # colors are from http://colorbrewer2.org/
set_box_color(bpb, '#D7191C') # colors are from http://colorbrewer2.org/

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#3182bd', label='Legacy')
plt.plot([], c='#D7191C', label='NBA_MMS')
plt.legend()

plt.xticks(range(0, len(ticks) * 2, 2), ticks)
#plt.xlim(-2, len(ticks)*2)
plt.ylim(0, 350)
#plt.tight_layout()
#plt.savefig('boxcompare.png')
plt.grid(linestyle='dotted')
plt.ylabel('ToF_STD: ps')
plt.title('ToF Comparison')
plt.legend(loc='upper left')
plt.xticks(rotation=15)
plt.show()
