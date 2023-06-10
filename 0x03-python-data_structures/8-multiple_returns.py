#!/usr/bin/python3
def multiple_returns(sentence):
    """a function for returning string length plus char 1st ."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
