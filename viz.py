import nltk
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize

def get_paths(quality):
    return os.listdir(quality)

def get_file_contents(quality, filename):
    return open(quality + "/" + filename, 'r', encoding="utf-8").read()

def load_all_tags(contents):
    tokens = nltk.word_tokenize(contents)
    tag_tuples = nltk.pos_tag(tokens)
    tags = [thingy[1] for thingy in tag_tuples]
    return tags

all_tags = []
possible_tags = {}

for quality in ["good", "medium", "bad"]:
    for path in get_paths(quality):
        tags = load_all_tags(get_file_contents(quality, path))
        possible_tags = set.union(set(tags), possible_tags)
        all_tags.append(tags)

all_freqs = [[tags.count(tag)/len(tags) for tag in possible_tags] for tags in all_tags]
pca = PCA(n_components=2)
reduced = pca.fit_transform(all_freqs)
reduced = normalize(reduced)
x = [red[0] for red in reduced]
y = [red[1] for red in reduced]
colors = ["red" for i in range(10)] + ["yellow" for i in range(10)] + ["green" for i in range(10)]
plt.scatter(x,y,color=colors)
plt.show()
