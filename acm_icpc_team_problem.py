#!/bin/python3

import math
import os
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topics):
    final_max_number_of_topics = 0
    number_of_ways_to_form = 0
    for first_counter in range(0,len(topics)):
        for second_coutner in range(first_counter+1,len(topics)):
            initial_max_number_of_topics = 0https://github.com/mani1soni/Python-Scripts
            for index in range(0, len(topics[first_counter])):
                if topics[first_counter][index] == "1" or topics[second_coutner][index] == "1":
                    initial_max_number_of_topics += 1
            if initial_max_number_of_topics > final_max_number_of_topics:
                final_max_number_of_topics = initial_max_number_of_topics
                number_of_ways_to_form = 0
            if initial_max_number_of_topics == final_max_number_of_topics:
                number_of_ways_to_form += 1

    answer = []
    answer.append(final_max_number_of_topics)
    answer.append(int(number_of_ways_to_form))
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

