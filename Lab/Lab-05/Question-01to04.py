import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd

#Question-01
meghalaya_file =gpd.read_file("D:\\Programming Lab\\Lab-05\\meghalaya\\meghalaya.shp")
NE_states_file = gpd.read_file("D:\\Programming Lab\\Lab-05\\NE_states\\NE_states.shp")

print("CRS Meghalaya =",meghalaya_file.crs)
print("CRS NE_States =",NE_states_file.crs)

#Question-02
m = meghalaya_file.isnull().sum()
n = NE_states_file.isnull().sum()
print("Null values in  Meghalaya_file =\n",m,"\nNull values in NE_states_file =\n",n)

#Question-03
meghalaya_reprojected = meghalaya_file.to_crs("EPSG:4326")
NE_states_reprojected = NE_states_file.to_crs("EPSG:4326")
print("CRS Meghalaya after reprojecting =",meghalaya_reprojected.crs)

meghalaya_reprojected.plot()
plt.title("Meghalaya State")
plt.show()
NE_states_reprojected.plot(color="blue", edgecolor="black")
plt.title("North Eastern States of India")
plt.show()
#meghalaya_reprojected.to_file("D:\\Programming Lab\\Lab-05\\meghalaya\\meghalaya_reprojected_plot.shp")
#NE_states_reprojected.to_file("D:\\Programming Lab\\Lab-05\\NE_states\\NE_states_reprojected_plot.shp")

#Question-04
NE_states_file = NE_states_file.to_crs("EPSG:32646")
print("Area of North Eastern States of India =\n")
Area ={}
for i in NE_states_file['State_Name']:
    area = NE_states_file[NE_states_file['State_Name'] == i].geometry.area.sum()
    Area[i] = area
A = sorted(Area.items(), key=lambda x: x[1], reverse=True)

for state, area in A:
    print(state,"=",area,"m2")

state = [x[0] for x in A]
area = [x[1] for x in A]
plt.figure(figsize=(10,8))
plt.bar(state,area, color ="yellow", edgecolor ="black")
plt.xlabel("North Eastern States")
plt.ylabel("Area (m²)")
plt.title("Area of North Eastern States of India")
plt.show()