import os
import subprocess
import time


#---- JARO ----#

def jaro_similarity(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 1.0

    match_distance = max(len(s1), len(s2)) // 2 - 1
    s1_matches = [False] * len(s1)
    s2_matches = [False] * len(s2)

    matches = 0
    transpositions = 0

    for i in range(len(s1)):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len(s2))

        for j in range(start, end):
            if s1[i] == s2[j] and not s2_matches[j]:
                s1_matches[i] = True
                s2_matches[j] = True
                matches += 1
                break

    if matches == 0:
        return 0.0

    k = 0
    for i in range(len(s1)):
        if s1_matches[i]:
            while not s2_matches[k]:
                k += 1
            if s1[i] != s2[k]:
                transpositions += 1
            k += 1

    return (matches / len(s1) + matches / len(s2) + (matches - transpositions / 2) / matches) / 3


def jaro_winkler_similarity(s1, s2, p=0.1):
    jaro_score = jaro_similarity(s1, s2)

    prefix_length = 0
    for i in range(min(4, min(len(s1), len(s2)))):
        if s1[i] == s2[i]:
            prefix_length += 1
        else:
            break

    return jaro_score + prefix_length * p * (1 - jaro_score)

#---- LEVENSHTEIN ----#

def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1], distances[index1 + 1], new_distances[-1])))
        distances = new_distances
    return distances[-1]


##--SIMILAR---#

def get_similar(input_word, database, similarity_type):
    most_similar_word = None
    if similarity_type == 'jaro':
        max_similarity = 0
        for word in database:
            similarity = jaro_similarity(input_word, word)
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_word = word
    elif similarity_type == 'jaro_winkler':
        max_similarity = 0
        for word in database:
            similarity = jaro_winkler_similarity(input_word, word)
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_word = word
    elif similarity_type == 'levenshtein':
        min_distance = float('inf')
        for word in database:
            distance = levenshtein_distance(input_word, word)
            if distance < min_distance:
                min_distance = distance
                most_similar_word = word
    return most_similar_word




