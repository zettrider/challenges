#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
import copy

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    LETTERS_DRAWN = []
    for i in range (0, NUM_LETTERS):
        LETTERS_DRAWN.append(POUCH[random.randrange(98)])
    return LETTERS_DRAWN

def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    WORD_PLAYER = input("Form a valid word: ") 
    while _validation(WORD_PLAYER, draw) is not True:
        print("The provided word did not pass the validation, please try again!")
        WORD_PLAYER = input("Form a valid word: ")
    
    return WORD_PLAYER

def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    # 1. Validate using only the letters of the draw
    WORD_IS_VALID = True
    DRAW_VALID = copy.copy(draw)
    for letter in word:
        if letter.upper() in DRAW_VALID:
            DRAW_VALID.remove(letter.upper())
        else:
            WORD_IS_VALID = False
            # Added ValueErrors to pass the Tests. While not_true loop makes sure 
            # that only a valid combination will be accepted.
            # Unclear why ValueError is desireable here.
            #raise ValueError("Letters...")

    if word.lower() not in DICTIONARY:
        WORD_IS_VALID = False
        # Added ValueErrors to pass the Tests. While not_true loop makes sure 
        # that only a valid combination will be accepted.
        # Unclear why ValueError is desireable here.
        #raise ValueError("Words...")
    
    return WORD_IS_VALID

# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    POSSIBLE_WORDS_LIST = []

    for item in _get_permutations_draw(draw):
        if item.lower() in DICTIONARY:
            POSSIBLE_WORDS_LIST.append(item)

    return POSSIBLE_WORDS_LIST


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    PERMUTATION_LIST = []
    MERGED_PERMUTATION_LIST = []

    for i in range(1, NUM_LETTERS + 1):
        PERMUTATION_LIST.append(list(map("".join, itertools.permutations(draw, i))))

    for i in range (0, len(PERMUTATION_LIST)):
        MERGED_PERMUTATION_LIST += PERMUTATION_LIST[i]

    return MERGED_PERMUTATION_LIST
    

# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()