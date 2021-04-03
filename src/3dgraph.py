import matplotlib.pyplot as plt;
import pandas as pd;
import numpy as np;

MAP_WIDTH = 2.5;
MAP_HEIGHT = 2.5;
lat_list = ["latitude"];
long_list = ["longitude"];
pop_density = ["population_2020"];
df = pd.read_csv("C:\\Users\Sarin\Downloads\pioneerandPropser\PioneerandProsper\csv files\population_vnm_2018-10-01.csv", usecols= lat_list);
df1 = pd.read_csv("C:\\Users\Sarin\Downloads\pioneerandPropser\PioneerandProsper\csv files\population_vnm_2018-10-01.csv", usecols = long_list);
df2 = pd.read_csv("C:\\Users\Sarin\Downloads\pioneerandPropser\PioneerandProsper\csv files\population_vnm_2018-10-01.csv", usecols = pop_density);

xdata = df.to_numpy();
xdata = xdata[0::1250];
# add the coordinate thingy? not sure

ydata = df1.to_numpy();
ydata = ydata[0::1250];

zdata = df2.to_numpy();
zdata = zdata[0::1250];

# label axes and make key points/cities
# create title
fig = plt.figure();
ax = plt.axes(projection = '3d');
ax.scatter(xdata, ydata, zdata, c= 'r', marker = 'o');
plt.xlabel("Longitude in Degrees");
plt.ylabel("Latitude in Degrees");
ax.set_zlabel("Number of Accidents");
ax.set_title("Number of Traffic Accidents by Longitude and Latitude in Hanoi")
plt.show();
