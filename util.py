import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram_create( n=256 ):
    h = np.zeros( (n), dtype=int)
    return h


def image_create(h,w,c=1):
    img = np.zeros((h, w, c), dtype="uint8")
    return img


def image_read( file ):
    im = cv2.imread( file, 0)
    return( im )


def image_write( im, file ):
    cv2.imwrite( file, im )


def image_local_max(img):

    def take_value(elem):
        return elem[2]

    local_max = []
    w, h = img.shape

    for i in range(1, w-1):
        for j in range(1, h-1):
            
            tmp = np.max(img[ i-1:i+1, j-1:j+1])
            if img[i,j] == tmp:
                local_max.append([i, j, img[i,j]])

    local_max.sort(key=take_value, reverse=True)
            
    return local_max 


def aa(local_max):

    for elm in local_max:
        i, j, value = elm[0], elm[1], elm[2]


def plot_histogram(histogram):

    plt.hist(histogram, bins=256, rwidth=0.2)
    plt.show()