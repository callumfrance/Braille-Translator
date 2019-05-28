# Contains dictionaries that map English letters to braille.

# http://www.duxburysystems.org/ximages/ueb_black8.pdf?type=8

import mapBrailleToAlpha

''' Mappings for letters, contractions, numbers, and punctuation have already
    been defined in `mapBrailleToAlpha.py`.
    So instead of redoing all of that work, the below reverse maps them.
'''
letters_A2B = {al : br for br, al in mapBrailleToAlpha.letters_B2A.items()}
contractions_A2B = {al : br for br, al in mapBrailleToAlpha.contractions_B2A.items()}
numbers_A2B = {al : br for br, al in mapBrailleToAlpha.numbers_B2A.items()}
punctuation_A2B = {al : br for br, al in mapBrailleToAlpha.punctuation_B2A.items()}

# Some punctuation rules work differently and as such are listed here
punctuation = {
               '(': chr(10294), # fix bracket two-way
               ')': chr(10294),
               '?': chr(10278), # check validity
               '…': chr(10290) + chr(10290) + chr(10290),
               '’': chr(10244),
               '­': chr(10276),
               '-': chr(10276),
               '‐': chr(10276),
               '‑': chr(10276),
               '‒': chr(10276),
               '–': chr(10276),
               '—': chr(10276),
               '―': chr(10276)}
