import os
import sys
import scipy as sp
from matplotlib.mlab import dist
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)

# content = ["How to format my hard disk", " Hard disk format problems "]
# X = vectorizer.fit_transform(content)
# print(vectorizer.get_feature_names())
# print(X.toarray().transpose())

DIR = "./data"
posts = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]
print(posts)
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape
print("#samples: %d, #features: %d" % (num_samples, num_features))
print(vectorizer.get_feature_names())

new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])


def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())


best_doc = None
best_dist = sys.maxsize
best_i = None
for i in range(0, num_samples):
    post = posts[i]
    if post == new_post:
        continue

post_vec = X_train.getrow(i)

d = dist(post_vec, new_post_vec)

print("=== Post %i with dist=%.2f: %s" % (i, d, post))

if d < best_dist:
    best_dist = d
    best_i = i
    print("Best post is %i with dist=%.2f" % (best_i, best_dist))
