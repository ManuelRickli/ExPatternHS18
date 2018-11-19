import sys
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import scipy.io
import scipy.spatial
import matplotlib.pyplot as plt
import math
from pca import PCA

# TODO: Implement euclidean distance between two vectors
def euclideanDistance(a, b):
    '''
    :param a: vector
    :param b: vector
    :return: scalar
    '''
    return np.linalg.norm(a-b)

# TODO: Implement mahalanobis distance between two vectors
def mahalanobisDistance(a, b, invS):
    '''
    :param a: vector
    :param b: vector
    :param invS: matrix
    :return: scalar
    '''
    return scipy.spatial.distance.mahalanobis(a,b,invS)


def faceRecognition():
    '''
    Train PCA with with 25 components
    Project each face from 'novel' into PCA space to obtain feature coordinates
    Find closest face in 'gallery' according to:
        - Euclidean distance
        - Mahalanobis distance
    Redo with different PCA dimensionality

    What is the effect of reducing the dimensionality?
    What is the effect of different similarity measures?
    '''
    numOfPrincipalComponents = 25
    # TODO: Train a PCA on the provided face images

    # TODO: Plot the variance of each principal component - use a simple plt.plot()

    # TODO: Implement face recognition

    # TODO: Visualize some of the correctly and wrongly classified images (see example in exercise sheet)


def faceLoaderExample():
    '''
    Face loader and visualizer example code
    '''
    matgal = scipy.io.loadmat('../data/gallery.mat')
    gall = matgal['gall'][0]

    numOfFaces = gall.shape[0]
    [N, M] = gall.item(0)[1].shape

    print("NumOfFaces in dataset", numOfFaces)

    # Show first image
    plt.figure(0)
    plt.title('First face')
    n = 0
    facefirst = gall.item(n)[1]
    faceId = gall.item(n)[0][0]
    print('Face got face id: {}'.format(faceId))
    plt.imshow(facefirst, cmap='gray')

    plt.show()




if __name__ == "__main__":
    print(sys.version)
    print("##########-##########-##########")
    print("PCA images!")
    faceLoaderExample()
    faceRecognition()
    print("Fertig PCA!")
