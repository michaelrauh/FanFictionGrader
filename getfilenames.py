import os
def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]
filenames = os.listdir("data/badhp")
for file in filenames:
	file = 'data/badhp/' + file
	os.rename(file,file.replace(' ',''))
temp = os.listdir("data/badhp")
f = open("badhp.txt",'w')
for word in temp:
    f.write(word)
    f.write(' ')
f.close()

filenames = os.listdir("data/goodhp")
for file in filenames:
	file = 'data/goodhp/' + file
	os.rename(file,file.replace(' ',''))
temp = os.listdir("data/goodhp")
f = open("goodhp.txt",'w')
for word in temp:
    f.write(word)
    f.write(' ')
f.close()
