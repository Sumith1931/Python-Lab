import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Picture001.jpeg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

height, width, channels = img_rgb.shape

mid_h = height // 2
mid_w = width // 2

top_left = img_rgb[:mid_h, :mid_w]
top_right = img_rgb[:mid_h, mid_w:]
bottom_left = img_rgb[mid_h:, :mid_w]
bottom_right = img_rgb[mid_h:, mid_w:]

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(top_left)
plt.title("Top Left")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(top_right)
plt.title("Top Right")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(bottom_left)
plt.title("Bottom Left")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(bottom_right)
plt.title("Bottom Right")
plt.axis('off')

plt.tight_layout()
plt.show()

top = cv2.hconcat([top_left, top_right])
bottom = cv2.hconcat([bottom_left, bottom_right])

merged_img = cv2.vconcat([top, bottom])

plt.figure(figsize=(8, 6))
plt.imshow(merged_img)
plt.title("Merged Image")
plt.axis('off')
plt.show()
