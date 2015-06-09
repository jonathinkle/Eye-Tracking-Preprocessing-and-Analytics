# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 15:13:08 2015

@author: Jwink
"""

# import libraries
import pandas as pd
import numpy as np
from os.path import join, isdir
from os import listdir
import time
import helper

# set start timestamp for timing one participant
t = time.time()

# set data directory path. each folder in data folder should contain data, log, and .tsv files
data_path = join('Z:\HuettelLab\Jonathan','Aji_Data')

# get list of usable participants
valid_px_folders = [ px for px in listdir(data_path) if (isdir(join(data_path,px)) and ('exclude' not in px)) ] 

for p in valid_px_folders:
    
    # get individual Px path
    p_path = join(data_path,p)    
    
    # open and store log, behavioral, and eye tracking data files. must specify .tsv encoding as utf-8-sig to strip Byte Object Marker (BOM) flags. fucking piece of shit tobii.
    log = pd.read_table(join(p_path, [f for f in listdir(p_path) if ('Log' in f)][0]), sep='\t')
    beh = pd.read_table(join(p_path, [f for f in listdir(p_path) if ('Data' in f)][0]), sep='\t')    
    eye = pd.read_table(join(p_path, [f for f in listdir(p_path) if ('tsv' in f)][0]), sep='\t', encoding='utf-8-sig', low_memory=False)

    # first to do:
    # strip useless columns from eye
    eye = helper.drop_cols(eye)
    
    # sync time stamps of beh and eye; first arg is start time from log file
    beh, eye = helper.sync_t(log['Exp_Start'].values[0], beh, eye)
    
    # strip excess row data based on timestamps
    eye = helper.trim(beh, eye)    
    
    # preprocess (e.g., interpolate gaps in data) fixation data    
    
    # code AOI data
    # generate fixation metrics for each trial and append each to beh

    # second to do:
    # append questionnaire and survey data to beh largely based on existing code

    # break out of loop after first iteration !for testing!
    break

# substract start timestamp from end timestamp and store as elapsed time
elapsed = time.time() - t

# print the time it takes to run the script for one participant to the console
print "Time Elapsed"
print elapsed



















######################### The land Of Misfit Codez ############################

# stripping BOM (byte object marker) from the beginning of the .tsv data

#file_name = open(join(p_path, [f for f in listdir(p_path) if ('tsv' in f)][0]))
#eye_tsv = file_name.read()
#file_name.close()
#eye_tsv = eye_tsv.decode('utf-8-sig')
#eye = pd.read_csv(eye_tsv,sep='\t',header=True)

