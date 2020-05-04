"""
This is code for the numpy and argparse assignment for effective computing (OCN506A), Week 5-6.
Goals:

-Make some arrays in numpy and try 5 methods of your choice on them  (SM notes: dimension, shape, index, transpose/math, mean, stdev, max, index of max)
-Have the code save some output to your output directory ([my_code]_output/) as a pickle file, and have it read that file back in.  DONE!
-Have the code make the output directory if needed. (I did this I think)
-Use argparse to add command-line arguments to your code, allowing the user to make some choice about what happens.
    -I did this at dinner time, thinking about eating potatoes


Suggestions of things to do from arrays code: 
Figure out how to find the mean, standard deviation, max, and index of
the max of an array.

Susanna's notes: I'm eventually trying to make a pretty basic 1D model
"""
#imports
import numpy as np
import sys, os
import matplotlib.pyplot as plt
import pickle
import argparse

#local imports
sys.path.append(os.path.abspath('./shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# make sure the output directory exists
this_dir = os.path.abspath('.').split('/')[-1]
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../' + this_parent + '_output/'
print('Creating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)

#Playin with arrays

distance = np.random.randn(1, 6)
print(distance)

time = np.random.randn(1, 6)
print(time)

dist_array = np.array(distance)
time_array = np.array(time)
rate_array = dist_array/time_array
print('distance')
print(dist_array)  
print('time')  
print(time_array)
print('rate')
print(rate_array)

print('data type')
print(dist_array.dtype)

print('dimension of time array')
print(time_array.ndim)

print('shape of rate array') 
print(rate_array.shape)

print('4th value in distance array')
print (dist_array[0,3])

print('slice of time')
slice_of_time = time_array[0,2:5]
print(slice_of_time)

print('mean of rate')
print(rate_array.mean())

print('standard deviation of rate')
print(rate_array.std())

print('maximum rate')
print(rate_array.max())

print('location of maximum rate')
print(np.argmax(rate_array))

# Pickle the rate file
out_rate = out_dir + 'pickled_rate_array.p'
pickle.dump(rate_array, open(out_rate, 'wb')) # 'wb' is for write binary

# read the rate array back in
in_rate = pickle.load(open(out_rate, 'rb')) # 'rb is for read binary

print('pickled rate (is less delicious than pickled onions:')
print(in_rate)

#Argparse

def boolean_string(s):
    # this function helps with getting Boolean input
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'True' # note use of ==

# create the parser object
parser = argparse.ArgumentParser()

# NOTE: argparse will throw an error if:
#     - a flag is given with no value
#     - the value does not match the type
# and if a flag is not given it will be filled with the default.
parser.add_argument('-num', '--num_string', default='17', type=str)
parser.add_argument('-var', '--pot_string', default='Idaho', type=str)
parser.add_argument('-cook', '--cook_string', default='mashed', type=str)
parser.add_argument('-little', '--integer_full', default=1190, type=int)
parser.add_argument('-big', '--float_full', default=0.82, type=float)

# Note that you assign a short name and a long name to each argument.
# You can use either when you call the program, but you have to use the
# long name when getting the values back from "args".

# get the arguments
args = parser.parse_args()

# output
print('\nYour potato preference is ' + args.num_string +' '+ args.pot_string + ' '+ args.cook_string + ' potatoes')

print('This is how full you will be if you eat all of them:')
print(args.integer_full+args.float_full)