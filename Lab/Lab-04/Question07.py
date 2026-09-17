import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Read Red and NIR bands
with rasterio.open('Sentinel-2_L2A_B04_(Raw).tiff') as src:
    red = src.read(1).astype(float)

with rasterio.open('Sentinel-2_L2A_B08_(Raw).tiff') as src:
    nir = src.read(1).astype(float)

# Compute NDVI
ndvi = (nir - red) / (nir + red + 1e-10)

# Vegetation threshold
vegetation = np.where(ndvi > 0.3, 1, 0)

# Calculate vegetation area
pixel_area = 10 * 10    # Sentinel-2 resolution = 10 m
veg_pixels = np.sum(vegetation)

veg_area_m2 = veg_pixels * pixel_area
veg_area_ha = veg_area_m2 / 10000

print("Vegetated Pixels:", veg_pixels)
print("Vegetated Area (m²):", veg_area_m2)
print("Vegetated Area (ha):", veg_area_ha)

# NDVI Map
plt.figure(figsize=(8,6))
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label='NDVI')
plt.title('NDVI Map')
plt.axis('off')
plt.show()

# Vegetation Landcover Map
plt.figure(figsize=(8,6))
plt.imshow(vegetation, cmap='Greens')
plt.colorbar(label='0 = No Vegetation, 1 = Vegetation')
plt.title('Vegetation Landcover Map')
plt.axis('off')
plt.show()