import matplotlib.pyplot as plt;
import pandas as pd;
import numpy as np;

lat_list = ["latitude"]
long_list = ["longitude"]
pop_density = ["population_2020"]
df = pd.read_csv("C:\\Users\Sarin\Downloads\pioneerandPropser\PioneerandProsper\population_vnm_2018-10-01.csv", usecols= lat_list)
df1 = pd.read_csv("C:\\Users\Sarin\Downloads\pioneerandPropser\PioneerandProsper\population_vnm_2018-10-01.csv", usecols = long_list)
df2 = pd.read_csv("C:\\Users\Sarin\Downloads\pioneerandPropser\PioneerandProsper\population_vnm_2018-10-01.csv", usecols = pop_density)

xdata = df.to_numpy()
xdata = xdata[0::1250]
# add the coordinate thingy? not sure 
ydata = df1.to_numpy()
ydata = ydata[0::1250]
zdata = df2.to_numpy()
zdata = zdata[0::1250]

# label axes and make key points/cities
# create title
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.scatter3D(xdata, ydata, zdata)
plt.xlabel("x");
plt.ylabel("y");
ax.set_zlabel("z");
plt.show()
