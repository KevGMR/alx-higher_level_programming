#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    highest_score = 0
    highest_scorer = None

    for key, value in a_dictionary.items():
        if value > highest_score:
            highest_score = value
            highest_scorer = key

    return highest_scorer
