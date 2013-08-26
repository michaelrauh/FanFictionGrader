from metrics import * #all function defs are here
import string
import os
import pickle
word_list = set(read_to_list('data/wordlist.txt')) #read dictionary
file_names = []
favs=[]
names = read_to_string('data/names.txt')
names = names.split('\n')
directory = os.listdir('data/fics') #all filenames actually present in directory
# Add filenames and number of favorites if file is present. Print names of missing files
not_found = 0
for i in range (0,len(names) -1,2):
    if names[i+1] + '.txt' in directory:
        favs.append(names[i])
        file_names.append(names[i+1])
    else:
        #print(names[i+1] + ' not found')
        not_found += 1
print (str(not_found) + ' files not found')
files=[] #all files
j = 0
for i in file_names:
    j+=1
    print(j)
    document = read_to_string('data/fics/' + i + '.txt')
    if len(document) > 10000:
        document = document[0:10000]
    files.append(document) 
all_coordinates =[]
i = 0
for doc in files:
    #helpers
    coordinates = []
    length=float(get_length(doc))
    sentence_lengths = sentence_length_list(doc) # get list of sentence lengths
    paragraph_lengths = paragraph_length_list(doc) #get paragraph lengths
    doc_list = nltk.word_tokenize(doc) #split doc into list of words
    tags = lexical_tags_list (doc) #get tags
    doc_set = set(doc) #convert doc to set
    #reused metrics
    avg_sentence_length = get_avg_sentence_length(sentence_lengths)
    coordinates.append(avg_sentence_length)
    avg_syllables_per_word = get_avg_syllables_per_word(doc_list)
    coordinates.append(avg_syllables_per_word)
    avg_paragraph_length = get_avg_paragraph_length (paragraph_lengths)
    coordinates.append(avg_paragraph_length)
    sentence_length_var = get_sentence_length_var(sentence_lengths,avg_sentence_length)
    coordinates.append(sentence_length_var)
    #tag counts
    possible_tags = ('CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NS','NNP','NNPS','PDT','POS','PRP','PRP$','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WPS','WRB')
    for tag in possible_tags:
        coordinates.append(tags.count(tag)/length)
    #punctuation counts
    for mark in string.punctuation:
        coordinates.append(doc.count(mark)/length)
    #other metrics
    coordinates.append(get_paragraph_length_var(paragraph_lengths,avg_paragraph_length))
    coordinates.append(get_run_on_count(sentence_lengths,avg_sentence_length,sentence_length_var)/length)
    coordinates.append(get_bad_capitalization_count(doc)/length)
    coordinates.append(get_flesch_kincaid(len(doc_list),len(sentence_lengths),avg_syllables_per_word))
    coordinates.append(get_word_repitition_count(doc_list)/length)
    coordinates.append(get_lexical_count(doc_set)/length)
    coordinates.append(get_non_dictionary_word_count(doc_set,word_list)/length)
    all_coordinates.append(coordinates)
    print (i)
    i+=1

pickle.dump(all_coordinates,open("data/coordinates.p","wb"))
pickle.dump(favs,open("data/favorites.p","wb"))
