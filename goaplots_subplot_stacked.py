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



# make a dict that associates letters with lines - tried to do this for a legend, but don't feel like it worked.
abc_list = list('abc') # a quick way to make the list ['a', 'b', 'c', 'd']
month_list = ['April','May','July']
month_dict = dict(zip(abc_list, month_list))


fig, axs = plt.subplots(4, 1, figsize=(6,7), squeeze=False)
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0, hspace=0.3)

fs = 12
fs2 = 8

#DAl plot
axs[0,0].plot(april_dist, april_DAl,'#014F94', marker = 'o', fillstyle ='none',linewidth=0, markersize = '7', label = 'April')
axs[0,0].plot(may_dist,may_DAl,'#00877B' , marker = 'o',fillstyle ='none', linewidth=0, markersize ='7', label = 'May')
axs[0,0].plot(july_dist,july_DAl,'#CB7941', marker = 'o', fillstyle ='none',linewidth=0, markersize='7', label = 'July')
axs[0,0].set_ylabel('DAl(nM)', color='black', size=fs,fontweight = 'bold')
#axs[0,0].set_xlabel('Distance from Shore(km)')
ax2 = axs[0,0].twinx()
ax2.plot(april_dist,april_sal,'#014F94', marker = '+', linewidth=1, label = 'salinity')
ax2.plot(may_dist, may_sal, '#00877B',marker = '+', linewidth=1)
ax2.plot(july_dist, july_sal,'#CB7841',marker = '+', linewidth=1)
ax2.set_ylabel('Salinity', color='black', size=fs,fontweight = 'bold')
#axs[0,0].set_title('DAl', fontsize=12)
axs[0,0].legend(fontsize=fs2, ncol=1, loc = 0)
#ax2.legend(fontsize=fs2, ncol=1, loc = 8)
axs[0,0].text(0,1.05, 'a.' , fontsize=fs, fontweight = 'bold', transform = axs[0,0].transAxes)
axs[0,0].set_yscale('log')
axs[0,0].tick_params(direction='in')
axs[0,0].tick_params(which = 'minor', direction='in')
axs[0,0].set_xticklabels([])
ax2.tick_params(direction = 'in')
#ax2.set_xticks(direction = 'in')

#DMn plot
axs[1,0].plot(april_dist, april_DMn,'#014F94', marker = 'D', fillstyle ='none',linewidth=0, markersize = '7', label = 'April')
axs[1,0].plot(may_dist,may_DMn,'#00877B' , marker = 'D', fillstyle ='none',linewidth=0, markersize ='7', label = 'May')
axs[1,0].plot(july_dist,july_DMn,'#CB7941', marker = 'D',fillstyle ='none', linewidth=0, markersize='7', label = 'July')
axs[1,0].set_ylabel('DMn(nM)', color='black', size=fs,fontweight = 'bold')
#axs[1,0].set_xlabel('Distance from Shore(km)')
#axs[1,0].set_yscale('log')
ax2 = axs[1,0].twinx()
ax2.plot(april_dist,april_sal,'#014F94', marker = '+', linewidth=1, label = 'salinity')
ax2.plot(may_dist, may_sal, '#00877B',marker = '+', linewidth=1)
ax2.plot(july_dist, july_sal,'#CB7841',marker = '+', linewidth=1)
ax2.set_ylabel('Salinity', color='black', size=fs,fontweight = 'bold')
#axs[1,1].set_title('DMn', fontsize=12)
axs[1,0].legend(fontsize=fs2, ncol=1, loc = 0)
#ax2.legend(fontsize=20, ncol=1, loc = 8)
axs[1,0].text(0,1.05, 'b.' , fontsize=fs, fontweight = 'bold', transform = axs[1,0].transAxes)
axs[1,0].tick_params(direction='in')
axs[1,0].set_xticklabels([])
ax2.tick_params(direction = 'in')


#TDAl plot
axs[2,0].plot(april_dist, april_TDAl,'#014F94', marker = 'o', linewidth=0, markersize = '7', label = 'April')
axs[2,0].plot(may_dist,may_TDAl,'#00877B' , marker = 'o', linewidth=0, markersize ='7', label = 'May')
axs[2,0].plot(july_dist,july_TDAl,'#CB7941', marker = 'o', linewidth=0, markersize='7', label = 'July')
axs[2,0].set_ylabel('TDAl(nM)', color='black', size=fs,fontweight = 'bold')
#axs[2,0].set_xlabel('Distance from Shore(km)')
axs[2,0].set_yscale('log')
ax2 = axs[2,0].twinx()
ax2.plot(april_dist,april_sal,'#014F94', marker = '+', linewidth=1, label = 'salinity')
ax2.plot(may_dist, may_sal, '#00877B',marker = '+', linewidth=1)
ax2.plot(july_dist, july_sal,'#CB7841',marker = '+', linewidth=1)
ax2.set_ylabel('Salinity', color='black', size=fs,fontweight = 'bold')
#axs[2,0].set_title('TDAl', fontsize=24)
axs[2,0].legend(fontsize=fs2, ncol=1, loc = 0)
#ax2.legend(fontsize=20, ncol=1, loc = 8)
axs[2,0].text(0,1.05, 'c.' , fontsize=fs, fontweight = 'bold', transform = axs[2,0].transAxes)
axs[2,0].tick_params(direction='in')
axs[2,0].tick_params(which = 'minor', direction='in')
axs[2,0].set_xticklabels([])
ax2.tick_params(direction = 'in')


#TDMn plot
axs[3,0].plot(april_dist, april_TDMn,'#014F94', marker = 'D', linewidth=0, markersize = '7', label = 'April')
axs[3,0].plot(may_dist,may_TDMn,'#00877B' , marker = 'D', linewidth=0, markersize ='7', label = 'May')
axs[3,0].plot(july_dist,july_TDMn,'#CB7941', marker = 'D', linewidth=0, markersize='7', label = 'July')
axs[3,0].set_ylabel('TDMn(nM)', color='black', size=fs,fontweight = 'bold')
axs[3,0].set_xlabel('Distance from Shore(km)',fontweight = 'bold')
axs[3,0].set_yscale('log')
ax2 = axs[3,0].twinx()
ax2.plot(april_dist,april_sal,'#014F94', marker = '+', linewidth=1, label = 'April salinity')
ax2.plot(may_dist, may_sal, '#00877B',marker = '+', linewidth=1, label = 'May Salinity')
ax2.plot(july_dist, july_sal,'#CB7841',marker = '+', linewidth=1, label = 'July Salinity')
ax2.set_ylabel('Salinity', color='black', size=fs,fontweight = 'bold')
#axs[1,1].set_title('TDMn', fontsize=12)
axs[3,0].legend(fontsize=fs2, ncol=3, loc = 1)
ax2.legend(fontsize=fs2, ncol=1, loc = 0)
axs[3,0].text(0,1.05, 'd.' , fontsize=fs, fontweight = 'bold', transform = axs[3,0].transAxes)
axs[3,0].tick_params(direction='in')
axs[3,0].tick_params(which = 'minor', direction='in')
ax2.tick_params(direction = 'in')

plt.show()
fig.savefig(out_dir + 'GoA_allPlots_stacked.png')