//BSD 2-Clause License
//Copyright (c) 2016, Roberto Souza and collaborators
//All rights reserved. 


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
