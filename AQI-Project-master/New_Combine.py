# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:57:11 2019

@author: INTEL
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import requests
from bs4 import BeautifulSoup
import csv
from New_AQI_Pgm import avg_data
path = "C:\\Users\\INTEL\\Desktop\\misc\\AQI-Project-master\\AQI-Project-master\\Data\\AQI".strip()
filename = path + "\\"+ 'aqi2013.csv'
outfile = r"C:\Users\INTEL\Desktop\misc\AQI-Project-master\AQI-Project-master\Data\Real-Data\Real_Combine.csv"
## Extracting average of PM2.5 columns

def met_data(month, year):
    filename1 = "C:\\Users\\INTEL\\Desktop\\misc\\AQI-Project-master\\AQI-Project-master\\Data\\Html_Data\\".strip() + str(year)+"\\" + str(month)+".html"
    #print(filename1)
    file_html = open(filename1, 'rb')
    plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD) / 15

    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)

    length = len(finalD)

    finalD.pop(length - 1)
    finalD.pop(0)

    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)

    return finalD

def data_combine(year, cs):
    file_name = "C:\\Users\\INTEL\\Desktop\\misc\\AQI-Project-master\\AQI-Project-master\\Data\\Real-Data\\real_" + str(year)+".csv"
    for a in pd.read_csv(file_name, chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist

if __name__ == "__main__":
    year_avg = {}
    data1 = {}
    file_path = "C:\\Users\\INTEL\\Desktop\\misc\\AQI-Project-master\\AQI-Project-master\\Data\\Real-Data"
    for files in os.listdir(path):
        filename = path + "\\"+files
        year_avg[files] = avg_data(filename)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    for year in year_avg.keys():
        print(year[3:7])
    for year in year_avg.keys():
        final_data = []
        file_name = "C:\\Users\\INTEL\\Desktop\\misc\\AQI-Project-master\\AQI-Project-master\\Data\\Real-Data\\real_" + str(year[3:7])+".csv"
        with open(file_name, 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(
                ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in range(1, 13):
            temp = met_data(month, year[3:7])
            final_data = final_data + temp
            
        pm = year_avg[year]

        #if len(pm) == 364:
        #    pm.insert(364, '-')

        for i in range(len(final_data)-1):
            # final[i].insert(0, i + 1)
            final_data[i].insert(8, pm[i])

        with open(file_name, 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)
                    
        data1[year[3:7]] = data_combine(year[3:7], 600)
    total=[]
    for k,v in data1.items():
        total +=v
    with open(outfile , 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
    
    df=pd.read_csv(outfile)