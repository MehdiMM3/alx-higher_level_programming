#!/usr/bin/python3
def multiple_returns(sentence):
    asd = len(sentence)
    if asd == 0:
        first_char = None
    else:
        first_char = sentence[0]

    return (asd, first_char)
