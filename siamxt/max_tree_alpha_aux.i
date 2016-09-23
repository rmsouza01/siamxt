/*
BSD 2-Clause License
Copyright (c) 2016, Roberto Souza and collaborators
All rights reserved. */

%module max_tree_alpha_aux
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

void compute_height_aux_c(int , int *, int , int *, int , int *);

void compute_volume_aux_c(int , int *, int , int *,
                      int , int *, int , int *);

void compute_extinction_values_aux_c(int , int *,
                                     int , int *,
                                     int , int *,
                                     int , int *,
                                     int , int *,
                                     int , int *);

void compute_stability_measure_aux_c(int , int *,int , int *,
                                     int , int *,int , int *,
                                     int , int *,int , double *,
                                     int delta, int hmin );

void get_signature_aux_c(int , int *, int , int *,
                         int , int *, int , int *,
                         int **, int *, int start, int end, int cte);

void extinction_filter_aux_c(int , int *, int , int *,
                             int ,  int *);

void mms_mser_aux_c(int , double *, int , int *,
                    int , int *, int , int *);

void mms_t_aux_c(double t, int , int *, int , int *, int ,
                 int *, int , int *, int , int *,
                 int , int *);

void area_difference_aux_c(int AD, int, int *,int, int *, int, int *);

void prog_area_difference_aux_c(int AD, int, int *,int, int *, int, int *, int, 
int *, int , int *);

%}

%feature("autodoc", 1);
void compute_height_aux_c(int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1);

void compute_volume_aux_c(int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1,
                      int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1);

void compute_extinction_values_aux_c(int DIM1, int *INPLACE_ARRAY1,
                                     int DIM1, int *INPLACE_ARRAY1,
                                     int DIM1, int *INPLACE_ARRAY1,
                                     int DIM1, int *INPLACE_ARRAY1,
                                     int DIM1, int *INPLACE_ARRAY1,
                                     int DIM1, int *INPLACE_ARRAY1);

void compute_stability_measure_aux_c(int DIM1, int *INPLACE_ARRAY1,int DIM1, int *INPLACE_ARRAY1,
                                     int DIM1, int *INPLACE_ARRAY1,int DIM1, int *INPLACE_ARRAY1,
                                     int DIM1, int *INPLACE_ARRAY1,int DIM1, double *INPLACE_ARRAY1, int delta, int hmin );

void get_signature_aux_c(int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1,
                         int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1,
                         int **ARGOUT_ARRAY1, int *DIM1, int start, int end, int cte);

void mms_mser_aux_c(int DIM1, double *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1,
                    int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1);

void mms_t_aux_c(double t, int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1, int DIM1,
                 int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1,
                 int DIM1, int *INPLACE_ARRAY1);




void extinction_filter_aux_c(int DIM1, int *INPLACE_ARRAY1, int DIM1, int *IN_ARRAY1,
                             int DIM1,  int *INPLACE_ARRAY1);

void area_difference_aux_c(int AD, int DIM1, int *INPLACE_ARRAY1,int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1);

void prog_area_difference_aux_c(int AD, int DIM1, int *INPLACE_ARRAY1,int DIM1, int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1, int DIM1, 
int *INPLACE_ARRAY1, int DIM1, int *INPLACE_ARRAY1);



