from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\Sarin\Downloads\pioneerandPropser\PioneerandProsper\files\train.csv").to_numpy();
clf = DecisionTreeClassifier();

xtrain = data[:21000,1:];
train_label = data[0:21000,0];

clf.fit(xtrain,train_label);

xtest = data[21000:,1:]
actual_label = data[21000:,0];

for i in range(50,55):
    d = xtest[i];
    d.shape = (28,28);
    print(clf.predict([xtest[i]]));
    plt.imshow(d,cmap='gray');
    plt.show();

p = clf.predict(xtest);

count = 0;
for i in range(0, 21000):
    count +=1 if p[i] == actual_label[i] else 0
print((count/21000)*100)
