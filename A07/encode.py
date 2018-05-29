import cv2
import numpy as np
from random import *
import random
import math
# [::step_size,::step_size,:]
base_size = 900
step_size = int(round(base_size / 9))
base = np.zeros((base_size,base_size,1),dtype=np.uint8)
base[:,:,:] = 255
points = []
tracking_points = []
c = 0


def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result
s = input("Enter a string less than 10 characters to be encoded: ")
while len(s) > 9:
	s = input("Enter a string less than 10 characters to be encoded: ")

bits = tobits(s)

if len(bits) < 77:
    bits.append(0.5)

while len(bits) < 77:
    bits.append(randint(0,1))

for y in range(0,base_size,step_size):
    for x in range(0,base_size,step_size):
        c +=1
        points.append((y,x))

tracking_points.append(points[10])
tracking_points.append(points[16])
tracking_points.append(points[64])
tracking_points.append(points[70])


del points[10]
del points[15]
del points[62]
del points[67]


for p in points:
    c = bits[0]
    base[p[0]:p[0]+step_size,p[1]:p[1]+step_size] = c*255
    bits.pop(0)

c = 0
for p in tracking_points:
    c = tracking_points.index(p)
    x = p[0] + (step_size/2)
    y = p[1] + (step_size/2)
    base[p[0]:p[0] + step_size, p[1]:p[1] + step_size] = 0
    if c == 2:
        cv2.circle(base, (int(y),int(x)),int(step_size/3),255,-1)
    if c ==0:
        base[p[0] + int(step_size / 4):p[0] + int(step_size * 3 / 4),p[1] + int(step_size / 4):p[1] + int(step_size * 3 / 4)] = 255
    if c ==1:
        points = [[750,125],[775,150],[750,175],[725,150]]
        cv2.fillConvexPoly(base,np.array(points),255)
    if c ==3:
        base[p[0] + int(step_size / 3):p[0] + int(step_size * 2 / 3),p[1] + int(step_size / 3):p[1] + int(step_size * 2 / 3)] = 255

for x in range(0,10):
    if x %3 !=0:
        cv2.line(base,(0,x*step_size),(base_size,x*step_size) , (255, 255, 255), 6, 1)
    else:
        cv2.line(base, (0, x * step_size), (base_size, x * step_size), (255, 255, 255), 6, 1)
for y in range(0,10):
    if y % 3 != 0:
        cv2.line(base,(y*step_size,0),(y*step_size,base_size) , (255, 255, 255), 6, 1)
    else:
        cv2.line(base, (y * step_size, 0), (y * step_size, base_size), (255, 255, 255), 6, 1)
cv2.line(base, (0, base_size), (base_size, base_size), (255, 255, 255), 6, 1)
cv2.line(base, (base_size, 0), (base_size, base_size), (255, 255, 255), 6, 1)


cv2.imwrite("output.png",base)
cv2.waitKey(0)