# -*- encoding: utf-8 -*-

# BSD 2-Clause License
# Copyright (c) 2016, Roberto Souza and collaborators
# All rights reserved.

# Module morph_tree_bbox

import copy
import numpy as np
import os

def bbox(self, dx, dy, dz = 0):
    """
    Contracts all nodes with bounding box less than 'dx' by 'dy'
    """
    ddx = self.node_array[7,:] - self.node_array[6,:] + 1
    ddy = self.node_array[10,:] - self.node_array[9,:] + 1
    if self.node_index.ndim == 2:
        self.prune((ddx < dx) & (ddy < dy))
    else:
        ddz = self.node_array[13,:] - self.node_array[12,:] + 1
        self.prune((ddx < dx) & (ddy < dy) & (ddz < dz))
    return self

def clone(self):
    """
    This method returns a hard copy of the Max-Tree object.
    """
    mxt = copy.deepcopy(self)
    return mxt

def compact(self, to_remove, lut):
    """
    This method removes the nodes to_remove of self.node_array and adjust 
    the pointers in self.node_array and self.node_index. to_remove is a boolean
    array with 1 for the nodes that need to be removed. 
    """
    self._children_updated = False 
    self._sb_updated = False 
    N = self.node_array.shape[1]
    parent = self.node_array[0,:]
    index_fix = to_remove.astype(np.int32).cumsum()
    lut = (lut - index_fix[lut]).astype(np.int32)
    self.node_array[0,:] = lut[parent]

    if self.node_index.ndim == 3:
        self.lut_node_index_3d_aux(lut,self.node_index)
    else:    
        self.lut_node_index_2d_aux(lut,self.node_index)
        
    nodes_kept = np.nonzero(~to_remove)[0].astype(np.int32)
    new_node_array = np.empty((self.node_array.shape[0],nodes_kept.size), dtype = np.int32)    
    self.remove_node_array_lines_aux(nodes_kept,new_node_array,self.node_array)
    self.node_array = new_node_array
    return self



def areaOpen(self, n):
    """
    Contracts all the nodes with area less than 'area'
    """
    area = self.node_array[3,:]
    self.prune(area <= n)
    return self

def getImage(self):
    """
    This method returns the image corresponding to the tree.
    """
    out_img = np.empty(self.node_index.shape, dtype = np.uint16)
    if self.node_index.ndim == 3:
        self.get_image_aux_3d_aux(self.node_array[2],self.node_index,out_img)
    else:
        self.get_image_aux_2d_aux(self.node_array[2],self.node_index,out_img)
    return out_img.astype(self.ftype)



def computeRR(self):
    """
    Compute the rectangularity ratio (RR) of the max-tree nodes. RR is defined as the 
    area (volume) of a connected component divided by the area (volume) of its bounding-box. 
    """
    xmin,xmax = self.node_array[6,:], self.node_array[7,:] + 1
    ymin,ymax = self.node_array[9,:], self.node_array[10,:] + 1
    area = self.node_array[3,:]

    if self.node_index.ndim == 2:
        return 1.0*area/((xmax-xmin)*(ymax-ymin))
    else:
        zmin,zmax = self.node_array[12,:], self.node_array[13,:] + 1
        return 1.0*area/((xmax-xmin)*(ymax-ymin)*(zmax-zmin))


def prune(self, to_prune):
    """
    Contracts entire branches of the tree. This is the prunning procedure to be
    used for the non-increasing
    connected filters. If a node is indicated in to_prune, all its descendants
    should also be indicated in to_prune.
    """
    N = self.node_array.shape[1]
    lut = np.arange(N, dtype = np.int32)
    self.prune_aux(lut,to_prune.astype(np.int32), self.node_array[0,:], self.node_array[1,:])
    self.node_index = lut[self.node_index]
    self.compact(to_prune,lut)
    return self

# Filterin algorithm proposed in
# R. Souza, L. Rittner, R. Machado, R. Lotufo: An Array-based Node-Oriented Max-tree Representation.
# In: International Conference on Image Processing, 2015, Quebec.
def contractDR(self, to_keep):
    """
    Direct rule for contracting any max-tree nodes marked as False in 'to_keep'.
    This is a generic node removal procedure. Note that a node in the max-tree 
    can represent many level components.
    """
        
    to_keep[0] = True # The root can never be removed
    N = self.node_array.shape[1]
    lut = np.arange(N, dtype = np.int32)
    self.contract_dr_aux(to_keep.astype(np.int32),lut,self.node_array[0,:])
    self.node_index = lut[self.node_index]
    self.compact(~to_keep,lut)
    self.node_array[1,:] = 0
    self.update_nchild_aux(self.node_array[0,:],self.node_array[1,:])
    return self 

def getAncestors(self, node):
    """
    Returns the ancestors of a given node.
    """
    return self.get_ancestors_aux(node, self.node_array[0,:])


def getChildren(self,node = 0):
    """
    Returns the children list of a node.
    """
    if not self._children_updated:
        self._cum_children_hist = self.node_array[1,:].cumsum().astype(np.int32)
        par = self.node_array[0,:]
        self._children_list = self.get_children_aux(self._cum_children_hist.copy(),par)
        self._children_updated = True
    if node == 0:
        return self._children_list[0:self._cum_children_hist[node]]
    else:
        return self._children_list[self._cum_children_hist[node-1]:self._cum_children_hist[node]]



def generateGraph(self, keep = [],nodes_attr = [], LR = False,file_name = "graph" ):
    """
    Generates the max-tree graph. You can provide an array containing
    attributes to be displayed in the graph representation.
    """
    
    n_nodes = self.node_array.shape[1]
    h = self.node_array[2,:]
    if keep == []:
        keep = np.ones(n_nodes, dtype = bool)
    if nodes_attr == []:
        nodes_attr = self.node_array[3,:]   # Default attribute is area

    G = gvgen.GvGen()
    G.styleAppend("remove", "style", "dashed")

    G.styleAppend("keep", "color","red")
    G.styleAppend("keep", "style","filled")
    items = {}


    for i in xrange(n_nodes):
        if keep[i]:
            items[i] = G.newItem('%d: %d [%d]' %(i,h[i],nodes_attr[i]))
            G.styleApply("keep", items[i])
        else:
            items[i] = G.newItem('%d: %d [%d]' %(i,h[i],nodes_attr[i]))
            G.styleApply("remove", items[i])
        pindex = self.node_array[0,i]
        if pindex != i:
            G.newLink(items[i], items[pindex])
    fd = StringIO.StringIO()
    G.dot(fd)
    dottext = fd.getvalue()

    if LR:
        dottext = dottext.replace("TB","RL")
        dottext = dottext.replace("{","{rankdir=LR")

    text_file = open(file_name + ".dot", "w")
    text_file.write(dottext)
    text_file.close()	
    try:
        os.system("/usr/bin/dot -Tpng %s.dot  > %s.png" %(file_name,file_name))

        os.remove(file_name + ".dot")
    except:
        print("Unable to save graph image. The method will return just the GraphViz code")
        os.remove(file_name + ".dot")
        return dottext
    return

def getDescendants(self, node):
    """
    Returns the descendants of a given node.
    """

    if self._children_updated == False:
        self.getChildren()
    if node == 0:
        return np.arange(self.node_array.shape[1], dtype = np.int32)
    elif self.node_array[1,node] == 0:
        return np.array([node],dtype = np.int32)
    else:
        return self.get_descendants_aux(node,self._children_list,self._cum_children_hist)


def getSubBranches(self,sb_index = 0):
    """
    Returns a sub-branch of the max-tree. Sub-branches were defined in
    R. Souza, L. Ríttner, R. Machado and R. Lotufo, "Maximal Max-tree Simplification," Proceedings of
    the 22nd International Conference on Pattern Recognition, Stockholm, Sweden, August 2014.
    """
    
    if self._sb_updated == False:
        visited = np.zeros(self.node_array.shape[1], dtype = np.int32)
        self._sb = np.zeros_like(visited)
        self._cum_sb_hist = self.get_sub_branches_aux(self.node_array[0,:],\
                                                      self.node_array[1,:],\
                                                      self._sb, visited)
        self._cum_sb_hist = np.concatenate((np.array([0],dtype = np.int32),\
                                           self._cum_sb_hist),axis = 0)
        self._sb_updated = True
    return self._sb[self._cum_sb_hist[sb_index]:self._cum_sb_hist[sb_index+1]]





def recConnectedComponent(self,node, bbonly = False):
    """
    This method returns a binary image corresponding to the
    connected component represented by node.
    bbonly -> Flag that indicates wether return the whole 
    image or just the connecetd component bounding-box.
    """
    seed = self.node_array[4,node]
    cc = np.zeros(self.node_index.shape, dtype = np.uint8)
        
    if self.node_index.ndim == 2:
       self.rec_connected_component_2d_aux(int(node),int(seed),self.node_index,cc,self.off)
    else:
       self.rec_connected_component_3d_aux(int(node),int(seed),self.node_index,cc,self.off)
        
    if not bbonly:
       return cc.astype(bool)

    xmin,xmax = self.node_array[6,node], self.node_array[7,node] + 1
    ymin,ymax = self.node_array[9,node], self.node_array[10,node] + 1
    if self.node_index.ndim == 2:
       indexes = (slice(xmin,xmax),slice(ymin,ymax))
    else:
       zmin,zmax = self.node_array[12,node], self.node_array[13,node] + 1
       indexes = (slice(xmin,xmax),slice(ymin,ymax),slice(zmin,zmax))
    return cc[indexes].astype(bool)




def computeHistogram(self,img,nbins = 256,wimg = [], normalize = True):
    """
    This method computes histograms of the max-tree nodes.
    Input:
       - img, 2d-array int32. Image used to compute the histograms.
       - wimg, 2d-array int32. Weight image used in the histogram computation.
       - nbins, int. Number of histogram bins. It starts in 0 and ends in nbins - 1.
       - normalize, bool. Flag indicating whether the histogram should be normalized or not. 
    Output
       - img, 2d-array float. Histogram array. Each line corresponds to a node histogram.
    """
    hist = np.zeros((self.node_array.shape[1],nbins), dtype = np.int32)    
    if wimg == []:
        hist[self.node_index,img] += 1
    else:
        hist[self.node_index,img] += wimg
        self.compute_hist_aux(self.node_array[0],hist)
    if normalize:
        hist = hist*1.0/hist.sum(axis = 1).reshape(-1,1) 
    return hist.astype(float)

def getBifAncestor(self, node):
    """
    This method returns the first ancestor immediately after a bifurcation of a given node.
    """
    
    return self.get_bif_ancestor_aux(node, self.node_array[0,:],self.node_array[1,:])

def computeNodeGrayAvg(self):
    """
    This method computes the gray-level average of
    the max-tree nodes.
    """
    gray_avg = np.zeros(self.node_array.shape[1], dtype = np.float)
    self.compute_node_gray_avg_aux(self.node_array[0,:],self.node_array[2,:],self.node_array[3,:].copy(),gray_avg)
    gray_avg = (gray_avg)/self.node_array[3,:]
    return gray_avg


def computeNodeGrayVar(self,gray_avg = [] ):
    """
    This method computes the gray-level standard deviation of
    the max-tree nodes.
    """
    if gray_avg == []:
        gray_avg = self.computeNodeGrayAvg()
                
    gray_var = np.zeros(self.node_array.shape[1], dtype = np.float)
    squared_gray_avg = np.zeros(self.node_array.shape[1], dtype = np.float)
    self.compute_node_gray_var_aux(self.node_array[0,:],self.node_array[2,:],self.node_array[3,:].copy(),squared_gray_avg)
    squared_gray_avg = squared_gray_avg/self.node_array[3,:]
    gray_var = (squared_gray_avg - gray_avg**2)
    return gray_var



def computeEccentricity(self):
    """
    This method computes the eccentricity
    of the max-tree nodes.
    """
        
    M20 = np.zeros((self.node_array.shape[1]),dtype = np.float)  
    M02 = np.zeros((self.node_array.shape[1]),dtype = np.float)  
    M11 = np.zeros((self.node_array.shape[1]),dtype = np.float) 
        
        
    par = self.node_array[0,:]
    self.compute_eccentricity_aux(M20,M02,M11,par,self.node_index)
       
    M00 = self.node_array[3,:]
    xc = 1.0*self.node_array[5,:]/M00
    yc = 1.0*self.node_array[8,:]/M00
    m20 = 1.0*M20 /M00 - xc**2
    m02 = 1.0*M02/M00 - yc**2
    m11 = 1.0*M11/M00 - xc*yc
    aux1 = (m20+m02)/2
    aux2 = np.sqrt((m20-m02)**2 + 4*m11*m11)/2
    L1 = aux1 - aux2
    L2 = aux1 + aux2
    ecc = L1/L2
    return L1,L2,ecc

def computeNodeCentroid(self):
    cent = np.zeros((self.node_array.shape[1],self.node_index.ndim))
    area = self.node_array[3,:]
    sumx = self.node_array[5,:]
    sumy = self.node_array[8,:]
    
    
    cent[:,0] = 1.0*sumx/area
    cent[:,1] = 1.0*sumy/area
    
    if self.node_index.ndim == 3:
        sumz = self.node_array[11,:]
        cent[:,2] = 1.0*sumz/area
    return cent
