# -*- encoding: utf-8 -*-

# BSD 2-Clause License
# Copyright (c) 2016, Roberto Souza and collaborators
# All rights reserved.

# Module morph_tree_alpha

from .build_max_tree import build_max_tree
from .morph_tree_alpha_methods import getImage, clone, recConnectedComponent, compact,\
				     areaOpen, bbox, computeRR, \
                                     getChildren, getAncestors, \
                                     getDescendants, getSubBranches, prune, contractDR, computeHistogram,\
                                     getBifAncestor, computeNodeGrayAvg, computeNodeGrayVar, \
                                     computeEccentricity, computeNodeCentroid
    
                                     

from .morph_tree_alpha_aux import get_children_aux_c, get_ancestors_aux_c, get_descendants_aux_c, \
     get_sub_branches_aux_c,prune_aux_c, contract_dr_aux_c, update_nchild_aux_c, remove_node_array_lines_c,\
     rec_connected_component_2d_c, rec_connected_component_3d_c, get_image_aux_2d_c, get_image_aux_3d_c, \
     lut_node_index_3d_c, lut_node_index_2d_c ,get_bif_ancestor_aux_c, compute_node_gray_avg_aux_c, \
     compute_node_gray_var_aux_c, compute_eccentricity_aux_c, compute_hist_aux_c

from ._aux import se2off

class MorphTreeAlpha:
    """
    This class builds the morphological tree corresponding to a 8-bit
    grayscale image. The morphological trees available for
    construction are 2D and 3D max-trees, and 2D tree of shapes.
    **Input:**
    img -> uint8 image, may be either 2D or 3D. When working with 1D
    signals use a 2D array with the shape 1xW.
    Bc -> Boolean array corresponding to the connectivity to be used
    during the tree construction. The convention is that coordinates
    (0,0) or (0,0,0) are in the center of the array.
    option-> string, it may either be 'max_tree' or 'tree_of_shapes'
    """

    getImage = getImage
    clone = clone
    recConnectedComponent = recConnectedComponent
    computeRR = computeRR
    areaOpen = areaOpen
    bbox = bbox
    compact = compact
    getChildren = getChildren
    getAncestors = getAncestors
    getDescendants = getDescendants
    getSubBranches = getSubBranches
    prune = prune
    contractDR = contractDR
    computeHistogram = computeHistogram
    computeNodeCentroid = computeNodeCentroid
    
    # New 01/27/2016
    getBifAncestor = getBifAncestor
    computeNodeGrayAvg = computeNodeGrayAvg
    computeNodeGrayVar = computeNodeGrayVar
    computeEccentricity = computeEccentricity
    


    def __init__(self,img = None, Bc = None,option = 'max_tree'):
        if option == 'max_tree':
            _,_,self.node_array,self.node_index, = build_max_tree(img,Bc, option = 1)
        elif option == 'tree_of_shapes':
            print("Error: Option not implemented yet")
        else:
            print("Error: invalid option")
            return
        self.Bc = Bc
        self.shape = img.shape
        self._children_list = []
        self._cum_children_hist = []
        self._children_updated = False
        self._sb = []
        self._cum_sb_hist = []
        self._sb_updated = False
        self.off = se2off(Bc)
        self.ftype = img.dtype

        self.get_children_aux = get_children_aux_c
        self.get_ancestors_aux = get_ancestors_aux_c
        self.get_descendants_aux = get_descendants_aux_c
        self.get_sub_branches_aux = get_sub_branches_aux_c
        self.prune_aux = prune_aux_c
        self.contract_dr_aux = contract_dr_aux_c
        self.update_nchild_aux = update_nchild_aux_c
        self.remove_node_array_lines_aux = remove_node_array_lines_c
        self.rec_connected_component_2d_aux = rec_connected_component_2d_c
        self.rec_connected_component_3d_aux = rec_connected_component_3d_c
        self.get_image_aux_2d_aux = get_image_aux_2d_c
        self.get_image_aux_3d_aux = get_image_aux_3d_c
        self.lut_node_index_3d_aux = lut_node_index_3d_c
        self.lut_node_index_2d_aux = lut_node_index_2d_c

        self.get_bif_ancestor_aux = get_bif_ancestor_aux_c
        self.compute_node_gray_avg_aux = compute_node_gray_avg_aux_c
        self.compute_node_gray_var_aux = compute_node_gray_var_aux_c
        self.compute_eccentricity_aux = compute_eccentricity_aux_c
        self.compute_hist_aux = compute_hist_aux_c

