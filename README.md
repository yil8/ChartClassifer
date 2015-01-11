ChartClassifer
==============

An chart image classifier based on Python

Copyright (c) 2013 Yi Li <hmily870311@gmail.com>

INSTALL
=======

Prerequisites
-------------
**Mandatory** 
* Python (2.7). [Python 2.7.3](http://www.python.org/download/releases/2.7.3/) is recommended.

* [Numpy](http://www.numpy.org/)(>=1.6.1). You can download the source of Numpy from [here](http://sourceforge.net/projects/numpy/files/).

* [Scipy](http://www.scipy.org/)(>=0.10). You can download the source of Scipy from [here](http://sourceforge.net/projects/scipy/files/).

* [PIL](http://www.pythonware.com/products/pil/index.htm)(>=1.1.7).

Install numpy, scipy on Ubuntu:
sudo apt-get install python-numpy python-scipy

Instal PIL on Linux:

1. Download PIL 1.1.7 under "Python Imaging Library 1.1.7 Source Kit" as Imaging-1.1.7.tar.gz

2. run:
tar -xzvf Imaging-1.1.7.tar.gz

3. Go into the folder created and (as root) install the package as run:
python setup.py install

Compile libSVM
--------------

Under the bin directory, imageUtils.py and img_svm_predict.py are my sources; libSVM_COPYRIGHT  Makefile  svm.cpp  svm.def  svm.h  svm.py  svmutil.py are the sources of libSVM. 

The static library of libSVM need to be compiled to run img_svm_predict.py. Simply type:

make

TEST
====

Under the model directory are the trained model of chart image classifier.
Under the images directory are the images used for both training and testing.

To test img_svm_predict.py, go to images directory and run:


python ../bin/img_svm_predict.py ./bar/1.jpeg

python ../bin/img_svm_predict.py ./pie/2.jpeg

You can also download any chart images from Google image to test.
Currently, only bar chart, pie chart and scatter plot are supported.

Reference
=========
Manolis Savva (2011). ReVision: Automated Classification, Analysis and Redesign of Chart Images


