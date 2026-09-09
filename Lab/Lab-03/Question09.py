import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Picture001.jpeg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pyramid1 = cv2.pyrDown(img_rgb)
pyramid2 = cv2.pyrDown(pyramid1)
pyramid3 = cv2.pyrDown(pyramid2)

print("Pyramid Level 3     :", pyramid3.shape)
print("Pyramid Level 2     :", pyramid2.shape)
print("Pyramid Level 1     :", pyramid1.shape)
print("Original image shape :", img_rgb.shape)

plt.figure(figsize=(7, 6))
plt.title("Image Pyramid")
plt.subplot(4, 1, 4)
plt.imshow(img_rgb)
plt.axis('on')

plt.subplot(4, 1, 3)
plt.imshow(pyramid1)
plt.axis('on')

plt.subplot(4, 1, 2)
plt.imshow(pyramid2)
plt.axis('on')

plt.subplot(4, 1, 1)
plt.imshow(pyramid3)
plt.axis('on')
plt.tight_layout()
plt.show()
