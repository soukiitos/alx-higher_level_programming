#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for dlm in "?:.":
        words = (dlm + "\n\n").join([i.strip(" ") for i in words.split(dlm)])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
