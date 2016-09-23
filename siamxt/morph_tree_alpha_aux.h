//BSD 2-Clause License
//Copyright (c) 2016, Roberto Souza and collaborators
//All rights reserved. 

void get_descendants_aux_c(int node, int , int *, int , int *, int **, int *);

void get_ancestors_aux_c(int node, int , int *,int **, int *);

void get_children_aux_c(int ,  int *,int ,  int *, int **, int *);

void get_sub_branches_aux_c(int , int *, int , int *,int , int *,int , int *,int **, int *);

void contract_dr_aux_c(int,  int *,int, int *, int,int  *);

void update_nchild_aux_c(int,  int *,int, int *);

void prune_aux_c(int , int *, int , int *, int , int *, int , int *);


void get_image_aux_2d_c(int,  int *,int,int,int *,int,int,unsigned short *);
    
void get_image_aux_3d_c(int, int *,int ,int ,int ,int *,int,int , int , unsigned short *);

void rec_connected_component_2d_c(int , int , int ,int ,int *, int ,int , unsigned char *,int ,int , int *);  

void rec_connected_component_3d_c(int , int , int ,int , int , int *, int ,int , int , unsigned char *,int ,int , int *); 

void lut_node_index_2d_c(int,  int *,int ,int,int *);

void lut_node_index_3d_c(int ,  int *,int ,int ,int , int *);

void remove_node_array_lines_c(int , int *,int ,int ,int *,int ,int ,int *);

int get_bif_ancestor_aux_c(int , int , int * ,int , int *);

void compute_hist_aux_c(int , int *, int , int , int *);

void compute_node_gray_avg_aux_c(int , int *, int , int *, int ,int *,int , double *);

void compute_node_gray_var_aux_c(int , int *, int , int *, int , int *,int , double *);

void compute_eccentricity_aux_c(int , double *, int , double *, int , double *, int , int *, int , int , int *);
