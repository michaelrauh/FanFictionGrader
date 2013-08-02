from getstats import *
import random
import math
global total_f_score
global total_percent_correct
total_f_score = 0
total_percent_correct = 0
def get_distance(point_1,point_2):
    distance = 0
    for i in range (0,len(point_1)):
        distance +=((point_1[i] - point_2[i])**2)
    return math.sqrt(distance)
num_spam=get_num_spam()
coordinates=get_coordinates()
number_of_coordinates=len(coordinates)
for run in range (0,10):
    #get random indexes for test set. The rest is training
    range_of_files = range (0,number_of_coordinates)
    test_set = random.sample (range_of_files,number_of_coordinates/10)
    
    #set up metrics
    true_positive = 0.0
    false_positive = 0.0
    false_negative = 0.0
    true_negative = 0.0
    precision = 0.0
    recall = 0.0
    
    for i in test_set:
        current_coordinate=coordinates[i]
        distance_all_spam = 0
        distance_all_ham=0
        for point in range (0, len (coordinates)):
            if point not in test_set:
                is_spam=point<num_spam
                distance = get_distance(current_coordinate,coordinates[point])
                if is_spam:
                    distance_all_spam += math.sqrt(distance)
                else:
                    distance_all_ham += math.sqrt(distance)
        current_coordinate_guess = distance_all_spam<distance_all_ham
        current_coordinate_actual = i<num_spam

        if current_coordinate_guess: # if it is predicted to be spam
            if current_coordinate_actual: # if it is actually spam
                true_positive += 1
            else:
                false_positive += 1
        else: # it is predicted to be ham
            if current_coordinate_actual: # but it is actually spam
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
        total_f_score += f_score
    percent_correct = (true_positive + true_negative)/(true_positive + true_negative + false_positive + false_negative)
    total_percent_correct += percent_correct
# print average f score
print ("Average F score: ")
print(total_f_score/10)
print ("Average Percent correct: ")
print(total_percent_correct/10)
