#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:04:26 2022

@author: ethanburkett
"""
#NORMALIZATION

#import scipy.io
#import seaborn as sns
#import pandas as pd
#import matplotlib.pyplot as plt
#import io
#import numpy as np
#import sys
#from sklearn import preprocessing 

import numpy as np
from scipy.stats import zscore
import pandas as pd
# create a for loop to read/normalize data

# we need to have groups information. The best way to do that is to create an excel table, one column is group, the other is subject_id.

group_file = pd.read_excel('/Users/ethanburkett/Desktop/group_file.xlsx')

for group, sub_id in zip(group_file.group, group_file.subject_id):
    # import data
    # path of single subject:
    single_path = '/Users/ethanburkett/Desktop/TestPD/'+group+'/'+str(sub_id)+'/tvb_inputs/rfMRI.ica/ts.txt'
    subj = np.loadtxt(single_path)
    normalized_data  = zscore(subj)
    save_path = '/Users/ethanburkett/Desktop/TestPD/'+group+'/'+str(sub_id)+'/'+str(sub_id)+'_norm.txt'
    np.savetxt(save_path, normalized_data, delimiter='  ', newline='\n')
    
    