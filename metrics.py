import string
import math
#HELPERS
#read file into string
def read_to_string(filename):
    file = open(filename,'r')
    return file.read()

#read file into list of words
def read_to_list(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

#returns list of sentence lengths
def sentence_length_list(doc):
    sentences = doc.split('.')
    lengths = []
    for i in sentences:
        lengths.append(len(i))
    return lengths

#returns list of paragraph lengths
def paragraph_length_list(doc):
    paragraphs = doc.split('\t')
    lengths = []
    for i in paragraphs:
        lengths.append(len(i))
    return lengths

#This will be an nltk tagger call
def lexical_tags_list(doc):
    return [0,0]

#METRICS
#After document is read to string:
def get_length(document):
    return len(document)

def get_dialog_count(document):
    return document.count('\"')

def get_ellipsis_count(document):
    return document.count('...')

def get_parenthesis_count(document):
    return document.count('(')

def get_comma_count(document):
    return document.count (',')

def get_exclamation_count(document):
    return document.count('!')

def get_question_count(document):
    return document.count('?')

def get_avg_sentence_length(sentence_lengths):
    return sum(sentence_lengths)/len(sentence_lengths)

def get_sentence_length_var(sentence_lengths,avg_sentence_length):
    differences = [(x-avg_sentence_length)**2 for x in sentence_lengths]
    return math.sqrt(sum(differences)/len(sentence_lengths))

def get_common_error_count(doc):
    return doc.count('its the')

def get_banned_word_count(doc):
    return doc.count('throbbing')

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

def get_contraction_count(doc):
    return doc.count("\'s") + doc.count("n\'t") + doc.count("\'m") + doc.count("\'ve")+doc.count("\'d")+doc.count("\'ll")+doc.count("\'em")
#After Document is list of words:
def get_avg_syllables_per_word(doc):
    return 1
def get_flesch_kincaid(number_of_words,number_of_sentences,avg_syllables_per_word):
    return 206.835-1.015*(number_of_words/number_of_sentences) - 84.6 *(avg_syllables_per_word)
def get_word_repitition_count(document):
    count = 0
    for i in range (0,len(document)-1):
        if document[i] == document[i+1]:
            count +=1
    return count
def get_leading_word_count(doc):
    return doc.count('Anyway,') + doc.count('So,') + doc.count('Then,')
#After Lexical category tagging
def get_proper_noun_count(tags):
    return 0
def get_adverb_count(tags):
    return 0
def get_adjective_count(tags):
    return 0
def get_noun_count(tags):
    return 0
#After Document is set of words:
def get_lexical_count(document):
    return len(document)
#After dictionary words are removed:
def get_non_dictionary_word_count (words,word_list):
    return len(set(["foo","bar"]))

