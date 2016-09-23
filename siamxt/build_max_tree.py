# -*- encoding: utf-8 -*-

# BSD 2-Clause License
# Copyright (c) 2016, Roberto Souza and collaborators
# All rights reserved.

from aux import se2off
import numpy as np
import max_tree_c_01

# Max-tree construction
def build_max_tree(f, Bc, option = 0):

    ndim = f.ndim
    off = se2off(Bc) # Array of offsets that defines the structuring element

    parent = np.empty(f.size, dtype = np.int32)
    parent[:] = -1 # parent array

    zpar = np.empty(f.size, dtype = np.int32) #auxiliary array to store level roots

    ftype = f.dtype
    if (ftype == np.uint8):
       fu16 = f.astype(np.uint16)
    else:
        fu16 = f    

    flat_img = fu16.ravel()
    MAX = flat_img.max()
    S_rev = max_tree_c_01.counting_sort_c(int(MAX),flat_img) #image sorting

    #Max-tree construction	
    if ndim == 2:
        H,W = f.shape
        max_tree_c_01.union_find2d_c(H,W,off,parent,zpar,S_rev,flat_img)
    elif ndim == 3:
        L,M,N = f.shape
        max_tree_c_01.union_find3d_c(L,M,N,off,parent,zpar,S_rev,flat_img)
    else:
        print "Invalid option"
        return

    # Tree canocalization
    max_tree_c_01.canonicalize_c(flat_img,parent,S_rev)

	
    if option == 0:
        return parent,S_rev # returns usual max-tree representation
    else:
        node_index = np.empty(f.shape, dtype = np.int32)
        node_index[:] = -1
        if ndim == 2: # node array/node index representation
            node_array = max_tree_c_01.computeNodeArray2d_c(parent,flat_img,S_rev,node_index)
        else:
            node_array = max_tree_c_01.computeNodeArray3d_c(parent,flat_img,S_rev,node_index)

        node_array = node_array.T.copy()
        return parent,S_rev,node_array,node_index


