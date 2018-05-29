import cv2
import numpy as np

def greyscale(img):
	img = img *1
	img = img[:,:,0]*0.2+img[:,:,1]*.7+img[:,:,2]*0.1
	img = img[:,:,None]
	img = np.uint8(img)
	return img


def blackWhite(img, threshold=128):
	img = greyscale(img)
	img[img<threshold] = 0
	img[img>threshold] = 255
	return np.uint8(img)


def desaturate(img, percent=1):
	img = greyscale(img)*percent+img*(1-percent)
	return np.uint8(img)


def contrast(img,factor=1):
	img[:,:,:]=((img-128)*factor)+128
	#cv2.imwrite("output/pic_1_d.png",img)
	return img

img = cv2.imread('input/image1.png')
img2 = cv2.imread('input/image2.png')
img3 = cv2.imread('input/image3.png')
w1,h1 = img.shape[:2]


def perspectiveCube1(img1, img2):
	pts1 = np.float32([[0, 0], [640, 0], [640, 480], [0, 480]])
	pts2 = np.float32([[135,112], [278, 192], [291, 412], [157, 306]])

	M1 = cv2.getPerspectiveTransform(pts1, pts2)
	M2 = np.float32([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	M = M1.dot(M2)
	dst = cv2.warpPerspective(img1, M, (640, 480))

	mask = np.min(dst == 0, axis=2)
	mask = mask[:, :, None] * img2
	mask += dst

	return mask

def perspectiveCube2(img1, img2):
	pts1 = np.float32([[0, 0], [640, 0], [640, 480], [0, 480]])
	pts2 = np.float32([[139,108], [318,54], [474,111], [281,188]])

	M1 = cv2.getPerspectiveTransform(pts1, pts2)
	M2 = np.float32([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	M = M1.dot(M2)
	dst = cv2.warpPerspective(img1, M, (640, 480))

	mask = np.min(dst == 0, axis=2)
	mask = mask[:, :, None] * img2
	mask += dst

	return mask

def perspectiveCube3(img1, img2):
	pts1 = np.float32([[0, 0], [640, 0], [640, 480], [0, 480]])
	pts2 = np.float32([[283,192], [479,115], [467,319], [296,414]])

	M1 = cv2.getPerspectiveTransform(pts1, pts2)
	M2 = np.float32([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	M = M1.dot(M2)
	dst = cv2.warpPerspective(img1, M, (640, 480))

	mask = np.min(dst == 0, axis=2)
	mask = mask[:, :, None] * img2
	mask += dst

	return mask




#theta = np.deg2rad(30)
#R1 = np.float32([[1,0,-640],[0,1,-480],[0,0,1]])
#R2 = np.float32([[np.cos(theta),np.sin(theta),0],[-np.sin(theta),np.cos(theta),479],[0,0,1]])
#R3 = np.float32([[1,0,640],[0,1,480],[0,0,1]])
#R_Final = R1.dot(R2).dot(R3)
#print(R_Final)
#copy = cv2.warpPerspective(img*1,R_Final,(cols,rows))
#cv2.imwrite("output/pic_2_b.png", copy)

#M_flip = np.float32([[1,0,0],[0,-1,479]])
#dst = cv2.warpAffine(img*1,M_flip,(cols,rows))


cv2.waitKey(0)
cv2.destroyAllWindows()
