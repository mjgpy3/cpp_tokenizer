#!/usr/bin/env python

"""
    A module designed to handle tokenizing C++ source files
"""

from sys import argv
import re

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

    # Get all the strings and chars from the code
    strings_and_chars = re.findall('".+"|\'.+?\'', code)

    # Place the "@sc@" token wherever we took chars or strings from in the code
    for replace_me in strings_and_chars:
        code = code.replace(replace_me, '@sc@')

    # Get rid of tab characters and split it into a list of lines
    lines = code.replace('\t', '').split('\n')
    words = []

    # Split up the lines into words
    for line in lines:
        words += [i for i in line.split(' ') if i]

    # Will store the "words" after they have been processed
    words_after_filters = []

    # Tokenize (split up) each word
    for word in words:
        words_after_filters += tokenize_word(word)

    i = 0

    # Place strings and chars back into their slots
    for (j, word) in enumerate(words_after_filters):
        if word == '@sc@':
            words_after_filters[j] = strings_and_chars[i]
            i += 1

    return words_after_filters

def tokenize_word(word):
    """
        Takes a single "word" and matches it agains the mother of regexes that
        splits it by various classifications
    """
    return re.findall('[\d\.]+|'+\
                      ';|,|==|=|#|'+\
                      '[<>\+-=%\*\^&\|]+|'+\
                      '\w+|\(|\)|{|}|\[|\]|@sc@|::', word)

def strip_comments_from_raw_code(code):
    """
        Still in progress, successfully strips by-line comments, needs to 
        strip multi-line
    """
    code = re.sub('//.*', '', code)
    #code = re.sub('\/\*[.\n]*\*\/', '', code)
    return code

def main():
    """
        Reads the passed source file, tokenized it and prints the tokens
    """
    code_read = try_read_code_from_arg1()
    code_read = strip_comments_from_raw_code(code_read)

    print "\n".join(tokenize_cpp_code(code_read))

if __name__ == '__main__':
    main()
