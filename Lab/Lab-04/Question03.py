import rasterio

band_files = [
    'Sentinel-2_L2A_B01_(Raw).tiff',
    'Sentinel-2_L2A_B02_(Raw).tiff',
    'Sentinel-2_L2A_B03_(Raw).tiff',
    'Sentinel-2_L2A_B04_(Raw).tiff',
    'Sentinel-2_L2A_B05_(Raw).tiff',
    'Sentinel-2_L2A_B06_(Raw).tiff',
    'Sentinel-2_L2A_B07_(Raw).tiff',
    'Sentinel-2_L2A_B08_(Raw).tiff',
    'Sentinel-2_L2A_B8A_(Raw).tiff',
    'Sentinel-2_L2A_B09_(Raw).tiff',
    'Sentinel-2_L2A_B11_(Raw).tiff',
    'Sentinel-2_L2A_B12_(Raw).tiff',
    'Sentinel-2_L2A_False_color.tiff',
    'Sentinel-2_L2A_NDVI.tiff',
    'Sentinel-2_L2A_True_color.tiff',
]

srcs = [rasterio.open(f) for f in band_files]

meta = srcs[0].meta

meta.update(
    count=len(srcs)
)

with rasterio.open("bandstack.tif","w",**meta) as dst:

    for i,src in enumerate(srcs, start=1):
        dst.write(src.read(1), i)

print("Band stack saved")