# -*- encoding: utf-8 -*-

# BSD 2-Clause License
# Copyright (c) 2016, Roberto Souza and collaborators
# All rights reserved.


# Module max_tree_alpha

from .max_tree_alpha_methods import vmax, hmax, computeHeight, computeVolume, computeStabilityMeasure,\
                                   computeExtinctionValues, getSignature, extinctionFilter, mmsT, mmsMSER, areaDifference, progAreaDifference 
                                   

from .max_tree_alpha_aux import compute_height_aux_c, compute_volume_aux_c, compute_stability_measure_aux_c, \
                               compute_extinction_values_aux_c, get_signature_aux_c, extinction_filter_aux_c, \
                               mms_t_aux_c, mms_mser_aux_c, \
area_difference_aux_c, prog_area_difference_aux_c

  

from .morph_tree_alpha import MorphTreeAlpha

                                     
class MaxTreeAlpha(MorphTreeAlpha):
  """
  This class builds the max-tree corresponding to a 8-bit grayscale image.
  Many methods,to extract attributes and filter the max-tree are available.
  **Input:**
  img -> uint8 image, may be either 2D or 3D. When working with 1D signals use
  a 2D array with the shape 1xW.
  Bc -> Boolean array corresponding to the connectivity to be used during the
  tree construction. The convention is that coordinates (0,0) or (0,0,0) are
  in the center of the array.
  """

  hmax = hmax
  vmax = vmax
  computeHeight = computeHeight
  computeVolume = computeVolume
  computeStabilityMeasure = computeStabilityMeasure
  computeExtinctionValues = computeExtinctionValues
  getSignature = getSignature
  extinctionFilter = extinctionFilter
  mmsT = mmsT
  mmsMSER = mmsMSER
  areaDifference = areaDifference
  progAreaDifference = progAreaDifference

  def __init__(self, img, Bc):
    MorphTreeAlpha.__init__(self,img, Bc,option = 'max_tree')

    self.compute_height_aux = compute_height_aux_c
    self.compute_volume_aux = compute_volume_aux_c
    self.compute_stability_measure_aux = compute_stability_measure_aux_c
    self.compute_extinction_values_aux = compute_extinction_values_aux_c
    self.get_signature_aux = get_signature_aux_c
    self.extinction_filter_aux = extinction_filter_aux_c
    self.mms_t_aux = mms_t_aux_c
    self.mms_mser_aux = mms_mser_aux_c
    self.area_difference_aux = area_difference_aux_c
    self.prog_area_difference_aux = prog_area_difference_aux_c
    
