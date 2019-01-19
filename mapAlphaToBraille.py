# Contains dictionaries that map English letters to braille.

# http://www.duxburysystems.org/ximages/ueb_black8.pdf?type=8

letters_B = {al : br for br, al in mapBrailleToAlpha.letters_A.items()}

contractions_B = {al : br for br, al in mapBrailleToAlpha.contractions_A.items()}

numbers_B = {al : br for br, al in mapBrailleToAlpha.numbers_A.items()}

punctuation_B = {al : br for br, al in mapBrailleToAlpha.punctuation_A.items()}

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
