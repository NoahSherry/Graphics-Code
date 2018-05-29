import cv2
import numpy as n
image1 = cv2.imread("input/image1.png")
image2 = cv2.imread("input/image2.png")
flag_OG = cv2.imread("input/flag.png")

def splitChannels(image):
    b = image*1
    # set green and red channels to 0
    b[:, :, 1] = 0
    b[:, :, 2] = 0
    g = image*1
    # set blue and red channels to 0
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    r = image*1
    # set blue and green channels to 0
    r[:, :, 0] = 0
    r[:, :, 1] = 0
    # RGB - Blue
    cv2.imshow('B-RGB', b)
    # RGB - Green
    cv2.imshow('G-RGB', g)
    # RGB - Red
    cv2.imshow('R-RGB', r)

def swapChannels(img,c1=0,c2=1):
    chan1=img[:,:,c1]
    chan2=img[:,:,c2]
    img_swap=img*1
    img_swap[:,:,c2]=chan1
    img_swap[:,:,c1]=chan2
    cv2.imshow("Output",img_swap)
    cv2.imwrite("output/pic_1_a.png", img_swap)

def extractChannel(img,chan):
    ext=img[:,:,chan]
    cv2.imwrite("output/pic_1_b.png", ext)

def invertChannel(img,chan):
    inv = img*1
    inv[:,:,chan] = 255 - img[:,:,chan]
    cv2.imwrite("output/pic_1_c.png", inv)

def addHundred(img):
    copy=img*1.0
    copy += 100
    copy[copy>255] = 255
    cv2.imwrite("output/pic_1_d.png", n.uint8(copy))

def centerAdd(img,chan):
    cen = img*1
    w = img.shape[0]
    h = img.shape[1]
    cen[int(w/2)-50:int(w/2)+50,int(h/2)-50:int(h/2)+50,chan] = 255
    cv2.imwrite("output/pic_2_a.png", cen)

def copyCenter(img1, img2):
    copy1 = img1*1
    copy2 = img2*1
    w1 = img1.shape[0]
    h1 = img1.shape[1]
    w2 = img2.shape[0]
    h2 = img2.shape[1]

    copy2[int(w2 / 2) - 50:int(w2 / 2) + 50, int(h2 / 2) - 50:int(h2 / 2) + 50,:] = copy1[int(w1/2)-50:int(w1/2)+50,int(h1/2)-50:int(h1/2)+50,:]
    cv2.imwrite("output/pic_2_b.png", copy2)

def imageStats(img):
    print("Total Pixels = " + str(img.shape[0] * img.shape[1]))
    print("Min Intensity Value = " + str(n.min(img)))
    print("Max Intensity Value = " + str(n.max(img)))
    print("Standard Deviation = " + str(n.std(img)))
    print("Mean Intensity Value = " + str(n.mean(img)))

def drawStar(img,point,color=(0,0,0),N=5,R=100,C=2):
	xc,yc=point
	h,w=img.shape[:2]
	y,x=n.mgrid[:h,:w]
	dy=y-yc
	dx=x-xc
	r=n.hypot(dx,dy)
	tip_angle=(180-360.0*C/N)/2*n.pi/180
	angle=n.arctan2(dy,dx)/n.pi*180-90
	angle%=360.0/N
	angle-=180.0/N
	angle=n.abs(angle)
	xp=r*n.cos(angle*n.pi/180)
	yp=r*n.sin(angle*n.pi/180)
	img[yp<-n.tan(tip_angle)*xp+R*n.sin(tip_angle)]=color

def makeFlag(img):
    h, w = img.shape[:2]
    y, x = n.mgrid[:h, :w]
    flag = n.zeros((int(h),int(w),3), dtype=n.uint8)
    flag[int(h/3):int(2*h/3),:] = (255,255,255)
    flag[int(w/3):int(w/2),:] = (61,122,0)

    flag[n.minimum(y,h-y)>x/2] = (38,17,206)

    drawStar(flag, (130,int(h/2)), color=(255,255,255), N=7, R=int(h*(0.08)),C=2.6)
    cv2.imwrite("output/pic_4_a.png",flag)

def getDiff(img1,img2):
    image1 = img1*1.0
    image2 = img2*1.0
    dif = n.abs(image1-image2)
    dif -= dif.min()
    dif += dif.max()
    dif += 255
    cv2.imwrite("output/pic_4_b.png", n.uint8(dif))


cv2.waitKey(0)
cv2.destroyAllWindows()
