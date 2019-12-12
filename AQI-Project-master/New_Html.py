# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:20:39 2019

@author: Plaban_Nayak
"""


import time
import requests
import sys
import os

#Path to store the output
file_path = "C:\\Users\Plaban_Nayak\\Desktop\\Air-Quality-Index-Prediction-master\\AQI-Project-master\\AQI-Project-master\\Data"
# Retrieve climate data for Bhubaneswar from the below url
def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10):
                url= "https://en.tutiempo.net/climate/0{}-{}/ws-429710.html".format(month,year)
            else:
                url = "https://en.tutiempo.net/climate/{}-{}/ws-429710.html".format(month,year)
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')
            output_path = file_path + "\\"+str(year)
            out_path = output_path + "\\"+str(month)+".html"
            print(out_path)
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            with open(out_path,"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
if __name__ == '__main__':
    start_time = time.time()
    retrieve_html()
    end_time = time.time()
    print("Time Taken : {}".format(end_time - start_time))