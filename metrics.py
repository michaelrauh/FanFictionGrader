from __future__ import division
import string
import math
import nltk
from nltk.corpus import cmudict
#HELPERS
#read file into string
def read_to_string(filename):
    file = open(filename,'r')
    return file.read()

#read file into list of words
def read_to_list(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

#find number of syllables with nltk
from nltk.corpus import cmudict
d = cmudict.dict()
def syllables(word):
    if word in d:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]])
    else:
        return 0

#returns list of sentence lengths
def sentence_length_list(doc):
    sentences = doc.split('.')
    lengths = []
    for i in sentences:
        lengths.append(len(i))
    return lengths

#returns list of paragraph lengths
def paragraph_length_list(doc):
    paragraphs = doc.split('\n')
    lengths = []
    for i in paragraphs:
        lengths.append(len(i))
    return lengths

#This will be an nltk tagger call
def lexical_tags_list(doc):
    sentences = doc.split('.')
    tags = []
    i=0
    for sentence in sentences:
        i+=1
        tokens = nltk.word_tokenize(sentence)
        pairs = nltk.pos_tag(tokens)
        zipped = zip(*pairs)
        if (len(zipped) > 1):
            tags+=zipped[1]
    return tags

#METRICS
#After document is read to string:
def get_length(document):
    return len(document)

def get_avg_sentence_length(sentence_lengths):
    return sum(sentence_lengths)/float(len(sentence_lengths))

def get_sentence_length_var(sentence_lengths,avg_sentence_length):
    differences = [(x-avg_sentence_length)**2 for x in sentence_lengths]
    return math.sqrt(sum(differences)/len(sentence_lengths))

def get_avg_paragraph_length(paragraph_lengths):
    return sum(paragraph_lengths)/len(paragraph_lengths)

def get_paragraph_length_var(paragraph_lengths,avg_paragraph_length):
    differences = [(x-avg_paragraph_length)**2 for x in paragraph_lengths]
    return math.sqrt(sum(differences)/len(paragraph_lengths))

def get_run_on_count(sentence_lengths,avg_sentence_length,sentence_length_var):
    return sum([i>(avg_sentence_length + (3* sentence_length_var)) for i in sentence_lengths]) #This defines a run on in terms of avg and standard deviation

def get_bad_capitalization_count(doc):
    sentences = doc.split('.')
    count = 0
    for i in sentences:
        if len(i) > 0:
            if i[0].lower == i[0]:
                count +=1
    return count

#After Document is list of words:
def get_avg_syllables_per_word(doc):
    count = 0
    for word in doc:
        count += syllables(word)
    return count/len(doc)
def get_flesch_kincaid(number_of_words,number_of_sentences,avg_syllables_per_word):
    return 206.835-1.015*(number_of_words/number_of_sentences) - 84.6 *(avg_syllables_per_word)
def get_word_repitition_count(document):
    count = 0
    for i in range (0,len(document)-1):
        if document[i] == document[i+1]:
            count +=1
    return count
#After Document is set of words:
def get_lexical_count(document):
    return len(document)
def get_non_dictionary_word_count (words,word_list):
    extras = word_list.difference(words)
    return len(extras)

