import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Picture001.jpeg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist_gray = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.plot(hist_gray, color='black')
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
