import matplotlib.pyplot as plt

img = plt.imread("C:\\Users\Sarin\Downloads\hanoiflipped.jpg")
plt.figure()

x = [1,2,3]
y = [4,5,6]

# bottom left
# 21.013415, 105.849094

# bottom right
# 21.022155, 105.849094

# top left
# 21.013415, 105.848701

# top right
# 21.022155, 105.848701

plt.imshow(img)
plt.ylim(0,1535)
plt.scatter(x,y)
plt.show();
