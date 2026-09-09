import matplotlib.pyplot as plt
import numpy as np
import cv2
img = cv2.imread('Picture001.jpeg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("Picture001")
plt.axis('off')
plt.show()