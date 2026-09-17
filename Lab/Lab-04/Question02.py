import matplotlib.pyplot as plt
import rasterio
import numpy as np

bands = ["Sentinel-2_L2A_B02_(Raw).tiff", "Sentinel-2_L2A_B03_(Raw).tiff", "Sentinel-2_L2A_B04_(Raw).tiff"]

for file in bands:

    with rasterio.open(file) as src:
        data = src.read(1)

        print(file)
        print("Min :", np.min(data))
        print("Max :", np.max(data))
        print("Mean:", np.mean(data))
        print()
    plt.figure(figsize=(6,4))
    plt.hist(data.flatten(), bins=50)
    plt.title(f"Histogram of {file}")

    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.show()