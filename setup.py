#! /usr/bin/env python

# BSD 2-Clause License
# Copyright (c) 2016, Roberto Souza and collaborators
# All rights reserved.


# System imports
from distutils.core import *
from distutils      import sysconfig

import os

(opt,) = sysconfig.get_config_vars('OPT')
if opt is not None:
    os.environ['OPT'] = " ".join(flag for flag in opt.split() if flag != '-Wstrict-prototypes')



# Third-party modules - we depend on numpy for everything
import numpy


# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include() # get_numpy_include()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


src_dir = 'siamxt'
src_dir_c = 'C++'
src_dir_swig = 'SWIG'



# extension modules
_max_tree_c_01 = Extension(
            '_max_tree_c_01',
            [os.path.join(src_dir,src_dir_c,'max_tree_c_01.cpp'), os.path.join(src_dir,\
            src_dir_c,'max_tree_c_01_wrap.cpp')],
                           define_macros=[('NDEBUG', None)],#,('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')
            include_dirs=[numpy_include],
            library_dirs=[],
            libraries=[],
	    extra_compile_args=['-std=c++11']
            #swig_opts=['-c++', '-includeall', '-threads', '-keyword'],
        )

_morph_tree_alpha_aux_c = Extension(
            '_morph_tree_alpha_aux',
            [os.path.join(src_dir,src_dir_c,'morph_tree_alpha_aux.cpp'),os.path.join(src_dir,src_dir_c,'morph_tree_alpha_aux_wrap.cpp') ],
            define_macros=[('NDEBUG', None)],
            include_dirs=[numpy_include],
            library_dirs=[],
            libraries=[],
	    extra_compile_args=['-std=c++11']
            #swig_opts=['-c++', '-includeall', '-threads', '-keyword'],
        )


_max_tree_alpha_aux_c = Extension(
            '_max_tree_alpha_aux',
            [os.path.join(src_dir,src_dir_c,'max_tree_alpha_aux.cpp'), os.path.join(src_dir,\
            src_dir_c,'max_tree_alpha_aux_wrap.cpp')],
            define_macros=[('NDEBUG', None)],
            include_dirs=[numpy_include],
            library_dirs=[],
            libraries=[],
	    extra_compile_args=['-std=c++11']
            #swig_opts=['-c++', '-includeall', '-threads', '-keyword'],
        )

setup(  name        = "siamxt",
    version     = "1.0.0",
	ext_modules = [_max_tree_c_01,_morph_tree_alpha_aux_c,_max_tree_alpha_aux_c],
	packages=['siamxt'],
	package_data={'siamxt': ['things/grey_levels.png']},
    author="Roberto M Souza and collaborators",
    author_email="roberto.medeiros.souza@gmail.com",
    description="Max-tree Toolbox for Teaching Image Processing",
    license="BSD 2-clause License",
    keywords=["image processing", "mathematical morphology","max-tree"],
    url="https://github.com/rmsouza01/siamxt/tree/16bit/siamxt",
    long_description=read('README.txt'),
    classifiers=[
    "Development Status :: 1 - Alpha",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python and C++ glued with SWIG",
    "Topic :: Scientific/Engineering :: Mathematical Morphology",
    "License :: BSD 2-clause",
    ],
    )


