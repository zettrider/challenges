'''
Read in dictionary.txt (a copy of /usr/share/dict/words on my Mac) and 
calculate the word that has the most value in Scrabble based on LETTER_SCORES 
which is imported in wordvalue-template.py.
'''

from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        words = f.read().splitlines()
    return words

def calc_word_value(WORD_SCRABBLE):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    WORD_VALUE = 0
    for letter in WORD_SCRABBLE:
        if letter.isalpha():
            WORD_VALUE += LETTER_SCORES[letter.upper()]
        else:
            continue
    return WORD_VALUE

def max_word_value(WORD_LIST = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    WORD_VALUE_DICT = {}
    for word in WORD_LIST:
        WORD_VALUE_DICT [word] = (calc_word_value(word))
    VALUE_LIST = list(WORD_VALUE_DICT.values())
    KEY_LIST = list(WORD_VALUE_DICT.keys())
    return KEY_LIST[VALUE_LIST.index(max(VALUE_LIST))]

if __name__ == "__main__":
    pass # run unittests to validate