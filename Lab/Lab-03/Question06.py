import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Picture001.jpeg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

R = img_rgb[:, :, 0]
G = img_rgb[:, :, 1]
B = img_rgb[:, :, 2]

hist_R = cv2.calcHist([R], [0], None, [256], [0, 256])
hist_G = cv2.calcHist([G], [0], None, [256], [0, 256])
hist_B = cv2.calcHist([B], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(hist_R, color='red')
plt.title('Red Channel Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])

plt.subplot(3, 1, 2)
plt.plot(hist_G, color='green')
plt.title('Green Channel Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])

plt.subplot(3, 1, 3)
plt.plot(hist_B, color='blue')
plt.title('Blue Channel Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
