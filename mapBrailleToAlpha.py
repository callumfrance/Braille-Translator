# Contains dictionaries that map braille to English letters.

# http://www.duxburysystems.org/ximages/ueb_black8.pdf?type=8

# https://docs.python.org/3/library/functions.html#chr
# http://jrgraphix.net/r/Unicode/2800-28FF
# https://www.rapidtables.com/convert/number/hex-to-decimal.html

# https://en.wikipedia.org/wiki/Braille_pattern_dots-0

'''
This is map braille to alpha, so most of the new ones have to be redone
'''

import contractions

# the alphabet
letters_B2A = {
        chr(10241): 'a',
        chr(10243): 'b',
        chr(10249): 'c',
        chr(10265): 'd',
        chr(10257): 'e',
        chr(10251): 'f',
        chr(10267): 'g',
        chr(10259): 'h',
        chr(10250): 'i',
        chr(10266): 'j',
        chr(10245): 'k',
        chr(10247): 'l',
        chr(10253): 'm',
        chr(10269): 'n',
        chr(10261): 'o',
        chr(10255): 'p',
        chr(10271): 'q',
        chr(10263): 'r',
        chr(10254): 's',
        chr(10270): 't',
        chr(10277): 'u',
        chr(10279): 'v',
        chr(10298): 'w',
        chr(10285): 'x',
        chr(10301): 'y',
        chr(10293): 'z',
        }

contractions_B2A = {
        chr(10293): 'as',
        chr(10243): 'but',
        chr(10249): 'can',
        chr(10265): 'do',
        chr(10257): 'every',
        chr(10251): 'from',
        chr(10267): 'go',
        chr(10259): 'have', # rem ?
        chr(10278): 'his',
        chr(10260): 'in',
        chr(10285): 'it',
        chr(10266): 'just',
        chr(10280): 'knowledge', # rem ?
        chr(10296): 'like',
        chr(10253): 'more',
        chr(10269): 'not',
        chr(10255): 'people',
        chr(10271): 'quite',
        chr(10263): 'rather',
        chr(10254): 'so',
        chr(10270): 'that',
        chr(10262): 'to',
        chr(10277): 'us',
        chr(10279): 'very',
        chr(10292): 'was',
        chr(10298): 'will',
        chr(10301): 'you',
        }

numbers_B2A = {
        chr(10241): '1',
        chr(10243): '2',
        chr(10249): '3',
        chr(10265): '4',
        chr(10257): '5',
        chr(10251): '6',
        chr(10267): '7',
        chr(10259): '8',
        chr(10250): '9',
        chr(10266): '0',
        }

punctuation_B2A = {
        chr(10242): ',',
        chr(10246): ';',
        chr(10258): ':',
        chr(10290): '.',
        chr(10262): '!',
        chr(10294): '()',
        chr(10278): '“',
        chr(10292): '”',
        chr(10252): '/',
        chr(10300): '#',
        chr(10244): '\'',
        chr(10276): '-',
        }
