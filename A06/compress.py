import cv2
import numpy as np
import struct
import os

class CompressedImageWriter:
	def __init__(self,name,w,h):
		self.f=open(name,"wb")
		self.f.write(b'OOF')
		self.f.write(struct.pack(">HH",w,h))
	def write(self,n,c):
		c=int(c)
		while n>0:
			if n<128:
				b=n*2+c
				b=struct.pack(">B",b)
				self.f.write(b)
				n-=n
			else:
				b=127*2+c
				b=struct.pack(">B",b)
				self.f.write(b)
				n-=127
	def close(self):
		self.f.close()

def runLengthRow():
	for row in img:
		color = row[0]
		count = 0
		for item in row:
			if item == color:
				count += 1
			else:
				out.write(count, color)
				color = item
				count = 1
		out.write(count, color)

def runLengthCol():
	img2  = img.T
	for col in img2:
		color = col[0]
		count = 0
		for item in col:
			if item == color:
				count += 1
			else:
				out.write(count, color)
				color = item
				count = 1
		out.write(count, color)


for file in os.listdir("input/"):
	if file.endswith(".bmp"):
		img = cv2.imread("input/"+file, 0) / 255
		h, w = img.shape[:2]
		out = CompressedImageWriter("output/"+file[:-4]+".nls", w, h)
		if w > h:
			runLengthRow()
		else:
			runLengthCol()
		out.close()



