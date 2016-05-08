import numpy as np
from estimate_orientations import *

im1 = np.array( [[1,2,3,4,5,6,7,8,9,1],
                  [1,2,3,4,5,6,7,8,1,10],
                  [1,2,3,4,5,6,7,1,9,10],
                  [1,2,3,4,5,6,1,8,9,10],
                  [1,2,3,4,5,1,7,8,9,10],
                  [1,2,3,4,1,6,7,8,9,10],
                  [1,2,3,1,5,6,7,8,9,10],
                  [1,2,1,4,5,6,7,8,9,10],
                  [1,1,3,4,5,6,7,8,9,10],
                  [1,2,3,4,5,6,7,8,9,10]
                ])


im2 = np.array( [[10,9,8,7,6,5,4,3,2,1],
                  [9,8,7,6,5,4,3,2,1,1],
                  [9,8,7,6,5,4,3,1,2,1],
                  [9,8,7,6,5,4,1,3,2,1],
                  [9,8,7,6,5,1,4,3,2,1],
                  [9,8,7,6,1,5,4,3,2,1],
                  [9,8,7,1,6,5,4,3,2,1],
                  [9,8,1,7,6,5,4,3,2,1],
                  [9,1,8,7,6,5,4,3,2,1],
                  [1,2,3,4,5,6,7,8,9,10]
                ])
im1.shape



im1_interpolater = make_interpolator(im1)
im2_interpolater = make_interpolator(im2)
	
common_line(im1,im2, 30, 30)
















