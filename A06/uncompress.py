import numpy as np
import cv2
import struct
import os

for file in os.listdir("output/"):
	if file.endswith(".nls"):
		f = open("output/"+file, "rb")
		m = []
		print(f.read(3))
		w, h = struct.unpack(">HH", f.read(4))
		print(w, h)
		data = f.read()
		for b in data:
			b = int(b)
			rl = b // 2
			color = b % 2
			m += [color] * rl

		w2 = w
		h2 = h
		if h > w:
			w2 = h
			h2 = w
		img = np.uint8(m).reshape(h2, w2) * 255
		if w > h:
			cv2.imwrite("output/"+file[:-4]+".bmp", img)
		else:
			cv2.imwrite("output/"+file[:-4]+".bmp", img.T)


