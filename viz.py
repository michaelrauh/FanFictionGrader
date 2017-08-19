import nltk
import os
import matplotlib.pyplot as plt

colors = {"bad": "red", "medium": "yellow", "good": "green"}
all_data = []
for quality in colors.keys():
    all_freqs = []
    for filename in os.listdir(quality):
        contents = open(quality + "/" + filename, 'r', encoding="utf-8").read()
        tokens = nltk.word_tokenize(contents)
        tag_tuples = nltk.pos_tag(tokens)
        tags = [thingy[1] for thingy in tag_tuples]
        possible_tags = sorted(list(set(tags)))
        number_of_words = len(tags)
        freqs = [tags.count(tag)/number_of_words for tag in possible_tags]
        all_freqs.append(freqs)
        
    rotated = list(zip(*all_freqs[::-1]))
    all_data.append(rotated)

for x in range(3):
    rotated = all_data[x]
    for i in range(len(rotated)):
        plt.scatter(rotated[i], [i] * len(rotated[i]), color = list(colors.values())[x])
plt.xlim(0, .15)
plt.ylim(0, 40)
plt.show()
