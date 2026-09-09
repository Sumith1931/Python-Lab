#02
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Picture001.jpeg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_float = img_rgb.astype(np.float32)

mean = np.mean(img_float, axis=(0, 1))
std = np.std(img_float, axis=(0, 1))

print("Mean of R, G, B channels:", mean)
print("Standard deviation of R, G, B channels:", std)

normalized_img = (img_float - mean) / std

print("\nNormalized image:")
print("Minimum value:", normalized_img.min())
print("Maximum value:", normalized_img.max())

plt.imshow(normalized_img)
plt.title("Normalized RGB Image")
plt.axis('off')
plt.show()

#03
height, width, channels = img.shape

total_pixels = height * width

print("Height:", height)
print("Width:", width)
print("Channels:", channels)
print("Data type:", img.dtype)
print("Total pixels:", total_pixels)