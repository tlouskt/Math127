import numpy as np
from MRCFile import MRCFile
from sim_image import *
import matplotlib.pyplot as plt
import matplotlib.image
import sys


# Cooking up our own set of rotation matrices
# For more information see 
# https://en.wikipedia.org/wiki/Rotation_matrix


"""
Cooks up "evenly spaced" rotation matrices that rotate 
the yz plane about the x direction

Args: 
    n: number of rotation matrices 
     
Returns:
    list of rotation matrices
"""

def rotate_x(n):
	# range of angle is from 0 to pi
	step = np.pi/n
	# + 1e-5 hacky fix to make range inclusive
	thetas = np.arange(0,np.pi + 1e-5 ,step) 
	# TODO fix for efficieny purposes
	matrices = []
	for i in thetas:
		new_matrix = np.array([[ 1, 0, 0],
							   [ 0 , np.cos(i), -np.sin(i)],
							   [ 0 , np.sin(i), np.cos(i)]
							   ])
		matrices[i] = new_matrix
	return matrices

"""
Cooks up "evenly spaceed" rotation matrices that rotate 
the xz plane about the y direction

Args: 
    n: number of rotation matrices 
     
Returns:
    np array of rotation matrices
"""
def rotate_y(n):
	# range of angle is from 0 to pi
	step = np.pi/n
	# + 1e-5 hacky fix to make range inclusive
	thetas = np.arange(0,np.pi + 1e-5 ,step) 
	# TODO fix for efficieny purposes
	matrices = []
	for i in thetas:
		new_matrix = np.array([[ np.cos(i), 0, np.sin(i)],
							   [ 0 , 1, 0],
							   [ -np.sin(i) , 0, np.cos(i)]
							   ])
		matrices[i] = new_matrix
	return matrices

"""
Cooks up "evenly spaceed" rotation matrices that rotate 
the xz plane about the y direction

Args: 
    n: number of rotation matrices 
     
Returns:
    np array of rotation matrices
"""
def rotate_y(n):
	# range of angle is from 0 to pi
	step = np.pi/n
	# + 1e-5 hacky fix to make range inclusive
	thetas = np.arange(0,np.pi + 1e-5 ,step) 
	# TODO fix for efficieny purposes
	matrices = []
	for i in thetas:
		new_matrix = np.array([[ np.cos(i), -np.sin(i), 0],
							   [ np.sin(i) , np.cos(i), 0],
							   [ 0 , 0, 1]
							   ])
		matrices[i] = new_matrix
	return matrices

























































