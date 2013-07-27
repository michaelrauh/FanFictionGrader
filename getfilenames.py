import os
def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]
filenames = os.listdir("data/smallbadhp")
for file in filenames:
	file = 'data/smallbadhp/' + file
	os.rename(file,file.replace(' ',''))
temp = os.listdir("data/smallbadhp")
f = open("ficsbad.txt",'w')
for word in temp:
    f.write(word)
    f.write(' ')
f.close()
