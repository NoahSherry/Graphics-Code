import cv2
import numpy as np
import time

cv2.namedWindow("webcam")  # , cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("webcam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cap = cv2.VideoCapture(0)


ret, frame = cap.read()
h, w = frame.shape[:2]
y, x = np.mgrid[0:h, 0:w]
x = np.float32(x)
y = np.float32(y)
i = 0
start = time.time()
state = "normal"
contrast=5
spinSpeed = 1
threshold = 128

def greyscale(img):
	img = img *1
	img = img[:,:,0]*0.2+img[:,:,1]*.7+img[:,:,2]*0.1
	img = img[:,:,None]
	img = np.uint8(img)
	return img

while True:
    ret, frame = cap.read()
    fps = i / (time.time() - start)
    xp = x
    yp = y

    if state == "none":
        frame = frame
    if state == "con":
        frame[:,:,:]=((frame-128)*contrast)+128
    if state == "energy":
        kernel = np.float32([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        frame = cv2.filter2D(frame, -1, kernel)
    if state == "spin":
        angle = i%360
        angle = angle * spinSpeed
        image_center = tuple(np.array(frame.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        frame = cv2.warpAffine(frame, rot_mat, frame.shape[1::-1], flags=cv2.INTER_LINEAR)
    if state == "color":
        b = frame*1
        frame[:, :, 0] = b[:, :, 1]
        frame[:, :, 1] = b[:, :, 2]
        frame[:, :, 2] = b[:, :, 0]
    if state == "blur":
        kernel = np.float32([[1,1,1], [1,1,1], [1,1,1]])
        frame = cv2.filter2D(frame, -1, kernel * 1/9)
    if state == "invert":
        frame = (255 -frame)
    if state == "rorschach":
        frame = greyscale(frame)
        frame[frame < threshold] = 0
        frame[frame > threshold] = 255
    output = cv2.remap(frame, xp, yp, cv2.INTER_CUBIC)
    cv2.imshow("webcam", output)


    key = cv2.waitKey(1)
    if key == 113: #q
        state = "con"
    if key == 119: # w
        state = "energy"
    if key == 101: #e
        state = "spin"
    if key == 114: #r
        state = "color"
    if key == 116: #t
        state = "blur"
    if key == 121: #y
        state = "invert"
    if key == 117: #u
        state = "rorschach"
    if key == 120: #x
        state = "none"
    if key == 97: #a
        contrast=contrast+1
    if key == 122: #z
        contrast=contrast-1
    if key == 100: #d
        spinSpeed = spinSpeed+1
    if key == 99: #c
        spinSpeed = spinSpeed-1
    if key == 102: #f
        threshold = threshold+10
    if key == 118: #v
        threshold = threshold-10
    if key == 27:
        break
    i += 1

cap.release()
cv2.destroyAllWindows()