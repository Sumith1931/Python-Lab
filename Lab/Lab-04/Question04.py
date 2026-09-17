import rasterio
import numpy as np
import matplotlib.pyplot as plt
with rasterio.open("bandstack.tif") as src:
    print("Number of bands:", src.count)

    red = src.read(4)
    green = src.read(3)
    blue = src.read(2)

rgb = np.dstack([red,green,blue])

rgb = rgb / np.max(rgb)

plt.figure(figsize=(8,8))
plt.imshow(rgb)
plt.title("True Color Composite")
plt.axis('off')
plt.show()

with rasterio.open("bandstack.tif") as src:

    blue = src.read(2) # B02
    green = src.read(3) # B03
    NIR = src.read(8) # B08 (NIR)

    fcc = np.dstack((NIR, green, blue))

    fcc = fcc / fcc.max()

    plt.figure(figsize=(8,8))
    plt.imshow(fcc)
    plt.title("False Color Composite (FCC)")
    plt.axis('off')
    plt.show()