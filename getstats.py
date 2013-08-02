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
def get_num_spam():
    return num_spam
def get_coordinates():
    all_coordinates =[]
    for doc in files:
        length=get_length(doc)
        punctuation = count_punctuation(doc) # get list of punctuation counts
        dialog_density = get_dialog_count(punctuation[0])/length
        ellipsis_density = get_ellipsis_count(punctuation[1])/length
        parenthesis_density = get_parenthesis_count(punctuation[2])/length
        comma_density = get_comma_count(punctuation[3])/length
        sentence_lengths = sentence_length_list(doc) # get list of sentence lengths
        avg_sentence_length=get_avg_sentence_length(sentence_lengths)
        sentence_length_var = get_sentence_length_var(sentence_lengths,avg_sentence_length)
        common_error_density = get_common_error_count(doc)/length
        banned_word_density = get_banned_word_count(doc)/length
        repeated_punctuation_density = get_repeated_punctuation_count(doc)/length
        chapter_lengths = chapter_length_list(doc) # get list of chapter lengths
        avg_chapter_lengths = get_avg_chapter_length(doc)
        chapter_length_var = get_chapter_length_var(doc)
        long_chapter_density = get_long_chapter_count(chapter_lengths)/length
        paragraph_lengths = paragraph_length_list(doc) #get paragraph lengths
        avg_paragraph_length = get_avg_paragraph_length (paragraph_lengths)
        paragraph_length_var = get_paragraph_length_var(paragraph_lengths,avg_paragraph_length)
        run_on_density = get_run_on_count(doc)/length
        bad_capitalization_density = get_bad_capitalization_count(doc)/length
        contraction_density = get_contraction_count(doc)/length
        non_said_quote_density = get_non_said_quote_count(doc)/length
        doc = doc.split() #split doc into list of words
        avg_syllables_per_word = get_avg_syllables_per_word(doc)
        flesch_kincaid = get_flesch_kincaid(len(doc),len(sentence_lengths),avg_syllables_per_word)
        word_repitition_density = get_word_repitition_count(doc)/length
        leading_word_density = get_leading_word_count(doc)/length
        tags = lexical_tags_list (doc)
        proper_noun_density = get_proper_noun_count(tags)/length
        adverb_density = get_adverb_count(tags)/length
        adjective_density = get_adjective_count(tags)/length
        noun_density = get_noun_count(tags)/length
        doc = set(doc) #convert doc to set
        lexical_density = get_lexical_count(doc)/length
        non_dictionary_words = notfound(doc,word_list) #get non-dictionary words
        spelling_error_density = get_spelling_error_count(doc,non_dictionary_words)/length
        made_up_word_density = get_made_up_word_count(doc,non_dictionary_words)/length

        #put into a single coordinate. Final version will remove names
        coordinates1 = [length,dialog_density,ellipsis_density,parenthesis_density]
        coordinates2 = [comma_density,avg_sentence_length,sentence_length_var,common_error_density,banned_word_density,repeated_punctuation_density]
        coordinates3 = [avg_chapter_lengths,chapter_length_var,long_chapter_density,avg_paragraph_length,paragraph_length_var,run_on_density]
        coordinates4 = [bad_capitalization_density,contraction_density,non_said_quote_density,avg_syllables_per_word,flesch_kincaid]
        coordinates5 = [word_repitition_density,leading_word_density,proper_noun_density,adverb_density,adjective_density,noun_density]
        coordinates6 = [lexical_density,spelling_error_density,made_up_word_density]
        coordinates = coordinates1 + coordinates2 +coordinates3 +coordinates4 +coordinates5 +coordinates6
        all_coordinates.append(coordinates)
    return all_coordinates
