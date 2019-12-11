# -*- coding: utf-8 -*-
"""
Spyder Editor

Air Quality Index Formating from CSV files.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
#
'''
 iterrows()is a generator that iterates over the rows of the dataframe 
 and returns the index of each row, in addition to an object containing the row itself. 
 iterrows() is optimized to work with Pandas dataframes, and, 
 although it’s the least efficient way to run most standard functions (more on that later), 
 it’s a significant improvement over crude looping. 

'''
path = "C:\\Users\\INTEL\\Desktop\\misc\\AQI-Project-master\\AQI-Project-master\\Data\\AQI".strip()
print(os.listdir(path))
def avg_data(files):
    temp_i = 0
    average = []
    for rows in pd.read_csv(files,chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        #print(df.iterrows())
        for index,row in df.iterrows():
            #print(index)
            #print(rows)
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg = add_var / 24
        temp_i +=1
        average.append(avg)    
    return average

if __name__ == '__main__':
    year_avg = {}
    for files in os.listdir(path):
        filename = path + "\\"+files
        year_avg[files] = avg_data(filename)
        #print(year_avg[files])
        plt.plot(range(len(year_avg[files])),year_avg[files],label = files+"data")
        plt.xlabel('Day')
        plt.ylabel('PM 2.5')
        plt.legend(loc='upper right')
        plt.show()
        plt.show()