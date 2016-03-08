from distance_based_trees import *
from ete3 import Tree
import numpy as np

from distance_based_trees import *
from ete3 import Tree
import numpy as np


M = np.array([[ 1.0        ,  1.04725288,  1.05048391,  1.13837828,  1.51596702, 1.12434297],
       		  [ 0        ,  1.0        ,  1.06679748,  1.14191811 ,  1.50062145, 1.12783337],
       		  [ 0        ,  0        ,  1.0      ,  1.14547051  ,  1.52632981, 1.14547051],
       		  [ 0        ,  0        ,  0        ,  1.0           ,  1.51082562, 1.1208647 ],
      		  [ 0        ,  0        ,  0        ,  0           ,  1.0         , 1.48550782],
              [ 0        ,  0        ,  0        ,  0           ,  0         , 0       ]])

ans = neighbor_joining(M,names = ["dnt", "ptb", "ptc", "ptd", "ctrl1", "ctrl5"])
print(ans)
ans.show()
# M = np.array([[0, 19.0,  27.0,  8.0, 33.0, 18.0 ,13.0],
# 					[0,    0,  31.0, 18.0, 36.0,  1.0, 13.0],
# 					[0,    0,   0,   26.0, 41.0, 32.0, 29.0],
# 					[0,    0,   0,      0, 31.0, 17.0, 14.0],
# 					[0,    0,   0,      0,    0, 35.0, 28.0],
# 					[0,    0,   0,      0,    0,    0, 12.0],
# 			        [0,    0,   0,      0,    0,    0,   0 ]
# 			  ])

# names = ['a', 'b', 'c', 'd','e','f','g']


# ans = neighbor_based_method(M,names, closest_neighbors, UPGMA_new_dist, split_dist)
# print(ans)

# M = np.array([[ 0        ,  0.04615385,  0.04923077,  0.12923077,  0.40307692, 0.11692308],
#        		  [ 0        ,  0         ,  0.06461538,  0.13230769,  0.39384615, 0.12      ],
#               [ 0        ,  0         ,  0         ,  0.13538462,  0.40923077, 0.13538462],
#        		  [ 0        ,  0         ,  0         ,  0         ,  0.4       , 0.11384615],
#        		  [ 0        ,  0         ,  0         ,  0         ,  0         , 0.38461538],
#               [ 0        ,  0         ,  0         ,  0         ,  0         , 0        ]])

# names = ['a', 'b', 'c', 'd','e','f']

# tree = UPGMA(M, names)
# tree.show()

# # a = UPGMA(np.array([[0, .45, .27, .53],
# # 					[0,   0, .40, .50],
# # 					[0,   0,   0, .62],
# # 					[0,   0,   0,  0]]),
# # 					['a', 'b', 'c', 'd'])
# # print(a)
# #
# # # http://www.southampton.ac.uk/~re1u06/teaching/upgma/upgma15.PNG
# #
# # b = UPGMA(np.array([[0, 19.0,  27.0,  8.0, 33.0, 18.0 ,13.0],
# # 					[0,    0,  31.0, 18.0, 36.0,  1.0, 13.0],
# # 					[0,    0,   0,   26.0, 41.0, 32.0, 29.0],
# # 					[0,    0,   0,      0, 31.0, 17.0, 14.0],
# # 					[0,    0,   0,      0,    0, 35.0, 28.0],
# # 					[0,    0,   0,      0,    0,    0, 12.0]]),
# # 					['a', 'b', 'c', 'd','e','f','g'])
# #
# # print(b)
# #
# #
# # a = neighbor_joining(np.array([[0, .45, .27, .53],
# # 					[0,   0, .40, .50],
# # 					[0,   0,   0, .62],
# # 					[0,   0,   0,  0]]),
# # 					['a', 'b', 'c', 'd'])
# # print(a)
# #
# # # http://www.southampton.ac.uk/~re1u06/teaching/upgma/upgma15.PNG
# #
# b = neighbor_joining(np.array([[0, 19.0,  27.0,  8.0, 33.0, 18.0 ,13.0],
# 					[0,    0,  31.0, 18.0, 36.0,  1.0, 13.0],
# 					[0,    0,   0,   26.0, 41.0, 32.0, 29.0],
# 					[0,    0,   0,      0, 31.0, 17.0, 14.0],
# 					[0,    0,   0,      0,    0, 35.0, 28.0],
# 					[0,    0,   0,      0,    0,    0, 12.0],
# 					[0,    0,   0,      0,    0,    0, 12.0]
# 					]),
# 					['a', 'b', 'c', 'd','e','f','g'])

# print(b)


