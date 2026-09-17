import rasterio
from rasterio.windows import Window

with rasterio.open("bandstack.tif") as src:

    # Clip 500x500 pixels starting from row=200, col=200
    window = Window(200, 200, 500, 500)

    clipped = src.read(window=window)

    profile = src.profile
    profile.update(
        height=500,
        width=500,
        transform=src.window_transform(window)
    )

    with rasterio.open("clipped_aoi.tif", "w", **profile) as dst:
        dst.write(clipped)

print("AOI clipped and saved as clipped_aoi.tif")