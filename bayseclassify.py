import random
import math
global total_f_score
global total_percent_correct

#set up variables for metrics
total_f_score = 0
total_percent_correct = 0

#Helper for reading files into lists
def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

#open listing, set up filenames
spam_files = read_words('data/fics/ficsbad.txt')
ham_files = read_words('data/fics/ficsgood.txt')
num_spam = len(spam_files)
num_ham = len(ham_files)

# Collect all documents into allD list, making sure that documents have no repeating words
# Read spam then ham. Category is based on position. If index<num_spam, then itis spam
i = 0
allD = []
for i in spam_files:
    D = list(set(read_words('data/fics/' + i)))
    allD.append(D)
for i in ham_files:
    D = list(set(read_words('data/fics/' + i)))
    allD.append(D)
number_of_files = len(allD)
#run entire algorithm ten times
for run in range (0,10):
    #get random indexes for test set. The rest is training
    range_of_files = range (0,number_of_files)
    test_set = random.sample (range_of_files,number_of_files/10)
    #reset di and dci
    di = {}
    spam_dict = {}
    ham_dict = {}
    dci = {}
    dci[False] = ham_dict
    dci[True] = spam_dict

    #for each document not in test set, for each word, increment count for word and category
    for i in range (0,len(allD)):
        if i not in test_set:
            for current_word in allD[i] :
                if current_word in di:
                    di[current_word] += 1
                else:
                    di[current_word] = 1
                spam_or_ham = i<num_spam
                if current_word in dci[spam_or_ham]:
                    dci[spam_or_ham][current_word] += 1
                else:
                    dci[spam_or_ham][current_word] = 1

    #set up metrics
    true_positive = 0.0
    false_positive = 0.0
    false_negative = 0.0
    true_negative = 0.0
    precision = 0.0
    recall = 0.0
    
    #for each test set document add up values for each word and take the greater.
    #Compare to actual values and increment appropriate metric
    for i in test_set:
        arg_max_ham = 0
        arg_max_spam = 0
        for current_word in allD[i]:
            #fill in zeroes where appropriate
            if current_word in dci[False]:
                num_doc_with_word_in_cat_ham = dci[False][current_word]
            else:
                num_doc_with_word_in_cat_ham = 0
            if  current_word in dci[True]:
                num_doc_with_word_in_cat_spam = dci[True][current_word]
            else:
                num_doc_with_word_in_cat_spam = 0
            if current_word in di:
                num_doc_with_word = di[current_word]
            else:
                num_doc_with_word = 0
            # calculate first values that get added for each word
            #ham
            numerator_ham = num_doc_with_word_in_cat_ham + 1
            denomenator_ham = num_doc_with_word + num_ham
            first_value_ham =(float(numerator_ham)/float(denomenator_ham))
            arg_max_ham += math.log(first_value_ham)
            #spam
            numerator_spam = num_doc_with_word_in_cat_spam + 1
            denomenator_spam = num_doc_with_word + num_spam
            first_value_spam =(float(numerator_spam)/float(denomenator_spam))
            arg_max_spam += math.log(first_value_spam)
        # add on second values that are added on for each document
        #ham
        second_value_ham = float((num_ham + 1))/float(((number_of_files) + 2))
        second_value_spam = float((num_spam + 1))/float(((number_of_files) + 2))
        #spam
        arg_max_ham += math.log(second_value_ham)
        arg_max_spam += math.log(second_value_spam)
        #check which is greater, and assign classification
        solution = (arg_max_spam/arg_max_ham) > .5
        #Tally up metrics by comparing to actual
        actual = i<num_spam
        if solution: # if it is predicted to be spam
            if actual: # if it is actually spam
                true_positive += 1
            else:
                false_positive += 1
        else: # it is predicted to be not spam
            if actual: # but it is actually spam
                false_negative += 1
            else:
                true_negative +=1
    #Add to f score, then total f score
    if (true_positive != 0 or false_positive !=0):
        precision = true_positive/(true_positive+false_positive)
    if (true_positive != 0 or false_negative != 0):
        recall = true_positive/(true_positive+false_negative)
    if (precision != 0 or recall != 0):
        f_score = 2 * ((precision * recall)/(precision + recall))
        percent_correct = (true_positive + true_negative)/(true_positive + true_negative + false_positive + false_negative)
        total_percent_correct += percent_correct
        total_f_score += f_score
# print average f score
print ("Average F score: ")
print(total_f_score/10)
print ("Average Percent correct: ")
print(total_percent_correct/10)

#1000 runs on spam/ham
#Average F score: 
#0.950071886806
#Average Percent correct: 
#0.982975778547
