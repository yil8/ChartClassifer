import sys
import Image
import numpy
import scipy
from random import random

#input: img object, rescaled size, e.g. 128
#return: img object after resizing
def imageResize(img, size):
    x_len, y_len = img.size
    
    if x_len >= y_len:
        x_resized_len = size
        y_resized_len = int(y_len*x_resized_len/x_len)
    else:
        y_resized_len = size
        x_resized_len = int(x_len*y_resized_len/y_len)
        
    img_resized = img.resize((x_resized_len, y_resized_len), Image.ANTIALIAS)
    img_resized = img_resized.convert('L')
    
    luma = numpy.array(img_resized.getdata(), numpy.uint8).reshape(img_resized.size[1], img_resized.size[0])
    luma_resized = numpy.ones((size, size), dtype=numpy.uint8)*255    
    luma_resized[:luma.shape[0], :luma.shape[1]] = luma
    
    img_padded = Image.fromarray(luma_resized)
    
    return img_padded

#input: img object after resizing
#output: luma matrix of the img object
def imageToLuma(img):
    
    return numpy.array(img.getdata(), numpy.uint8).reshape(img.size[1], img.size[0])
    
#function: check whether the patch is color block
#input: luma matrix of patch and the threshold, e.g. 0.1
#output: true if it is color block, and false otherwise
def patchFilter(luma_patch, thred):
    
    return luma_patch.var() < luma_patch.max()*thred or luma_patch.std() == 0

#input: luma matrix of the img object after resizing, sampled patch size, e.g. 6
#output: luma matrix of the sampled patch
def sampleOnePatch(luma, size_patch):
    x_len, y_len = luma.shape 
    x_start = int((x_len - size_patch)*random())
    y_start = int((y_len - size_patch)*random())
    luma_patch = luma[x_start:(x_start+size_patch), y_start:(y_start+size_patch)]

    return luma_patch

#input: luma matrix of the img object after resizing, sampled patch size, e.g. 6, patch number, e.g. 100
#output: a list of luma matrix of the N sampled patch
def sampleNPatches(luma, size_patch, N, thred):
    x_len, y_len = luma.shape
    luma_patches = []
    
    i = 0
    while i < N:
        x_start = int((x_len - size_patch)*random())
        y_start = int((y_len - size_patch)*random())
        luma_patch = luma[x_start:(x_start+size_patch), y_start:(y_start+size_patch)]        
        if patchFilter(luma_patch, thred) == False:
            luma_patches.append(luma_patch)
            i += 1
        
    return luma_patches

#input: luma matrix of the img object after resizing, sampled patch size, e.g. 6
#output: a list of luma matrix of all the patches
def getAllPatches(luma, size_patch):
    x_len, y_len = luma.shape
    luma_patches = []
    
    for i in range(0, x_len-size_patch+1):
        for j in range(0, y_len-size_patch+1):
            luma_patch = luma[i:(i+size_patch), j:(j+size_patch)]
            luma_patches.append(luma_patch)
    
    return luma_patches

#input: luma matrix of patch
#output: standardized luma matrix of patch
def patchStandardize(luma_patch):
    
    if luma_patch.std() == 0:
        return luma_patch*0
    else:
        return (luma_patch - luma_patch.mean())/(luma_patch.std())
   
def arrayFlatten(aray):
    
    return aray.flatten()
    
def arrayLstFlatten(aray_lst):
    
    return numpy.array(map(arrayFlatten, aray_lst))

    
    
    
    














