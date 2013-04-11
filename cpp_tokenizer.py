#!/usr/bin/env python

"""
    A module designed to handle tokenizing C++ source files
"""

from sys import argv

def try_read_code_from_arg1():
    """
        Attempts to read the source file, if fails it will blow up
    """
    if len(argv) < 2:
        raise ValueError("Usage: ./cpp_tokenizer [cpp file]")

    try:
        with open(argv[1], 'r') as file_stream:
            return file_stream.read()
    except IOError:
        raise ValueError('File: "' + argv[1] + '" not found')

def tokenize_cpp_code(code):
    """
        Returns a list of tokens from the passed code
    """
    lines = code.replace('\t', '').split('\n')
    words = []

    for line in lines:
        words += [i for i in line.split(' ') if i]

    return rejoin_strings(words)

# re.findall('\w+|;|,', 'afasdf,bas,c;')
# re.findall('\w+|#|;|\++', '#include++')


def rejoin_strings(words):
    """
        Parses through a list of words that were priorly split by ' ' and
        attempts to rejoin strings
    """
    join_mode = False
    result = []

    for word in words:
        if join_mode:
            result[-1] += " " + word
        else:
            result.append(word)

        if word.count('"') == 2:
            continue

        if '"' in word:
            join_mode = not join_mode

    return result

if __name__ == '__main__':
    print tokenize_cpp_code(try_read_code_from_arg1())
