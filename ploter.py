# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/11 14:01
@Auth ： Amos_Sha
@File ：ploter.py
"""
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

class Ploter():
    def __init__(self,tc_list, dir):
        '''
        :param tc_list: defined a list that includes test items you want to plots
        :param dir: combined csv file Dir
        :return:
        '''
        self.tc_list = tc_list
        self.combineCSV_dir = dir
        #self.skip_rows_sota = [0, 1, 2, 3, 4]
        self.remove_rows = [0, 1, 2, 3, 4]
        self.csvFiles = self.getFileList(self.combineCSV_dir)
        self.tc = 'expected tc'
        self.tc_upLimit=''
        self.tc_lowLimit = ''
        self.tc_unit = ''
        self.csv_PDCA = False
        self.csv_Local = False

    def getFileList(self, dir):
        '''
        :return: that will return a list includes csv files
        '''
        if(os.path.isdir(dir)):
            f_list = os.listdir(dir)
            csvfile_list = []
            for i in f_list:
                if(os.path.splitext(i)[1] == ".csv"):
                    csvfile_list.append(os.path.join(dir,i))
            return csvfile_list
        else:
            print(f' detected: {dir} --> is not a Directory')

    def add_median_labels(self,ax, fmt='.1f'):
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
            text.set_path_effects([path_effects.Stroke(linewidth=3, foreground=median.get_color()),path_effects.Normal()])


    def data_filter_SOTA(self, tc=None):
        '''
        :param tc: pass a string value which is the one of test header of csv file
        :return: a DataFrames includes: product info and test data of tc
        '''
        if tc==None:
            print('error detected: tc input is None...')
        else:
            try:
                self.tc = tc
                print(f'tc name expected is: {self.tc}\n')
                myDict = {}
                for file in self.csvFiles:
                    print(f'deal with csv files: {file}')
                    # df = pd.read_csv(file, header=1, skiprows= self.skip_rows_sota, low_memory=False)
                    df = pd.read_csv(file, header=1,low_memory=False)
                    self.tc_upLimit = df.at[2, tc]
                    self.tc_lowLimit = df.at[3, tc]
                    self.tc_unit = df.at[4, tc]
                    print(f'tc uplimit is {self.tc_upLimit}; lowlimit is {self.tc_lowLimit}; unit is: {self.tc_unit}; ')
                    df.drop(labels=self.remove_rows, axis=0, inplace=True) # remove row data(Display Name;PDCA Priority;Upper Limit;Lower Limit;Measurement Unit) from df
                    cols = df.columns.tolist()
                    product_list = df['Product'].dropna().tolist()
                    if(len(set(product_list)) == 1) and (tc in cols):
                        tc_testData = df[tc].dropna().tolist()
                        tc_testData = list(map(float,tc_testData)) #covent string to float
                        print(f'test product:{product_list[0]} and test count: {len(product_list)}')
                        #print(f'test data type {type(tc_testData[0])} and data is: {tc_testData}')
                        myDict.update({product_list[0]:tc_testData})
                        # print(f'test Dict data length is: {len(myDict)}')
                #print(f'test Dict data is: {myDict}')
                #Amos:Output unequal values insert to a DataFrame
                df_data = pd.DataFrame(pd.DataFrame.from_dict(myDict, orient='index').values.T, columns=list(myDict.keys()))
                print(f'total data shape: {df_data.shape}')
                print(f'total data info\n: {df_data}')
                # df_data = pd.DataFrame({'Product': Products, tc: tc_testData})
                # df_data = df_data.explode(tc)                  # must be add .explode due to Pandas version > 0.25
                # df_data[tc] = df_data[tc].astype(float)
                # print(df_data[tc].dtypes)
                return df_data
            except Exception:
                print(f'error detected: {traceback.format_exc()}')


    def plot_box_SOTA_tc(self, data_list=None, tc=None):
        '''
        this function will plot SOTA data
        :param data_list: DataFrames
        :return:
        '''
        if tc==None:
            print("stop plot creat due to no data detected")
        else:
            simplefilter(action='ignore', category=FutureWarning)
            f, ax = plt.subplots()
            # bp = sns.boxplot(data=data_list)
            if self.csv_PDCA:
                tclist = tc.split(' ')
                for temp in tclist:
                    if temp.find('tc=') != -1:
                        tcStr = temp
                        # print(f'tcStr is: {tcStr}')

                    if temp.find('tech=') != -1:
                        subtcStr = temp.split(":")
                        # print(f'subtc is: {subtcStr}')

                    if temp.find('tc=') != -1:
                        typeRateStr = temp
                        # print(f'typeRateStr is: {typeRateStr}')
                bp.set(xlabel=subtcStr[0] + ': Limits(' + str(self.tc_lowLimit) + ',' + str(self.tc_upLimit) + ')',
                       ylabel=subtcStr[1] + '(' + self.tc_unit + ')')
            if self.csv_Local:
                bp = sns.boxplot(data=data_list)
                tc_list = tc.split(';')
                for temp in tc_list:
                    if temp.find('tech=') != -1:
                        techStr = temp
                    if temp.find('tc=') != -1:
                        tcStr = temp
                    if temp.find('bit_rate=') != -1:
                        bit_rateStr = temp
                    if temp.find('subtc=') != -1:
                        subtcStr = temp
                    if temp.find('subsubtc=') != -1:
                        subsubtcStr = temp
                bp.set(xlabel=subtcStr+ "_" +subsubtcStr+ ': Limits(' + str(self.tc_lowLimit) + ',' + str(self.tc_upLimit) + ')',
                       ylabel=subtcStr + '(' + self.tc_unit + ')')


            #title = "tc=Tx_Clock_Ext_Reader:subtc=FieldStrengthDC_Corr"
            plt.title(tcStr)
            # self.add_median_labels(bp)
            # bp.axhline(self.tc_upLimit, ls='--', color='r')
            # bp.axhline(self.tc_lowLimit, ls='--', color='r')
            plt.grid()
            plt.tight_layout()
            # f.show(bp)
            # plt.savefig('%s/%s.png' % os.getcwd()%subtcStr)
            plt.savefig(os.path.join(os.getcwd(),tc +'.png'))
            print(f"created png file in: {os.getcwd()}\n")


    def plot_box_SCOND_tc(self,data_list=None, tc=None):
        pass

    def csv_tc_filter_combine(self,tc=None,product=False,stationID=False):
        # if tc==None:
        #     print('error detected: tc input is None...')
        # else:
        myDict = {}
        self.remove_rows = []
        for file in self.csvFiles:
            print(f'deal with csv files: {file}')

            df = pd.read_csv(file, header=1, low_memory=False)
            if 'Measurement Unit' in df.iloc[4, 0]:
                self.remove_rows = [0, 1, 2, 3, 4]  # will remove line[0,1,2,3,4] due to that download from PDCA
                self.csv_PDCA = True
                print(f'remove rows<PDCA> is: {self.remove_rows}')
            if 'Measurement Unit' in df.iloc[2, 0]:
                self.remove_rows = [0, 1, 2]  # will remove line[0,1,2] due to that created by WiPAS
                print(f'remove rows<Local> is: {self.remove_rows}')
                self.csv_Local = True
            cols = df.columns.tolist()
            # print(cols)
            if (tc in cols) and self.csv_PDCA:
                print(f'found the tc<PDCA>: {tc}')
                print(f'tc uplimit is {df.at[2, tc]}; lowlimit is {df.at[3, tc]}; unit is: {df.at[4, tc]}; ')
                df.drop(labels=self.remove_rows, axis=0, inplace=True)
                if product:
                    product_list = df['Product'].dropna().tolist()
                    if (len(set(product_list)) == 1):   # one csv file one product only is requested
                        tc_testData = df[tc].dropna().tolist()
                        tc_testData = list(map(float,tc_testData)) #covent string to float
                        print(f'test product:{product_list[0]} and test count: {len(product_list)}')
                        print(f'test data type {type(tc_testData[0])} and data legth is: {len(tc_testData)}')
                        myDict.update({product_list[0]:tc_testData})
                        print(f'test Dict data length is: {len(myDict)}')
                    else:
                        print(f'there is {len(set(product_list))} kinds products')
                if stationID:
                    stationID_list = df['Station ID'].dropna().tolist()
                    if (len(set(stationID_list)) == 1):  # one csv file one stationID only is requested
                        tc_testData = df[tc].dropna().tolist()
                        tc_testData = list(map(float, tc_testData))  # covent string to float
                        print(f'test data type {type(tc_testData[0])} and data legth is: {len(tc_testData)}')
                        myDict.update({stationID_list[0]: tc_testData})
                        print(f'test Dict data length is: {len(myDict)}')
                    else:
                        print(f'there is {len(set(stationID_list))} kinds station ID')

            if (tc in cols) and self.csv_Local:
                print(f'tc uplimit is {df.at[0, tc]}; lowlimit is {df.at[1, tc]}; unit is: {df.at[2, tc]}; ')
                df.drop(labels=self.remove_rows, axis=0, inplace=True)
                if stationID:
                    stationID_list = df['Station ID'].dropna().tolist()
                    if (len(set(stationID_list)) == 1):  # one csv file one stationID only is requested
                        tc_testData = df[tc].dropna().tolist()
                        tc_testData = list(map(float, tc_testData))  # covent string to float
                        print(f'test data type {type(tc_testData[0])} and data legth is: {len(tc_testData)}')
                        myDict.update({stationID_list[0]: tc_testData})
                        print(f'test Dict data length is: {len(myDict)}')
                    else:
                        print(f'there is {len(set(stationID_list))} kinds station ID')

        return myDict


def maker(tc_list):
    parser = argparse.ArgumentParser()
    parser.description = "to figout apple pass info from the combined csv"
    #parser.add_argument("-f",'--file',help ="csv file path")
    parser.add_argument("-d",'--directory',help ="csv file path")
    args = parser.parse_args()
    #csvfile = args.file
    mArgs = args.directory
    print("-" * 50)
    print(f'passed directory:{mArgs}')
    myPloter = Ploter(tc_list,mArgs)
    print("-"*50)
    for mtc in tc_list:
        # df_data = myPloter.data_filter_SOTA(tc= mtc)
        # myPloter.plot_box_SOTA_tc(df_data, tc=mtc)
        df_data = myPloter.csv_tc_filter_combine(tc=mtc, product=False,stationID=True)
        myPloter.plot_box_SOTA_tc(df_data, tc=mtc)


if __name__ == '__main__':
    # tc_list = [
    #            "tc=Tx_Clock_Ext_Reader tech=STOCKHOLM:subtc=FieldStrengthDC_Corr type=NA:bit_rate=NA",
    #             "tc=Tx_Clock_Ext_Reader tech=STOCKHOLM:subtc=Curr_Val type=NA:bit_rate=NA",
    #             "tc=TxResFreq_TxDr_H_Z tech=STOCKHOLM:subtc=TxDrive_HighZ_Res_Freq_Avg_CF"
    #            ]
    tc_list = [
            "tech=STOCKHOLM;bit_rate=106kbps;tc=NFCLD_Calibration;subtc=165.0mV;subsubtc=Trim_Step",
            "tech=STOCKHOLM;bit_rate=106kbps;tc=NFCLD_Calibration;subtc=012.5mV;subsubtc=Trim_Step",
         ]

    maker(tc_list)
