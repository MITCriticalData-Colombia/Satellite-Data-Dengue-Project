# -*- coding: utf-8 -*-

from sentinelhub import SHConfig
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import sys
from datetime import timedelta
sys.path.insert(0,'..') 
from sentinelhub import MimeType, CRS, BBox, SentinelHubRequest, SentinelHubDownloadClient, DataCollection, bbox_to_dimensions, DownloadRequest

from epiweeks import Week, Year
from datetime import date
import glob, shutil

from windows.request_multiple_images import download_multiple_images
from windows.request_multiple_images import get_folder_ID
from windows.rename import get_request_individual

coordenates =  [-75.607738,6.192609, -75.538731,6.301649]

# Customized for SENTINEL2_L1C 
root_images = "\\data\\"
dataset = "\\DATASET\\"

path = os.path.abspath(os.getcwd()) + root_images  
dataset_path = os.path.abspath(os.getcwd()) + dataset  
    
if not os.path.isdir(path):
    os.makedirs(path)
    #print("Creating temporal data folder")
if not os.path.isdir(dataset_path):
    os.makedirs(dataset_path)
    #print("Creating /DATASET")
else:
    #print("Re-writing in temporal data folder")
    pass
img_format = "tiff"
# Define the range of years
initial_year = 2015
end_year = 2018
years = list(range(initial_year,end_year))
first_2015_week = 44
end_year = 2020

start_2015 = Week(initial_year,first_2015_week).startdate()

weeks_2015 = list(range(first_2015_week, 53))
weeks = list(range(1,53))


# Download data
for year in years:
    if year == 2015:
        for week in weeks_2015:
            print(f"Year: {year} - week: {week}")
            # Set starting date for given year based on 
            start = Week(year, week).startdate()
            # Download individual images
            download_multiple_images(coordenates, start, str(year))
            # Obtain ID as the last-obtained response.tiff file, "real-time"
            folder_path = get_folder_ID(root_images, img_format)
            # Rename image based on JSON timestamp filter 
            dates = get_request_individual(folder_path+"\\request.json", img_format)
            # Clean folders which contain black images
            path_to_blank_ids  = "." + root_images + "\\" + str(year) + "\\*\\*" 
            ids = glob.glob(path_to_blank_ids)
            for idx in ids:
                if "response" in idx:
                    folder_path = idx.replace("\\" + "response." + img_format, "")
                    #print(folder_path)
                    shutil.rmtree(folder_path)
            ids = glob.glob(path_to_blank_ids)
            #print("ids available: ", ids)
                    
            #flag =  [idx if ("response" in idx) for idx in ids]
    #elif year ==2016:
    else:
        for week in weeks:
            print(f"Year: {year} - week: {week}")
            # Set starting date for given year based on 
            start = Week(year, week).startdate()
            # Download individual images
            download_multiple_images(coordenates, start, str(year))
            # Obtain ID as the last-obtained response.tiff file, "real-time"
            folder_path = get_folder_ID(root_images, img_format)
            # Rename image based on JSON timestamp filter 
            dates = get_request_individual(folder_path+"\\request.json", img_format)
            # Clean folders which contain black images
            path_to_blank_ids  = "." + root_images + "\\" + str(year) + "\\*\\*" 
            ids = glob.glob(path_to_blank_ids)
            for idx in ids:
                if "response" in idx:
                    folder_path = idx.replace("\\" + "response." + img_format, "")
                    #print(folder_path)
                    shutil.rmtree(folder_path)
            ids = glob.glob(path_to_blank_ids)
            
# Move to structured folder in DATASETS
root_images_store = "." + root_images
dataset_store = "." + dataset
for root, dirs, files in os.walk(root_images_store, topdown=True):
    for name in files:
        path = os.path.join(root, name)
        #print(path)
        if img_format in path and not dataset_store in path:
            shutil.copy(path, dataset_store)
            
images = glob.glob("./" + dataset + "/*")


'''
shutil.rmtree("dataset")
shutil.rmtree("data")
cleaners(dataset, root_images)
'''