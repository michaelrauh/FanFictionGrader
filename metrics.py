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

#returns unique words not in dictionary-This is currently catching proper nouns
def notfound (words,word_list):
    return set(["foo","bar"])
#returns list of length of each sentence
def sentence_length_list(doc):
    lengths = []
    count = 0
    for i in range(0,len(doc)):
        count +=1
        if doc[i] =='.':
            count =0
            lengths.append(count)
    return lengths
#returns list of chapter lengths
def chapter_length_list(doc):
    return [0,0]
def paragraph_length_list(doc):
    return [0,0]
def count_punctuation(doc): #this will get dialog,ellipsis,and parenthesis, with one linear sweep
    quotes = 0
    ellipses = 0
    parenthesis = 0
    commas = 0
    for i in range(0,len(doc)-3):
        if doc[i] == ',':
            commas +=1
        elif doc[i] == '(':
            parenthesis +=1
        elif doc[i] == '\"':
            quotes+=1
        elif doc[i] == '.' and doc[i+1] == '.' and doc[i+2] == '.':
            ellipses +=1
    return [quotes,ellipses,parenthesis,commas]
def lexical_tags_list(doc):
    return [0,0]
#METRICS
#After document is read to string:
def get_length(document):
    return len(document)
def get_dialog_count(punctuation):
    return punctuation
def get_ellipsis_count(punctuation):
    return punctuation
def get_parenthesis_count(punctuation):
    return punctuation
def get_comma_count(punctuation):
    return punctuation
def get_avg_sentence_length(sentence_lengths):
    return sum(sentence_lengths)/len(sentence_lengths)
def get_sentence_length_var(sentence_lengths,avg_sentence_length):
    differences = [(x-avg_sentence_length)**2 for x in sentence_lengths]
    return math.sqrt(sum(differences)/len(sentence_lengths))
def get_common_error_count(document):
    return 0
def get_banned_word_count(document):
    return 0
def get_repeated_punctuation_count(document):
    return 0
def get_avg_chapter_length(document):
    return 0
def get_chapter_length_var(document):
    return 0
def get_long_chapter_count(chapter_lengths):
    return 0
def get_avg_paragraph_length(paragraph_lengths):
    return 0
def get_paragraph_length_var(paragraph_lengths,avg_paragraph_length):
    return 0
def get_run_on_count(sentence_lengths):
    return 0
def get_bad_capitalization_count(document):
    return 0
def get_contraction_count(doc):
    return doc.count("\'s") + doc.count("n\'t") + doc.count("\'m") + doc.count("\'ve")+doc.count("\'d")+doc.count("\'ll")+doc.count("\'em")
#After Document is list of words:
def get_non_said_quote_count(document,dialog_count):
    return 0
def get_avg_syllables_per_word(document):
    return 0
def get_flesch_kincaid(number_of_words,number_of_sentences,avg_syllables_per_word):
    return 206.835-1.015*(number_of_words/number_of_sentences) - 84.6 *(avg_syllables_per_word)
def get_word_repitition_count(document):
    count = 0
    for i in range (0,len(document)-1):
        if document[i] == document[i+1]:
            count +=1
    return count
def get_leading_word_count(document):
    return 0
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
def get_spelling_error_count(document,non_dictionary_words):
    return 0
def get_made_up_word_count(document,non_dictionary_words):
    return 0
