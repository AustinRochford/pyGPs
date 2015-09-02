# Converts from .mat to .csv and removes nans from dataset

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime

def buildDate(val):
  # convert val into datetime
  # Zero pad where necessary
  fmt = '%Y %m %d'
  yr = str(val[0]).strip()
  mth = str(val[1]).strip()
  if len(mth) == 1: mth = '0'+mth
  day = str(val[2]).strip()
  if len(day) == 1: day = '0'+day
  dd = yr + ' ' + mth + ' ' + day
  return date2num(datetime.strptime(dd,fmt))
  

# ['snow_gnd', '__version__', 'url', '__header__', 'snowfall', '__globals__', 
#  'column_names', 'datevectors', 'alldata']
mat_contents = sio.loadmat('whistler.mat')
snow_gnd = np.asarray(mat_contents['snow_gnd'],dtype=np.float)
dates = mat_contents['datevectors']


t = []; x = []
for i,d in enumerate(dates):
  y = np.float(snow_gnd[i])
  if ~np.isnan(y):
    x.append(y)
    t.append(buildDate(d))

np.savetxt('whistler.csv',zip(t,x),delimiter=',')

