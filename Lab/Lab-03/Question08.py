import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load image
img = cv2.imread('Picture001.jpeg')

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Original dimensions
height, width, channels = img_rgb.shape

print("Original image shape:", img_rgb.shape)

# --------------------------------------------------
# 1. ZOOM IN BY 2x
# --------------------------------------------------

# Take the central half of the image
crop_h = height // 2
crop_w = width // 2

start_y = (height - crop_h) // 2
start_x = (width - crop_w) // 2

cropped = img_rgb[
    start_y:start_y + crop_h,
    start_x:start_x + crop_w
]

# Resize cropped region to original size
zoom_in = cv2.resize(
    cropped,
    (width, height),
    interpolation=cv2.INTER_LINEAR
)

# --------------------------------------------------
# 2. ZOOM OUT BY 2x
# --------------------------------------------------

# Reduce image to half its size
small = cv2.resize(
    img_rgb,
    (width // 2, height // 2),
    interpolation=cv2.INTER_AREA
)

# Create a black canvas of original size
zoom_out = np.zeros_like(img_rgb)

# Place the smaller image in the center
y_offset = (height - small.shape[0]) // 2
x_offset = (width - small.shape[1]) // 2

zoom_out[
    y_offset:y_offset + small.shape[0],
    x_offset:x_offset + small.shape[1]
] = small

print("Zoom In image shape:", zoom_in.shape)
print("Zoom Out image shape:", zoom_out.shape)

plt.figure(figsize=(6, 5))


plt.subplot(1, 2, 1)
plt.imshow(zoom_in)
plt.title("Zoom In (2x)")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(zoom_out)
plt.title("Zoom Out (2x)")
plt.axis("off")

plt.tight_layout()
plt.show()
