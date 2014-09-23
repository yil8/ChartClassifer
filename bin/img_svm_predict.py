#python libraries
import sys
import os
import Image
import numpy
import scipy
import pickle
from scipy.cluster.vq import kmeans, vq

#libSVM library
from svmutil import svm_load_model, svm_predict

#own library
from imageUtils import *

#macro parameters
img_size = 128
patch_size = 6
sample_per_img = 100
block_thred = 0.1
K = 150

centroid_bar = '../model/bar_centroids.pickle'
centroid_pie = '../model/pie_centroids.pickle'
centroid_scatter_plot = '../model/scatter_plot_centroids.pickle'
inmodel = '../model/t_1_d_1.model'



def main(argv=None):
    inimg = sys.argv[1] #input image file name
    
    #load in the k-means centroids of bar chart, pie chart, and scatter plot
    centroids = []
    centroids.extend(pickle.load(open(centroid_bar)))
    centroids.extend(pickle.load(open(centroid_pie)))
    centroids.extend(pickle.load(open(centroid_scatter_plot))) 
    centroids = numpy.array(centroids)
    D, __ = centroids.shape
    
    img = Image.open(inimg).convert('L')

    #image resize
    img_resized = imageResize(img, img_size)
        
    #get the luma of the image
    luma_resized = imageToLuma(img_resized)
    
    #get all the patches of the image
    luma_patches = getAllPatches(luma_resized, patch_size)

    #starndardize patches
    patches_standardized = map(patchStandardize, luma_patches)
    
    #flatten all patch matrix in patches_pool list
    patches_vector = arrayLstFlatten(patches_standardized)  
    
    #get the closest centroid index based fon features
    idx, __ = vq(patches_vector, centroids)
    idx = idx.tolist()
    
    #based on index form the feature
    feature = map(idx.count, range(0, D))
    
    model = svm_load_model(inmodel)
    
    label, __, __ = svm_predict([0], [feature], model, '-q')
    
    if label[0] == 1:
        print '***bar chart***'
    
    elif label[0] == 2:
        print '***pie chart***'

    elif label[0] == 3:
        print '***scatter plot***'

    


if __name__ == '__main__':
    main()
