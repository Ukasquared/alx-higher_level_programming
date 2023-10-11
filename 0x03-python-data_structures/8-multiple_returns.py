#!/usr/bin/python3


def multiple_returns(sentence):
    len_t = len(sentence)
    if sentence:
        char = sentence[0]
        return (len_t, char)
    else:
        char = None
    return (len_t, char)
