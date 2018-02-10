from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# We load the data with load_iris from sklearn
data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data.target_names
labels = target_names[target]

# for t, marker, c in zip(range(3), ">ox", "rgb"):
#     # We plot each class on its own to get different colored markers
#     plt.scatter(features[target == t, 0],
#                 features[target == t, 1],
#                 marker=marker,
#                 c=c)
plength = features[:, 2]
# use numpy operations to get setosa features

is_setosa = (labels == 'setosa')
# This is the important step:
max_setosa = plength[is_setosa].max()

features = features[~is_setosa]
labels = labels[~is_setosa]
virginica = (labels == 'virginica')

best_acc = -1.0
for fi in range(features.shape[1]):
    # We are going to generate all possible threshold for this feature
    thresh = features[:, fi].copy()
    thresh.sort()
    # Now test all thresholds:
    for t in thresh:
        pred = (features[:, fi] > t)
        acc = (pred == virginica).mean()
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
        best_t = t
if example[best_fi] > t:
    print('virginica')
else:
    print('versicolor')