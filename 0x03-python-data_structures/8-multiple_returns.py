#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if size == 0:
        first_character = 0, "None"
    else:
        first_character = size, sentence[0]
    return(first_character)
