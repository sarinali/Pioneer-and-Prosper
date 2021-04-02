import matplotlib.pyplot as plt;
import pandas as pd;
import numpy as np;
##from mpl_toolkits import Basemap

#print(os.getcwd())

def f(x, y):
    return x*y;

x = [1, 2, 3];
y = [4, 6, 7];
z = []
for i in range(len(x)):
    z.append(f(x[i], y[i]))

##with open('sample.csv', 'r') as csvfile:
##    plots = csv.reader(csvfile, delimiter=',')
##
##plt.plot(x,y, marker='o')
##plt.show()
lat_list = ["latitude"]
long_list = ["longitude"]
pop_density = ["population_2020"]
df = pd.read_csv("C:\\Users\Sarin\Downloads\population_vnm_2018-10-01.csv", usecols= lat_list)
df1 = pd.read_csv("C:\\Users\Sarin\Downloads\population_vnm_2018-10-01.csv", usecols = long_list)
df2 = pd.read_csv("C:\\Users\Sarin\Downloads\population_vnm_2018-10-01.csv", usecols = pop_density)
print(df);
xdata = df.to_numpy()
xdata = xdata[0::1250]
ydata = df1.to_numpy()
ydata = ydata[0::1250]
zdata = df2.to_numpy()
zdata = zdata[0::1250]
##df1 = df.iloc[:, :100]

##longitude = df1.to_list()
##latitude = df.to_list();

##plt.scatter(df, df1)
##plt.style.use('seaborn-whitegrid')
##plt.show()

##plt.figure(figsize = (8,8))
##m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
##m.bluemarble(scale=0.5);

##zdata = 15 * np.random.random(100)
##xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
##ydata = np.cos(zdata) + 0.1 * np.random.randn(100)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.scatter3D(xdata, ydata, zdata)
plt.xlabel("x");
plt.ylabel("y");
plt.figure(figsize=(3,3))
ax.set_zlabel("z");
plt.show()
