#4
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Picture001.jpeg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

height, width, channels = img_rgb.shape
print("Image dimensions:", height, "x", width)

y1, y2 = 200, 1000
x1, x2 = 1400, 2500

cropped_img = img_rgb[y1:y2, x1:x2]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cropped_img)
plt.title("Cropped Region")
plt.axis('off')

plt.tight_layout()
plt.show()
