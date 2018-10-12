#! /usr/bin/python3.7

import random

def create_random_string():

    random_string = ''

    #populate 28 chars (0 index) string
    while len(random_string) < 28:
        random_string += random.choice(char_list)

    return random_string



def score_random_string(test_string):
    amnt_correct = 0
    counter = 0

    while counter < len(goal_string):
        if goal_string[counter] == test_string[counter]:
            amnt_correct += 1

        counter += 1

    #return % correct aka 'score'
    return round((amnt_correct / len(goal_string)) * 100, 4)



def generate_and_score():
    temp_random = ''
    temp_score = 0.0
    tries = 0

    temp_random = create_random_string()

    while temp_score != 100.0:
        temp_score = score_random_string(temp_random)
        tries += 1

        if tries % 100 == 0:
            print('tries: {} --- temp_random: {} --- temp_score: {}'.format(
                tries, temp_random, temp_score
            ))

        #update temp_random
        temp_random = update_generated_string(temp_random)

    return temp_score, temp_random



def update_generated_string(generated_string):
    char_counter = 0
    temp_list = list(generated_string)
    for i in goal_string:
        if i != temp_list[char_counter]:
            temp_list[char_counter] = random.choice(char_list)
            break
        else:
            char_counter += 1

    return "".join(temp_list)



goal_string = 'methinks it is like a weasel'
random_generated_string = ''
string_score = ''
char_list = [' ']

#append ascii chars to char list
#char list now contains a space and all lowercase chars a-z
for i in range(97, 123):
    char_list.append(chr(i))

string_score, random_generated_string = generate_and_score()
print('Score: {} --- String: {}'.format(string_score, random_generated_string))
