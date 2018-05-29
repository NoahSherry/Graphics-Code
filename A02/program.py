import cv2
import numpy as np


def boxBlur5x5(img):
    kernel =  (1/25)*np.float32([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
    dst = cv2.filter2D(img, -1, kernel)
    return dst

def boxBlurSplit(img):
    kernel_0 = np.float32(
        [[1],[1],[1],[1],[1]]
    ) * (1/5)
    kernel_1 = kernel_0[:,None]
    kernel_mix = kernel_0.dot(kernel_1)
    dst = cv2.filter2D(img, -1, kernel_mix)
    return dst

def gaussianBlur5x5(img):
    kernel = (1/256) * np.float32([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])
    dst = cv2.filter2D(img, -1, kernel)
    return dst

def getDiff(img1,img2):
    image1 = img1*1.0
    image2 = img2*1.0
    dif = np.abs(image1-image2)
    dif -= dif.min()
    dif += dif.max()
    dif += 255
    return np.uint8(dif)

def gaussianBlurSplit(img):
    kernel_0 = np.float32(
        [[1],[4],[6],[4],[1]]
    ) * (1/16)
    kernel_1 = kernel_0[:,None]
    kernel_mix = kernel_0.dot(kernel_1)
    dst = cv2.filter2D(img, -1, kernel_mix)
    return dst

def edgeFilter(img):
    kernel = np.float32([[1,0,-1],[0,0,0],[-1,0,1]])
    dst = cv2.filter2D(img, -1, kernel)
    return dst

def sharpen(img):
    kernel = np.float32([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]])
    dst = cv2.filter2D(img, -1, kernel * (1/8))
    return dst

image = cv2.imread("input/image1.png")
cv2.imwrite("output/pic_1_d_1.png", boxBlurSplit(image))


cv2.waitKey(0)
cv2.destroyAllWindows()
