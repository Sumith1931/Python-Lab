import rasterio

geotiff = "Sentinel-2_L2A_B01_(Raw).tiff"

with rasterio.open(geotiff) as src:
    print("Width :", src.width)
    print("Height:", src.height)
    print("Total Bands:", src.count)
    print("CRS:", src.crs)
