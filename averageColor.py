#Created 4.20.13 by NR
#AMDG

from PIL import Image

imgFileName = raw_input("Enter the name of the image file (with extension):")

image = Image.open(imgFileName)
width, height = image.size

r = 0
g = 0
b = 0

unavR = 0
unavG = 0
unavB = 0

max = width * height

i = 0

x = 0
y = 0

while i < max:
	if x < width:
		r, g, b = image.getpixel((x, y))
		unavR = unavR + r
		unavG = unavG + g
		unavB = unavB + b
		x = x + 1
		i = i + 1
	elif x == width:
		x = 0
		y = y + 1
avR = unavR / max
avG = unavG / max
avB = unavB / max

print "Average RGB:", avR, avG, avB

newImg = Image.new('RGB', (300,300), (avR, avG, avB))
newImg.save('/tmp/averageColor.png')
