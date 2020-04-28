"""
Code to test input and (filtered) output of a text file.
"""

# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module as mymod
import numpy as np
import matplotlib.pyplot as plt


myplace = 'OCN506A' # *** YOU NEED TO EDIT THIS ***

# input directory
in_dir = '../' + myplace + '_data/'

# make sure the output directory exists
out_dir = '../' + myplace + '_output/'
mymod.make_dir(out_dir)

# define the input filename
in_fn = in_dir + '2017-01-0118.ctd'
# this is some Canadian CTD data, formatted in a strict but
# difficult-to-use way

# define the output filename
out_fn = out_dir + 'out_test.txt'

# open the output file for writing
outfile = open(out_fn, 'w')

#make lists to store data in
depth = []
temp = []

signal = False
# go through the input file one line at a time, and flag when you hit the end of the header


with open(in_fn, 'r', errors='ignore') as f: #open the file
	#go through each line in the file
	for line in f: 
		#Check to see if the signal has changed to true
		if signal ==True:
			#Split the line apart at the columns
			lls = line.split()
			depth.append(float(lls[1]))
			temp.append(float(lls[2])) #Make empty list and  put in z and t
			#Check to see if we are at the end of the header
		if '*END OF HEADER' in line and signal is False:
			signal = True


print (depth)
print (temp)
#outfile.write('depth = %0.3f\n' % (depth))
#outfile.write('temperature = %0.3f\n' % (temp))

# close the output file
#outfile.close()

# plotting
plt.close('all')
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)
ax.plot(temp, depth, 'ob')
ax.grid(True)
ax.set_xlabel('Temperature [deg C]')
ax.set_ylabel('depth [m]')
plt.gca().invert_yaxis() # this reverses y axis
ax.set_title(in_fn + ': From Scratch')
plt.show()
#plt.savefig(out_fn_1)
