# -*- encoding: utf-8 -*-

# BSD 2-Clause License
# Copyright (c) 2016, Roberto Souza and collaborators
# All rights reserved.

import numpy as np
import os

def computeHeight(self):
    """
    This method returns the height attribute of the max-tree nodes.
    """
    parent = self.node_array[0,:]
    level  = self.node_array[2,:]
    height = np.where(self.node_array[1,:] == 0, 1, 0)
    height = height.astype(np.int32)
    delta = (level - level[parent]).astype(np.int32)
    self.compute_height_aux(parent,delta,height)
    return height



def computeVolume(self):
    """
    This method returns the volume attribute of the max-tree nodes.
    """
    parent = self.node_array[0,:]
    level  = self.node_array[2,:]
    area   = self.node_array[3,:]
    volume = area.copy()
    delta = (level - level[parent]).astype(np.int32)
    self.compute_volume_aux(parent,delta,area,volume)
    return volume

def computeExtinctionValues(self,attrib_orig, opt = "area"):
    """
    This method computes the "hegiht", "area", "volume" or "bb" extinction
    values of the Max-Tree leaves. It receives the array attrib containing
    the values to be analysed and a string with the attribute option, since
    for "height" and "volume" attributes the hidden layers of the composite
    nodes have to be considered.
    """

    attrib = attrib_orig.copy()
    parent = self.node_array[0,:]
    nchild = self.node_array[1,:]
    h = self.node_array[2,:]
    area = self.node_array[3,:]
    nlevels = h - h[parent]
    composite_nodes = nlevels > 1
    if opt == "area":
        pass
    elif opt == "height":
        attrib[composite_nodes] = attrib[composite_nodes] + \
                                  (nlevels[composite_nodes] - 1)
    elif opt == "volume":
        attrib[composite_nodes] = attrib[composite_nodes] +\
                                  (nlevels[composite_nodes] - 1)\
                                  *area[composite_nodes]
    else:
        print("Invalid Option")
        return

    ichmax = np.zeros_like(parent)
    achmax = np.zeros_like(parent)
    ext_values = np.zeros_like(parent)
    leaves = (np.nonzero(nchild == 0)[0]).astype(np.int32)
    self.compute_extinction_values_aux(parent, attrib, leaves, ichmax,\
                                       achmax, ext_values)
    return ext_values

def computeStabilityMeasure(self, delta = 5):
  """
  This method computes the MSER stability measure of the Max-Tree nodes. The parameter delta
  is the number of thresholds to be considered in the stability computation.
  """

  h = self.node_array[2,:]
  parent = self.node_array[0,:]
  area = self.node_array[3,:]
  nlevels =  (h - h[parent]).astype(np.int32)
  nlevels[0] = 1
  hmin = int(h.min())
  stability_measure = np.ones(self.node_array.shape[1], dtype = np.float)
  nodes_list = (np.nonzero( (h >= (hmin + delta)))[0]).astype(np.int32)

  self.compute_stability_measure_aux(parent, h, area, nlevels, nodes_list, stability_measure, delta, hmin)
  return stability_measure

def extinctionFilter(self,ext,n):
    """
    This method implements the Extinction Filter. It keeps the n most
    relevant extrema according to the extinction values ext.
    """

    ii = (np.argsort(ext)[::-1][:n]).astype(np.int32)
    to_remove = np.ones((self.node_array.shape[1],),dtype = np.int32)
    self.extinction_filter_aux(to_remove,ii,self.node_array[0,:])
    self.prune(to_remove.astype(bool))
    return self

def getSignature(self,attrib, start, end = 0, cte = 0):
    """
    This method returns a tuple containing the gray-levels and the
    attribute signature. Composite nodes are considered.
    cte:
    0 -> shape signature
    1 -> volume signature
    """
    par = self.node_array[0,:]
    h = self.node_array[2,:]
    area = self.node_array[3,:]
    attrib = attrib.astype(np.int32)
    signature = self.get_signature_aux(par, h, area, attrib, int(start), int(end), int(cte))
    levels = np.arange(h[end], h[start] + 1, dtype = np.int32)
    return levels, signature

def hmax(self, h, Height =[]):
    """
    This method implemnets the hmax filter
    """
    h = h + 1
    if Height == []:
        child_height = self.computeHeight()
    else:
        child_height = Height

    level = self.node_array[2,:]
    parent = self.node_array[0,:]
    total_height = level - level[parent] + child_height
    self.prune(total_height < h)
    child_height = child_height[total_height >= h]
    self.node_array[2,child_height < h] -= (h - child_height[child_height < h])
    return self

def vmax(self, vol,V = None):
    """
    This method implemnets the vmax filter
    """
    vol = vol + 1
    area = self.node_array[3,:]
    level = self.node_array[2,:]
    parent = self.node_array[0,:]
    if V == None:
        child_volume = self.computeVolume() - area
    else:
        child_volume = V - area

    total_volume = child_volume + (level - level[parent])*area
    self.prune(total_volume < vol)
    area = area[total_volume >= vol]
    child_volume = child_volume[total_volume >= vol]
    self.node_array[2,child_volume < vol] -= (vol - child_volume[child_volume < vol]) // area[child_volume < vol]
    return self



#Implementation of the maximal max-tree simplification filter proposed in:
# R. Souza, L. Ríttner, R. Machado and R. Lotufo, "Maximal Max-tree
# Simplification," Proceedings of the 22nd International Conference on Pattern
#  Recognition, Stockholm, Sweden, August 2014.

def mmsMSER(self,stability_measure):
    if not self._sb_updated:
        self.getSubBranches()  # List of sub-branches

    to_keep = np.zeros(self._cum_sb_hist.size, dtype = np.int32)
    self.mms_mser_aux(stability_measure, to_keep, self._sb,self._cum_sb_hist)
    bool_tokeep = np.zeros(self.node_array.shape[1],dtype = bool)
    bool_tokeep[to_keep] = True
    self.contractDR(bool_tokeep)
    return

def mmsT(self, t = 0.5):
    if not self._sb_updated:
        self.getSubBranches()  # List of sub-branches
    to_keep = np.zeros(self._cum_sb_hist.size, dtype = np.int32)

    new_h = np.zeros(self._cum_sb_hist.size, dtype = np.int32)
    h = self.node_array[2,:]
    parent = self.node_array[0,:]
    nlevels =  (h - h[parent]).astype(np.int32)
    nlevels[0] = 1

    self.mms_t_aux(t, nlevels, h, to_keep, new_h,self._sb,self._cum_sb_hist )
    h[to_keep] = new_h
    bool_tokeep = np.zeros(self.node_array.shape[1],dtype = bool)
    bool_tokeep[to_keep] = True
    self.contractDR(bool_tokeep)
    return

def areaDifference(self,AD):
    """
    Implementation of the area difference filter proposed by Tavares et al.
    """    
    n = self.node_array.shape[-1]
    parent = self.node_array[0, :] 
    area = self.node_array[3, :]
    to_keep = np.zeros(n, dtype = np.int32)
    self.area_difference_aux(AD,parent,area,to_keep)
    self.contractDR(to_keep>0)
    return self


def progAreaDifference(self, AD):
    parent = self.node_array[0, :] 
    area = self.node_array[3, :]
    to_keep = np.zeros(self.node_array.shape[-1], np.int32)
    visited = np.zeros_like(to_keep)
    leaves = (np.nonzero(self.node_array[1,:] == 0)[0]).astype(np.int32)
    self.prog_area_difference_aux(AD,parent,area,to_keep,visited,leaves)              
    self.contractDR(to_keep>0)
    return self



