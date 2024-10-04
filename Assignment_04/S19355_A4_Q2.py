
# Import Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the Original image
img = cv2.imread(r'numbers.jpg', cv2.IMREAD_GRAYSCALE)

# Global thresholding
T1 = 100

# Adaptive thresholding
adpThres_1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)
adpThres_2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 2)

# Plotting
plt.figure(figsize=(12, 12), num='Hidden Numbers')

plt.subplot(1,3,1)
plt.title('Original Image')
plt.xticks([]),plt.yticks([])
plt.imshow(img)

plt.subplot(1,3,2)
plt.title('Adaptive-Mean-Binary')
plt.xticks([]),plt.yticks([])
plt.imshow(adpThres_1,cmap='Greys_r')

plt.subplot(1,3,3)
plt.title('Adaptive-Mean-Binary-Inverse')
plt.xticks([]),plt.yticks([])
plt.imshow(adpThres_2)

plt.show()