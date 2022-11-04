import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import setp
import csv
import os
import sys

x_path = os.getcwd()
print(x_path)
x = 1
# Ranging Error

# file_dir = 'csv_file_path'
##
# file_dir = input('Pls input CSV Path:')
# print(file_dir)
# df = pd.read_csv(file_dir,header=1,skiprows=lambda x:x>5)
def Range_AVG():
    data_a = [
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=HL;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=HL;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=HL;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=HL;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna()
    ]

    data_b = [
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LN;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LN;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LN;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LN;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna()
    ]
    data_c = [
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LP;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LP;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LP;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LP;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna()
    ]

    ticks = ['eLNA=1:ant0 CH5','eLNA=2:ant0 CH5','eLNA=1:ant0 CH9','eLNA=2:ant0 CH9']
    def set_box_color(bp, color):
        plt.setp(bp['boxes'], color=color)
        plt.setp(bp['whiskers'], color=color)
        plt.setp(bp['caps'], color=color)
        plt.setp(bp['medians'], color=color)
    plt.figure()
    bpa = plt.boxplot(data_a, positions=np.array(range(len(data_a)))*2.0-0.2, sym='', widths=0.3)
    bpb = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0+0.2, sym='', widths=0.3)
    bpc = plt.boxplot(data_c, positions=np.array(range(len(data_c)))*2.0+0.6, sym='', widths=0.3)

    set_box_color(bpa, '#3182bd') # colors are from http://colorbrewer2.org/
    set_box_color(bpb, '#D7191C') # colors are from http://colorbrewer2.org/
    set_box_color(bpc, '#28E6E3') # colors are from http://colorbrewer2.org/
    # draw temporary red and blue lines and use them to create a legend
    # plt.plot([], c='#3182bd', label='Legacy')
    # plt.plot([], c='#D7191C', label='NBA_MMS')
    plt.plot([], c='#3182bd', label='Rx_mode HL')
    plt.plot([], c='#D7191C', label='Rx_mode LN')
    plt.plot([], c='#28E6E3', label='Rx_mode LP')

    plt.legend()

    plt.xticks(range(0, len(ticks) * 2, 2), ticks)
    plt.grid(linestyle='dotted')
    plt.ylabel('ToF_Avg: ps')
    plt.title('ToF Comparison')
    plt.legend(loc='best')
    plt.xticks(rotation=15)
    plt.savefig('%s/ToF_Comparison_AVG.png'%x_path)

def Range_AVG_R():
    data_a = [
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=HL;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=HL;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LN;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LN;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LP;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LP;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=HL;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=HL;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LN;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LN;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LP;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LP;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Avg'].dropna()
    ]

    data_b = [
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=HL;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=HL;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=LN;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=LN;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=LP;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=LP;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),

        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LP;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Avg'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LP;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Avg'].dropna()


    ]

    print(data_a)
    # ticks = ['eLNA=1:ant0 CH5','eLNA=2:ant0 CH5','eLNA=1:ant0 CH9','eLNA=2:ant0 CH9']
    ticks = ['HL:eLNA=1 CH5','HL:eLNA=2 CH5','LN::eLNA=1 CH5','LN:eLNA=2 CH5','LP:eLNA=1 CH5','LP:eLNA=2 CH5',
             'HL:eLNA=1 CH9','HL:eLNA=2 CH9','LN:eLNA=1 CH9','LN:eLNA=2 CH9','LP:eLNA=1 CH9','LP:eLNA=2 CH9']

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

    plt.plot([], c='#3182bd', label='Legacy')
    plt.plot([], c='#D7191C', label='NBA_MMS')

    plt.legend()

    plt.xticks(range(0, len(ticks) * 2, 2), ticks)
    plt.grid(linestyle='dotted')
    plt.ylabel('ToF_Avg: ps')
    plt.title('ToF Comparison')
    plt.legend(loc='upper left')
    plt.xticks(rotation=15)
    plt.savefig('%s/ToF_Comparison_Avg_R.png'%x_path)

def Range_STD_R():

    data_a = [
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=HL;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=HL;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LN;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LN;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LP;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LP;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),

        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=HL;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=HL;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LN;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LN;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LP;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LP;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna()
    ]

    data_b = [
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=HL;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=HL;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=LN;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=LN;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=LP;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=6.5GHz;rx_mode=LP;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),

        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=HL;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LN;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LP;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=16;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df[
            'tech=ARROW_MMS;ant=ant_0_0;rate=MMS_pkt_type_1;freq=8.0GHz;rx_mode=LP;nb_ant=ant_0_0;nb_rate=NB_pkt_type_1;nb_band=1;nb_channel=1;nb_rx_mode=LF;nb_mini_slot_ms=1;mms_nfrag=2;tc=Cond_Range;subtc=ToF_Std'].dropna()


    ]


    print(data_b)

    ticks = ['HL:eLNA=1 CH5','HL:eLNA=2 CH5','LN::eLNA=1 CH5','LN:eLNA=2 CH5','LP:eLNA=1 CH5','LP:eLNA=2 CH5',
             'HL:eLNA=1 CH9','HL:eLNA=2 CH9','LN:eLNA=1 CH9','LN:eLNA=2 CH9','LP:eLNA=1 CH9','LP:eLNA=2 CH9']

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
    # plt.plot([], c='#28E6E3', label='LP')

    plt.legend()

    plt.xticks(range(0, len(ticks) * 2, 2), ticks)
    #plt.xlim(-2, len(ticks)*2)
    plt.ylim(0, 70)
    plt.grid(linestyle='dotted')
    plt.ylabel('ToF_STD: ps')
    plt.title('ToF Comparison')
    plt.legend(loc='upper left')
    plt.xticks(rotation=15)
    plt.savefig('%s/ToF_Comparison_STD—R.png'%x_path)

def Range_STD():

    data_a = [
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=HL;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=HL;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=HL;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=HL;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
    ]

    data_b = [
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LN;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LN;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LN;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LN;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna()

    ]
    data_c = [
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LP;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=6.5GHz;rx_mode=LP;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LP;ePA=0;eLNA=1;tc=Cond_Range;subtc=ToF_Std'].dropna(),
        df['tech=ARROW;ant=ant_0_0;rate=pkt_type_1;freq=8.0GHz;rx_mode=LP;ePA=0;eLNA=2;tc=Cond_Range;subtc=ToF_Std'].dropna()
    ]

    print(data_b)

    #ticks = ['HL: ant_1_1','LN: ant_1_1','HL: ant_1_2','LN: ant_1_2','HL: ant_2_1','LN: ant_2_1','HL: ant_2_2(CH5)','LN: ant_2_2(CH5)','HL: ant_2_2(CH9)','LN: ant_2_2(CH9)']
    ticks = ['eLNA=1:ant0 CH5','eLNA=2:ant0 CH5','eLNA=1:ant0 CH9','eLNA=2:ant0 CH9']

    def set_box_color(bp, color):
        plt.setp(bp['boxes'], color=color)
        plt.setp(bp['whiskers'], color=color)
        plt.setp(bp['caps'], color=color)
        plt.setp(bp['medians'], color=color)

    plt.figure()

    bpa = plt.boxplot(data_a, positions=np.array(range(len(data_a)))*2.0-0.2, sym='', widths=0.3)
    bpb = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0+0.2, sym='', widths=0.3)
    bpc = plt.boxplot(data_c, positions=np.array(range(len(data_c)))*2.0+0.6, sym='', widths=0.3)

    set_box_color(bpa, '#3182bd') # colors are from http://colorbrewer2.org/
    set_box_color(bpb, '#D7191C') # colors are from http://colorbrewer2.org/
    set_box_color(bpc, '#28E6E3') # colors are from http://colorbrewer2.org/

    # draw temporary red and blue lines and use them to create a legend
    plt.plot([], c='#3182bd', label='HL')
    plt.plot([], c='#D7191C', label='LN')
    plt.plot([], c='#28E6E3', label='LP')

    plt.legend()

    plt.xticks(range(0, len(ticks) * 2, 2), ticks)
    #plt.xlim(-2, len(ticks)*2)
    plt.ylim(0, 70)
    #plt.tight_layout()
    #plt.savefig('boxcompare.png')
    plt.grid(linestyle='dotted')
    plt.ylabel('ToF_STD: ps')
    plt.title('ToF Comparison')
    plt.legend(loc='upper left')
    plt.xticks(rotation=15)
    plt.savefig('%s/ToF_Comparison_STD.png'%x_path)

def ACOND_RXSens():

    data_a = [
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=6.5GHz:eLNA=1:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=6.5GHz:eLNA=2:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=6.5GHz:eLNA=1:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=6.5GHz:eLNA=2:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=6.5GHz:eLNA=1:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=6.5GHz:eLNA=2:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=8.0GHz:eLNA=1:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=8.0GHz:eLNA=2:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=8.0GHz:eLNA=1:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=8.0GHz:eLNA=2:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=8.0GHz:eLNA=1:rx_mode=HL'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=8.0GHz:eLNA=2:rx_mode=HL']
    ]
    data_b = [
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=6.5GHz:eLNA=1:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=6.5GHz:eLNA=2:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=6.5GHz:eLNA=1:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=6.5GHz:eLNA=2:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=6.5GHz:eLNA=1:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=6.5GHz:eLNA=2:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=8.0GHz:eLNA=1:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=8.0GHz:eLNA=2:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=8.0GHz:eLNA=1:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=8.0GHz:eLNA=2:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=8.0GHz:eLNA=1:rx_mode=LN'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=8.0GHz:eLNA=2:rx_mode=LN']
        ]
    data_c = [
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=6.5GHz:eLNA=1:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=6.5GHz:eLNA=2:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=6.5GHz:eLNA=1:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=6.5GHz:eLNA=2:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=6.5GHz:eLNA=1:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=6.5GHz:eLNA=2:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=8.0GHz:eLNA=1:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_0:ant=ant_0:freq=8.0GHz:eLNA=2:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=8.0GHz:eLNA=1:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_1:ant=ant_0:freq=8.0GHz:eLNA=2:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=8.0GHz:eLNA=1:rx_mode=LP'],
        df['tc=RxSens_Search tech=ARROW:subtc=Sensitivity rate=pkt_type_4:ant=ant_0:freq=8.0GHz:eLNA=2:rx_mode=LP']
    ]

    print(data_b)

    ticks = ['0:eLNA=1(CH5)','0:eLNA=2(CH5)',
             '1:eLNA=1(CH5)','1:eLNA=2(CH5)',
             '4:eLNA=1(CH5)','4:eLNA=2(CH5)',
             '0:eLNA=1(CH9)', '0:eLNA=2(CH9)',
             '1:eLNA=1(CH9)','1:eLNA=2(CH9)',
             '4:eLNA=1(CH9)', '4:eLNA=2(CH9)',
             ]

    def set_box_color(bp, color):
        plt.setp(bp['boxes'], color=color)
        plt.setp(bp['whiskers'], color=color)
        plt.setp(bp['caps'], color=color)
        plt.setp(bp['medians'], color=color)

    plt.figure()

    bpa = plt.boxplot(data_a, positions=np.array(range(len(data_a)))*2.0-0.2, sym='', widths=0.3)
    bpb = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0+0.2, sym='', widths=0.3)
    bpc = plt.boxplot(data_c, positions=np.array(range(len(data_c)))*2.0+0.6, sym='', widths=0.3)

    set_box_color(bpa, '#3182bd') # colors are from http://colorbrewer2.org/
    set_box_color(bpb, '#D7191C') # colors are from http://colorbrewer2.org/
    set_box_color(bpc, '#28E6E3') # colors are from http://colorbrewer2.org/

    # draw temporary red and blue lines and use them to create a legend
    plt.plot([], c='#3182bd', label='HL')
    plt.plot([], c='#D7191C', label='LN')
    plt.plot([], c='#28E6E3', label='LP')

    plt.legend()

    plt.xticks(range(0, len(ticks) * 2, 2), ticks)

    plt.grid(linestyle='dotted')
    plt.ylabel('Sensitivity: dB')
    plt.title('RxSens Comparison')
    # plt.legend(loc='upper left')
    plt.xticks(rotation=15)
    plt.savefig('%s/RxSens_Search.png'%x_path)


# plt.show()
while x ==1:
    #file_dir = input('Pls input CSV Path:')
    file_dir = "/Users/shaamos/PycharmProjects/pyworkstation/ACOND_Range.csv"
    if os.path.exists(file_dir):
        df = pd.read_csv(file_dir, header=1,)
        if 'Measurement Unit'in df.iloc[2,0]:
            rowdd = 5
            pass
            # df.drop(index=[0,1,2], inplace=True)
        elif'Measurement Unit' in df.iloc[4,0]:
            rowdd = 7
            pass
            # df.drop(index=[0,1,2,3,4], inplace=True)

        df = pd.read_csv(file_dir, header=1, skiprows=lambda x: 1<x < rowdd)

        All_Station_ID = df['Station ID'].tolist()
        dfver = pd.read_csv(file_dir, nrows=0, low_memory=False)
        ver = list(dfver)
        print(ver[0])
        df.dropna(axis=0,how='any')
        if 'SMT-DEVELOPMENT42' in ver[0]:
            try:
                ACOND_RXSens()
            except Exception as e:
                print(e)
                print('No Range_AVG Columns,Pls CHECK')
            print('Happy to See :)')
        else:
            try:
                Range_AVG()
                Range_AVG_R()
            except Exception as e:
                print(e)
                print('No Range_AVG Columns,Pls CHECK')
            try:
                Range_STD()
                Range_STD_R()
            except Exception as e:
                print(e)
                print('No Range_STD Columns,Pls CHECK')
            print('Happy to See :)')
            pass
    else:
        print('Error with File Path.....Pls Check.Exit')
    import time
    time.sleep(2)
    print('\n')
