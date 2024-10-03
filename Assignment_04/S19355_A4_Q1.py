
# Import Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the Original image
img = cv2.imread(r'orion_spinelli_c1.jpg',cv2.IMREAD_COLOR)

# Convert Color Spaces : BGR -> RGB -> GrayScale
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgGrayScale = cv2.cvtColor(imgRGB,cv2.COLOR_BGR2GRAY)

# Applies a median blur to the grayscale image to reduce noise
blur = cv2.medianBlur(imgGrayScale,13)

# Converts the grayscale image into a binary image : Otsu's thresholding
ret, mask = cv2.threshold(blur,0,255,cv2.THRESH_BINARY +cv2.THRESH_OTSU)

# Converts the binary mask image to a BGR image
maskBGR = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

output = cv2.bitwise_and(imgRGB,maskBGR)

# Plotting
plt.figure(figsize=(12, 12), num='Extracted Orion Constellation')

plt.subplot(1,3,1)
plt.title('Original Image')
plt.xticks([]),plt.yticks([])
plt.imshow(imgRGB)

plt.subplot(1,3,2)
plt.title('Mask')
plt.xticks([]),plt.yticks([])
plt.imshow(maskBGR,cmap='Greys_r')

plt.subplot(1,3,3)
plt.title('Output')
plt.xticks([]),plt.yticks([])
plt.imshow(output)

plt.show()