==================================
siamxt: Simple Max-tree Toolbox 
==================================

BSD 2-Clause License
Copyright (c) 2016, Roberto Souza and collaborators
All rights reserved.


Description
-----------

This is an alpha version of the simple max-tree toolbox (siamxt). The major difference to the iamxt toolbox is that it doesn't depend on OpenCV, SWIG, OpenMP and it doesn't come with the drawing methods. The toolbox was implemented in Python and the critical functions were implemented in C++ and wrapped in Python using SWIG. I run the SWIG files on my machine and I provide its output directly to you, so you don’t have to install SWIG on your machine. We have a different max-tree structure that is more suitable for array processing, and allows a fast development of new methods with a reasonable processing time. Our main goal in providing this toolbox is to spread the max-tree data structure further among the scientific community, investigate it further, and develop new tools that may be applied to solve real signal, image processing, and pattern recognition problems. This toolbox works for both 2D and 3D images of type uint8 and uint16. 

There is a public SoftwareX article describing the toolbox. The article is available for download here: http://www.sciencedirect.com/science/article/pii/S2352711017300079 If you use this toolbox on your work, please cite the this article.

- Souza, Roberto, et al. "iamxt: Max-tree toolbox for image processing and analysis." SoftwareX 6 (2017): 81-84.

@article{souza2017iamxt,
  title={iamxt: Max-tree toolbox for image processing and analysis},
  author={Souza, Roberto and Rittner, Let{\'\i}cia and Machado, Rubens and Lotufo, Roberto},
  journal={SoftwareX},
  volume={6},
  pages={81--84},
  year={2017},
  publisher={Elsevier}
}

Authors
---------

Roberto Souza - roberto.medeiros.souza@gmail.com
Letícia Rittner - lrittner@gmail.com
Rubens Machado - rubens.campos.machado@gmail.com 
Roberto Lotufo - robertoalotufo@gmail.com 


Acknowledgments
-----------------

Thanks to Alexandre Lopes (@alelopes) for adapting the code to Python 3.x.

Requirements
------------

This toolbox works with Python 3.x and requires NumPy. I use SWIG to communicate C and Python, but I generate the SWIG wrappers myself, so you don’t need to install SWIG on your computer.

Documentation
-------------

The documentation of this toolbox is the same of the iamxt (previous distribution of this toolbox) and is available at: http://adessowiki.fee.unicamp.br/adesso/wiki/iamxt/view/

The documentation page won’t load if you have Ad-blockers. Please, disable them!

Some demos can also be found in the jupyter-notebook folder in this repository.

Install
-------
Download the zip file, unzip it, go to the toolbox folder and type on terminal:
sudo python setup.py install (if installing in a root folder) or simply python setup.py install (if installing in a non-root folder, such as a virtual environment).


Note for Windows users
——————————————————————
I didn’t test this toolbox on windows platform, but I added the suggestion given by @u0078867 that should make it work.

Another option if you are a Windows user: a friend has developed a docker image with the toolbox. You can download it from the following repo: https://hub.docker.com/r/marianapbento/siamxt-1.0/

You can install Docker and download the image to use siamxt on your windows machine!


Collaborators
———————————————
If you are interested in adding features or contributing to the siamxt toolbox, please contact me at roberto.medeiros.souza@gmail.com. I am accepting all the help I can get! Currently, the toolbox has reasonable number of users, mostly in Brazil and Europe, but very few developers :(

Contact
---------

If you have any doubts, questions or suggestions to improve this toolbox, please contact me at: roberto.medeiros.souza@gmail.com
