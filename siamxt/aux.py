# -*- encoding: utf-8 -*-

# BSD 2-Clause License
# Copyright (c) 2016, Roberto Souza and collaborators
# All rights reserved.

# Module draw_1D_image
import numpy as np


#This function implements the algorithm described in:
# R. Souza, L. Rittner, R. Machado, R. Lotufo: A comparison between extinction
# filters and attribute filters. In: International Symposium on Mathematical
# Morphology, 2015, Reykjavik.
def extrema2attribute(n, ext):
    """
    This method computes the attribute parameter to be used in the attribute
    filter that tries to preserve n extrema in the image. If it is not possible  
    to preserve n extrema, it will give preserve the closest value from n from
    below. 
    """
    
    ext = ext[ext!=0] # Non-zero extinction values
    temp = np.unique(ext) # Returns non-repeated elements sorted
    max_ext = temp[-1]
    bins = np.zeros(len(temp)+2, dtype = np.int32)
    bins[1:-1] = temp
    bins[-1] = max_ext + 1
    hist, bins = np.histogram(ext.flatten(),bins = bins)
    x = bins[:-1]
    y = (hist.sum() - np.cumsum(hist))
    index = np.where(y >= n)[0][-1]
    attr_value =  x[index]
    new_n = y[index]
    return attr_value,new_n

def se2off(Bc):
    """
    This method returns the array of offsets corresponding to the structuring
    element Bc.
    """
    Bc2 = Bc.copy()
    center = np.array(Bc.shape)//2
    Bc2[tuple(center)] = 0
    off = np.transpose(Bc2.nonzero()) - center
    return np.ascontiguousarray(off, dtype = np.int32)


