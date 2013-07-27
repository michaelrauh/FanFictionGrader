import os
def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]
temp = os.listdir("data")
f = open("fics.txt",'w')
for word in temp:
    word = word.replace(" ","")
    f.write(word)
    f.write(' ')
f.close()
