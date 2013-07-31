import string
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
    return [0,0]
#returns list of chapter lengths
def chapter_length_list(doc):
    return [0,0]
def paragraph_length_list(doc):
    return [0,0]
def count_punctuation(doc): #this will get dialog,ellipsis,and parenthesis, with one linear sweep
    return [0,0,0,0]
def lexical_tags_list(doc):
    return [0,0]
#METRICS
#After document is read to string:
def get_length(document):
    return 1
def get_dialog_count(punctuation):
    return 0
def get_ellipsis_count(punctuation):
    return 0
def get_parenthesis_count(punctuation):
    return 0
def get_comma_count(document):
    return 0
def get_avg_sentence_length(sentence_lengths):
    return 0
def get_sentence_length_var(sentence_lengths,avg_sentence_length):
    return 0
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
def get_run_on_count(document):
    return 0
def get_bad_capitalization_count(document):
    return 0
def get_contraction_count(document):
    return 0
def get_non_said_quote_count(document):
    return 0
#After Document is list of words:
def get_avg_syllables_per_word(document):
    return 0
def get_flesch_kincaid(doc_length,number_of_sentences,avg_syllables_per_word):
    return 0
def get_word_repitition_count(document):
    return 0
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
    return 0
#After dictionary words are removed:
def get_spelling_error_count(document,non_dictionary_words):
    return 0
def get_made_up_word_count(document,non_dictionary_words):
    return 0
