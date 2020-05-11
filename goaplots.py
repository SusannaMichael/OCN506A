"""
Code to try to plot data better
"""



#imports
import numpy as np
import sys, os
import matplotlib.pyplot as plt
import pickle
import argparse
import matplotlib.pyplot as plt

#local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# make sure the output directory exists
this_dir = os.path.abspath('.').split('/')[-1]
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../' + this_parent + '_output/'
print('Creating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)

myplace = 'OCN506A' # Change this to fit your own computer

# input directory
in_dir = '../' + myplace + '_data/'

# define the input filename
in_fn = in_dir + 'goa_surface_simple.txt'

# create empty lists to put our data in
dist = []
sal = []
DAl = []
TDAl = []
DMn = []
TDMn = []
count = 0
month = []

april_dist = []
april_sal = []
april_DAl = []
april_TDAl = []
april_DMn = []
april_TDMn = []

may_dist = []
may_sal = []
may_DAl = []
may_TDAl = []
may_DMn = []
may_TDMn = []

july_dist = []
july_sal = []
july_DAl = []
july_TDAl = []
july_DMn = []
july_TDMn = []





with open(in_fn, 'r', errors='ignore') as f:
    for line in f:
        if count > 0:
            count = count + 1
            lls = line.split()
            month.append(str(lls[0]))
            dist.append(float(lls[2]))
            sal.append(float(lls[1]))
            DAl.append(float(lls[3]))
            TDAl.append(float(lls[4]))
            DMn.append(float(lls[5]))
            TDMn.append(float(lls[6]))
        else:
            count = count + 1

#print(month)
#print(dist)
#print(sal)
#print(DAl)
#print(TDAl)
#print(DMn)
#print(TDMn)

for i in range(len(month)):
    if month[i]=='April':
        april_dist.append(dist[i])
        april_sal.append(sal[i])
        april_DAl.append(DAl[i])
        april_TDAl.append(TDAl[i])
        april_DMn.append(DMn[i])
        april_TDMn.append(TDMn[i])
    elif month[i]=='May':
        may_dist.append(dist[i])
        may_sal.append(sal[i])
        may_DAl.append(DAl[i])
        may_TDAl.append(TDAl[i])
        may_DMn.append(DMn[i])
        may_TDMn.append(TDMn[i])
    elif month[i]=='July':
        july_dist.append(dist[i])
        july_sal.append(sal[i])
        july_DAl.append(DAl[i])
        july_TDAl.append(TDAl[i])
        july_DMn.append(DMn[i])
        july_TDMn.append(TDMn[i])

        
    i = i+1  

#print(april_sal)
#print(may_sal)
#print(july_sal)

# PLOTTING
plt.close('all') # always start by cleaning up


month_list = ['April','May','July']

# make a plot with distance from shore on the x axis, and 2 y-axes: analyte and salinity. Want 4 fof these arranged in a grid 

fs = 16
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

# make a dict that associates letters with lines - tried to do this for a legend, but don't feel like it worked.
abc_list = list('abc') # a quick way to make the list ['a', 'b', 'c', 'd']
month_list = ['April','May','July']
month_dict = dict(zip(abc_list, month_list))




ax.plot(april_dist, april_TDAl,'#014F94', marker = 'o', linewidth=0, markersize = '8', label = 'April')
ax.plot(may_dist,may_TDAl,'#00877B' , marker = 'o', linewidth=0, markersize ='8', label = 'May')
ax.plot(july_dist,july_TDAl,'#CB7941', marker = 'o', linewidth=0, markersize='8', label = 'July')
ax.set_ylabel('TDAl(nM)', color='black', size=fs)
ax.set_xlabel('distance from shore(m)')
ax.set_yscale('log')
ax2 = ax.twinx()
ax2.plot(april_dist,april_sal,'#014F94', marker = '+', linewidth=1, label = 'salinity')
ax2.plot(may_dist, may_sal, '#00877B',marker = '+', linewidth=1)
ax2.plot(july_dist, july_sal,'#CB7841',marker = '+', linewidth=1)
ax2.set_ylabel('Salinity', color='black', size=fs)
ax.set_title('TDAl', fontsize=24)
ax.legend(fontsize=20, ncol=1, loc = 7)
ax2.legend(fontsize=20, ncol=1, loc = 8)
plt.show()
fig.savefig(out_dir + 'GoA_TDAl.png')