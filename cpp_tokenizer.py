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
    lines = code.replace('\t', '').split('\n')
    words = []

    # Split up the lines into words
    for line in lines:
        words += [i for i in line.split(' ') if i]

    words_after_filters = []

    for word in words:
        words_after_filters += process_word(word)

    return rejoin_strings(words_after_filters)

def process_word(word):
    """
        Takes a single "word" and matches it agains the mother of regexes that
        splits it by various classifications
    """
    return re.findall('[\d\.]+|'+\
                      ';|,|==|=|#|\'.+?\'|'+\
                      '[<>\+-=%\*\^&\|]+|'+\
                      '\w+|\(|\)|{|}|\[|\]|\"|::', word)

def strip_comments_from_raw_code(code):
    """
        Still in progress, successfully strips by-line comments, needs to 
        strip multi-line
    """
    code = re.sub('//.*', '', code)
    #code = re.sub('\/\*[.\n]*\*\/', '', code)
    return code

def join_between_char(words, char):
    """
        Takes a list of words and a character and only joins together lists
        of words between that character
    """
    currently_joining = False
    stringed_words = []
    result = []

    for word in words:
        if word == char:
            currently_joining = not currently_joining
            if not currently_joining:
                result.append(char + " ".join(stringed_words) + char)
                stringed_words = []
        else:
            if currently_joining:
                stringed_words.append(word)
            else:
                result.append(word)

    return result

def rejoin_strings(words):
    """
        Parses through a list of words that were priorly split by ' ' and
        attempts to rejoin strings
    """

    return join_between_char(words, '"')

def main():
    """
        Reads the passed source file, tokenized it and prints the tokens
    """
    code_read = try_read_code_from_arg1()
    code_read = strip_comments_from_raw_code(code_read)

    print tokenize_cpp_code(code_read)

if __name__ == '__main__':
    main()
