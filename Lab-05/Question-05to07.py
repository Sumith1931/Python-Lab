import matplotlib.pyplot as plt
import geopandas as gpd

India_01 = gpd.read_file("gadm41_IND_0.shp")
India_02 = gpd.read_file("gadm41_IND_1.shp")
India_03 = gpd.read_file("gadm41_IND_2.shp")
India_04 = gpd.read_file("gadm41_IND_3.shp")
kerala = India_02[India_02['NAME_1'] == 'Kerala']
print(kerala)
India_03.plot()
plt.title("Districts of India")
kerala.plot(edgecolor="black", color="green")
plt.title("Kerala State Map")

print("Current CRS",India_03.crs)
Alappuzha = India_03[India_03['NAME_2'] == 'Alappuzha']
Alappuzha.plot(edgecolor="black", color="yellow")
plt.title("Alappuzha District Map")
plt.show()

#Question-07
India_03 = India_03.to_crs("EPSG:32643")
State = India_03[India_03['NAME_1'] == 'Kerala'].copy()
State['Area_m2'] = State.geometry.area

plt.figure(figsize=(10, 8))
plt.bar(State['NAME_2'], State['Area_m2'], color="blue", edgecolor="black")
plt.title("Kerala District Area Map")
plt.xlabel("Districts")
plt.ylabel("Area (m²)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

