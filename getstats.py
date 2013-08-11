from metrics import * #all function defs are here
word_list = set(read_to_list('data/wordlist.txt')) #read dictionary
spam_files = read_to_list('data/fics/badhp.txt') #spam file names
ham_files = read_to_list('data/fics/goodhp.txt') #ham file names
files=[] #all files. Spam then ham
num_spam = len(spam_files) #files before this index are spam
for i in spam_files:
    document = read_to_string('data/fics/' + i)
    files.append(document)
for i in ham_files:
    document = read_to_string('data/fics/' + i)
    files.append(document)
    
all_coordinates =[]
for doc in files:
    #helpers
    coordinates = []
    length=float(get_length(doc))
    sentence_lengths = sentence_length_list(doc) # get list of sentence lengths
    paragraph_lengths = paragraph_length_list(doc) #get paragraph lengths
    doc_list = nltk.word_tokenize(doc) #split doc into list of words
    tags = lexical_tags_list (doc_list) #get tags
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
    possible_tags = ('CC','CD','DT','EX','FW','IN','JJ','JJR','JJS','LS','MD','NN','NS','NNP','NNPS','PDT','POS','PRP','PRP$','RB','RBR','RBS','RP','SYM','TO','UH','VB','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WPS','WRB','\"','...','(',',','!','?',';',':')
    for tag in possible_tags:
        coordinates.append(doc_list.count(tag)/length)
    #other metrics
    coordinates.append(get_paragraph_length_var(paragraph_lengths,avg_paragraph_length))
    coordinates.append(get_run_on_count(sentence_lengths,avg_sentence_length,sentence_length_var)/length)
    coordinates.append(get_bad_capitalization_count(doc)/length)
    coordinates.append(get_flesch_kincaid(len(doc_list),len(sentence_lengths),avg_syllables_per_word))
    coordinates.append(get_word_repitition_count(doc_list)/length)
    coordinates.append(get_lexical_count(doc_set)/length)
    coordinates.append(get_non_dictionary_word_count(doc_set,word_list)/length)
    all_coordinates.append(coordinates)
