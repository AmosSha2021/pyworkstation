# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import traceback

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import setp
import csv
import os
import sys
import argparse
import matplotlib.patheffects as path_effects
from matplotlib.cbook import boxplot_stats
from warnings import simplefilter
import ploter

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


def data_filter(csvFiles,tcList=None):
    '''
    support to split csv data from PDCA or WiPAS
    1. crate keys = Products with test data if from PDCA
    2. crate keys = tc with test data if from WiPAS

    :param tc: pass a string value which is the one of test header of csv file
    :return: a DataFrames includes: product info and test data of tc
    '''
    csv_PDCA = False
    csv_Local = False
    if tcList==None:
        print('error detected: tc input is None...')
    else:
        myDict = {}
        remove_rows = []
        for file in csvFiles:
            print(f'deal with csv files: {file}')
            df = pd.read_csv(file, header=1, low_memory=False)
            if 'Measurement Unit'in df.iloc[4,0]:
                remove_rows = [0, 1, 2, 3, 4]       # will remove line[0,1,2,3,4] due to that download from PDCA
                csv_PDCA = True
                print(f'remove rows<PDCA> is: {remove_rows}')
            if 'Measurement Unit' in df.iloc[2, 0]:
                remove_rows = [0, 1, 2]             # will remove line[0,1,2] due to that created by WiPAS
                print(f'remove rows<Local> is: {remove_rows}')
                csv_Local = True
            cols = df.columns.tolist()
            # print(cols)
            # product_list = df['Product'].dropna().tolist()
            for tc in tcList:
                if (tc in cols):
                    if csv_PDCA:
                        print(f'found the tc<PDCA>: {tc}')
                        print(f'tc uplimit is {df.at[2, tc]}; lowlimit is {df.at[3, tc]}; unit is: {df.at[4, tc]}; ')
                        # df.drop(labels=remove_rows, axis=0, inplace=True)
                        # remove_rows = []
                        # print(df.shape)
                        # product_list = df['Product'].dropna().tolist()
                        # tc_testData = df[tc].dropna().tolist()
                        # tc_testData = list(map(float,tc_testData)) #covent string to float
                        # print(f'test product:{product_list[0]} and test count: {len(product_list)}')
                        # print(f'test data type {type(tc_testData[0])} and data is: {tc_testData}')
                        # myDict.update({product_list[0]:tc_testData})
                        # print(f'test Dict data length is: {len(myDict)} test Dict data is: {myDict}')
                    if csv_Local:
                        print(f'tc uplimit is {df.at[0, tc]}; lowlimit is {df.at[1, tc]}; unit is: {df.at[2, tc]}; ')
                        df.drop(labels=remove_rows_Local, axis=0, inplace=True)
                        remove_rows = []
                        tc_testData = df[tc].dropna().tolist()
                        tc_testData = list(map(float,tc_testData)) #covent string to float
                        #print(f'test data type {type(tc_testData[0])} and data is: {tc_testData}')
                        myDict.update({tc:tc_testData})
                        print(f'test Dict data length is: {len(myDict)} test Dict data is: {myDict}')
                else:
                    print(f'not found tc: {tc}\nin the file: {file}')

        # #Amos:Output unequal values insert to a DataFrame
        # df_data = pd.DataFrame(pd.DataFrame.from_dict(myDict, orient='index').values.T, columns=list(myDict.keys()))
        # print(f'total data shape: {df_data.shape}')
        # print(f'total data info\n: {df_data}')
        # # df_data = pd.DataFrame({'Product': Products, tc: tc_testData})
        # # df_data = df_data.explode(tc)                  # must be add .explode due to Pandas version > 0.25
        # # df_data[tc] = df_data[tc].astype(float)
        # # print(df_data[tc].dtypes)
        # return df_data

def group_data_filter(csvFiles,tc=None):
    pass

def plot_line():
    pass
if __name__ == '__main__':
    csv = ['/Users/shaamos/Desktop/data_review/SCOND/2700S_PDCA.csv',
           #'/Users/shaamos/Desktop/data_review/SCOND/X2800B_local.csv'
           #'/Users/shaamos/Desktop/LA4X/combine_all/LA4A_P1_S-OTA2_all.csv',
           ]
    # "tc=NFCLD_Calibration:subsubtc=Trim_Step tech=STOCKHOLM:subtc=012.5mV bit_rate=106kbps",
    # "tc=NFCLD_Calibration:subsubtc=Trim_Step tech=STOCKHOLM:subtc=165.0mV bit_rate=106kbps"
    mtc = [
          "tc=NFCLD_Calibration:subsubtc=Trim_Step tech=STOCKHOLM:subtc=165.0mV bit_rate=106kbps",
          "tc=NFCLD_Calibration:subsubtc=Trim_Step tech=STOCKHOLM:subtc=012.5mV bit_rate=106kbps",
          # "tech=STOCKHOLM;bit_rate=106kbps;tc=NFCLD_Calibration;subtc=012.5mV;subsubtc=Trim_Step",
          # "tech=STOCKHOLM;bit_rate=106kbps;tc=NFCLD_Calibration;subtc=165.0mV;subsubtc=Trim_Step",
          ]
    data_filter(csvFiles=csv,tcList=mtc)

    # np.random.seed(19680801)
    #
    # dt = 0.01
    # t = np.arange(0, 30, dt)
    # print(t)
    # print(type(t))
    # t1 = pd.Series(t)
    # print(t1)
    # print(type(t1))
    # nse1 = np.random.randn(len(t1))  # white noise 1
    # nse2 = np.random.randn(len(t1))  # white noise 2
    #
    # # Two signals with a coherent part at 10Hz and a random part
    # s1 = np.sin(2 * np.pi * 10 * t1) + nse1
    # s2 = np.sin(2 * np.pi * 10 * t1) + nse2
    # print(s1)
    # print(s2)
    # fig, axs = plt.subplots(2, 1)
    # axs[0].plot(t1, s1, t1, s2)
    # axs[0].set_xlim(0, 2)
    # axs[0].set_xlabel('time')
    # axs[0].set_ylabel('s1 and s2')
    # axs[0].grid(True)
    #
    # cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
    # axs[1].set_ylabel('coherence')
    #
    # fig.tight_layout()
    # plt.show()