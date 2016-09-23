/*
BSD 2-Clause License
Copyright (c) 2016, Roberto Souza and collaborators
All rights reserved. */
%module morph_tree_alpha_aux
%{
#define SWIG_FILE_WITH_INIT
#undef NO_IMPORT_ARRAY
%}

%include "typemaps.i"
%include "numpy.i"

%init %{
import_array();
%}

%{

void get_descendants_aux_c(int node, int , int *, int , int *, int **, int *);

void get_ancestors_aux_c(int node, int , int *,int **, int *);

void get_children_aux_c(int ,  int *,int ,  int *, int **, int *);

void get_sub_branches_aux_c(int , int *, int , int *,
                            int , int *,int , int *,
                            int **, int *);

void contract_dr_aux_c(int,  int *,int, int *, int,int  *);

void update_nchild_aux_c(int,  int *,int, int *);

void prune_aux_c(int , int *, int , int *, int ,
                 int *, int , int *);

void get_image_aux_2d_c(int,  int *,int,int,int *,int,int,unsigned short *);
    
void get_image_aux_3d_c(int, int *,int ,int ,int ,int *,int,int , int , unsigned short *);

void rec_connected_component_2d_c(int , int , int ,int ,int *, int ,int , unsigned char *,int ,int , int *);  

void rec_connected_component_3d_c(int , int , int ,int , int , int *, int ,int , int , unsigned char *,int ,int , int *);  

void lut_node_index_2d_c(int,  int *,int ,int,int *);

void lut_node_index_3d_c(int ,  int *,int ,int ,int , int *);

void remove_node_array_lines_c(int , int *,int ,int ,int *,int ,int ,int *);
    
int get_bif_ancestor_aux_c(int , int , int *,int , int *);
  
void compute_hist_aux_c(int , int *, int , int , int *);
    
    
void compute_node_gray_avg_aux_c(int , int *,int , int *,int, int *,int , double *);
    
    
void compute_node_gray_var_aux_c(int , int *, int , int *,int , int *, int , double *);
    
void compute_eccentricity_aux_c(int , double *, int , double *, int , double *, int , int *, int , int , int *);
    
    
    


%}

%feature("autodoc", 1);
void get_descendants_aux_c(int node, int DIM1, int *IN_ARRAY1, int DIM1, int *IN_ARRAY1, int **ARGOUT_ARRAY1, int *DIM1);

void get_ancestors_aux_c(int node, int DIM1, int *INPLACE_ARRAY1,int **ARGOUT_ARRAY1, int *DIM1);

void get_children_aux_c(int DIM1,  int *IN_ARRAY1,int DIM1,  int *INPLACE_ARRAY1, int **ARGOUT_ARRAY1, int *DIM1);

void get_sub_branches_aux_c(int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1,
                            int DIM1, int *INPLACE_ARRAY1,int DIM1, int *INPLACE_ARRAY1,
                            int **ARGOUT_ARRAY1, int *DIM1);

void contract_dr_aux_c(int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1,
                           int DIM1,int *INPLACE_ARRAY1);

void update_nchild_aux_c(int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1);

void prune_aux_c(int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1, int DIM1,
                 int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1);

void get_image_aux_2d_c(int DIM1,  int *INPLACE_ARRAY1,int DIM1,int DIM2,int *INPLACE_ARRAY2,
                        int DIM1,int DIM2,unsigned short *INPLACE_ARRAY2);
    
void get_image_aux_3d_c(int DIM1,  int *INPLACE_ARRAY1,int DIM1,int DIM2,int DIM3,int *INPLACE_ARRAY3,
                        int DIM1,int DIM2, int DIM3, unsigned short *INPLACE_ARRAY3);

void rec_connected_component_2d_c(int node, int seed, int DIM1,int DIM2,int *INPLACE_ARRAY2, int DIM1,int DIM2, 
                                  unsigned char *INPLACE_ARRAY2,int DIM1,int DIM2, int *INPLACE_ARRAY2);  

       
void rec_connected_component_3d_c(int node, int seed, int DIM1,int DIM2, int DIM3, int *INPLACE_ARRAY3, int DIM1,
                                  int DIM2, int DIM3, unsigned char *INPLACE_ARRAY3,int DIM1,int DIM2, int *INPLACE_ARRAY2);  

void lut_node_index_2d_c(int DIM1,  int *INPLACE_ARRAY1,int DIM1,int DIM2,int *INPLACE_ARRAY2);

void lut_node_index_3d_c(int DIM1,  int *INPLACE_ARRAY1,int DIM1,int DIM2,int DIM3, int *INPLACE_ARRAY3);

void remove_node_array_lines_c(int DIM1, int *INPLACE_ARRAY1,int DIM1,int DIM2,int *INPLACE_ARRAY2,int DIM1,int DIM2,int *INPLACE_ARRAY2);

int get_bif_ancestor_aux_c(int node, int DIM1, int *INPLACE_ARRAY1,int DIM1, int *INPLACE_ARRAY1);

void compute_hist_aux_c(int DIM1, int *INPLACE_ARRAY1, int DIM1, int DIM2, int *INPLACE_ARRAY2);


void compute_node_gray_avg_aux_c(int DIM1, int *INPLACE_ARRAY1,int DIM1, int *INPLACE_ARRAY1,
                                 int DIM1, int *INPLACE_ARRAY1,int DIM1, double *INPLACE_ARRAY1);


void compute_node_gray_var_aux_c(int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1,
                                 int DIM1, int *INPLACE_ARRAY1, int DIM1, double *INPLACE_ARRAY1
                                 );

void compute_eccentricity_aux_c(int DIM1, double *INPLACE_ARRAY1, int DIM1, double *INPLACE_ARRAY1,
                                int DIM1, double *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1,
                                int DIM1, int DIM2, int *INPLACE_ARRAY2);






