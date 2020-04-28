import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module as mymod
import matplotlib.pyplot as plt

myplace = 'OCN506A' # Change this to fit your own computer

# input directory
in_dir = '../' + myplace + '_data/'

# define the input filename
in_fn = in_dir + '2017-01-0118.ctd'

# create empty lists to put our data in
depth = []
temp = []

# create a signal to tell us when we have passed the header
signal = False

# open the file
with open(in_fn, 'r', errors='ignore') as f:
	# go through each line in the file
	for line in f:
		# check if the signal has changed to true
		if signal == True:
			# split the line apart at the columns
			lls = line.split()
			# put the numbers into our empty lists
			depth.append(float(lls[1]))
			temp.append(float(lls[2]))
		# check if we are at the end of the header
		if '*END OF HEADER' in line and signal is False:
			signal = True

# print out the data
print(temp)
print(depth)

# make a simple plot
fig = plt.figure()
plt.plot(temp,depth)
plt.xlabel('Temperature (˚C)')
plt.ylabel('Pressure (dbar)')
plt.gca().invert_yaxis() # this reverses y axis
plt.show()
