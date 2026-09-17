import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Open Sentinel-2 band stack
with rasterio.open("bandstack.tif") as src:
    data = src.read().astype(float)

print("Data shape:", data.shape)

# Sentinel-2 bands
# B02 = Blue  -> band 2
# B03 = Green -> band 3
# B04 = Red   -> band 4
# B08 = NIR   -> band 8

blue = data[1]
red = data[3]
nir = data[7]

# Calculate NDVI
ndvi = (nir - red) / (nir + red + 1e-10)

# Identify vegetation pixels
vegetation = np.where(ndvi > 0.5)

print("Number of vegetation pixels:", len(vegetation[0]))

# Extract spectral values for all vegetation pixels
veg_data = data[:, vegetation[0], vegetation[1]]

# Calculate mean spectral signature
veg_spec = np.mean(veg_data, axis=1)

# Plot spectral signature
bands = np.arange(1, data.shape[0] + 1)

plt.figure(figsize=(8, 5))
plt.plot(bands, veg_spec, marker='o', color='green')

plt.xlabel("Sentinel-2 Band")
plt.ylabel("Mean Pixel Value")
plt.title("Vegetation Spectral Signature")

plt.xticks(bands)
plt.grid(True)
plt.show()
