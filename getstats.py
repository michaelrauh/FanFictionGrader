import math
import string

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
#returns unique words not in dictionary-This is currently catching proper nouns
def notfound (words,word_list = word_list):
    for i in range(0,len(words)):
        strip_words = "'s" + string.punctuation
        words[i] = words[i].strip(strip_words).lower()
    return set(words).difference(word_list)
    
spam_files = read_to_list('data/fics/badhp.txt')
ham_files = read_to_list('data/fics/goodhp.txt')

for i in spam_files:
    document = read_to_string('data/fics/' + i)
    average_sentence_length = avg_sentence_length(document)
    fic_length = len(document)
    words = document.split()
    not_in_dictionary = notfound(words)
