import math

#read file into string
def read_to_string(filename):
    file = open(filename,'r')
    return file.read()

#read file into list of words
def read_to_list(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

#find the average sentence length, given a file in string format
def avg_sentence_length(document):
    periods = document.count('.')
    words = document.count(' ')
    return words/periods

word_list = read_to_list('data/wordlist.txt') #read dictionary
#returns unique words not in dictionary
def notfound (words,word_list = word_list):
    not_in_dictionary = []
    for word in words:
        posessive ="'s"
        word = word.strip(posessive)
        word = word.strip('-.,:?\'\"!').lower()
        if word not in word_list:
            not_in_dictionary.append(word)
    return list(set(not_in_dictionary))
    
spam_files = read_to_list('data/fics/badhp.txt')
ham_files = read_to_list('data/fics/goodhp.txt')

count = 0
for i in spam_files:
    count +=1
    document = read_to_string('data/fics/' + i)
    average_sentence_length = avg_sentence_length(document)
    fic_length = len(document)
    words = document.split()
    not_in_dictionary = notfound(words)
    print(not_in_dictionary)
