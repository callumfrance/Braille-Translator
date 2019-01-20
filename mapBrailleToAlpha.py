# Contains dictionaries that map braille to English letters.

# http://www.duxburysystems.org/ximages/ueb_black8.pdf?type=8

# https://docs.python.org/3/library/functions.html#chr
# http://jrgraphix.net/r/Unicode/2800-28FF
# https://www.rapidtables.com/convert/number/hex-to-decimal.html

# https://en.wikipedia.org/wiki/Braille_pattern_dots-0

'''
This is map braille to alpha, so most of the new ones have to be redone
'''

# the alphabet
letters_A = {
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


# these are things that can be within a bigger word (or their own word)
# that are aliased
sub_aliases = {
        'about'       : 'ab',
        'above'       : 'abv',
        'according'   : 'ac',
        'across'      : 'acr',
        'after'       : 'af',
        'afternoon'   : 'afn',
        'afterward',  : 'afw',
        'again',      : 'ag',
        'against',    : 'ag' + chr(10252),
        'almost',     : 'alm',
        'already',    : 'alr',
        'also',       : 'al',
        'although',   : 'al' + chr(10297),
        'altogether', : 'alt',
        'always',     : 'alw',
        'because',    : chr(10246) + 'c',
        'before',     : chr(10246) + 'f',
        'behind',     : chr(10246) + 'h',
        'beneath',    : chr(10246) + 'n',
        'beside',     : chr(10246) + 's',
        'between',    : chr(10246) + 't',
        'beyond',     : chr(10246) + 'y',
        'blind',      : 'bl',
        'braille',    : 'brl',
        'cannot',     : chr(10296) + 'c',
        'character',  : chr(10256) + chr(10273),
        'children',   : chr(10273) + 'n',
        'conceive',   : chr(10258) + 'cv',
        'conceiving', : chr(10258) + 'cvg',
        'could',      : 'cd',
        'day',        : chr(10256) + 'd',
        'deceive',    : 'dcv',
        'deceivng',   : 'dcvg',
        'declare',    : 'dcl',
        'declaring',  : 'dclg',
        'either',     : 'ei',
        'en',         : chr(10274),
        'ever',       : chr(10256) + 'e',
        'father',     : chr(10256) + 'f',
        'first',      : 'f' + chr(10252),
        'for',        : chr(10303),
        'friend',     : 'fr',
        'good',       : 'gd',
        'great',      : 'grt',
        'had',        : chr(10296) + 'h',
        'here',       : chr(10256) + 'h',
        'herself',    : 'h' + chr(10299) + 'f',
        'him',        : 'hm',
        'himself',    : 'hmf',
        'immediate',  : 'imm',
        'itself',     : 'xf',
        'know',       : chr(10256) + 'k',
        'letter',     : 'lr',
        'little',     : 'll',
        'lord',       : chr(10256) + 'l',
        'many',       : chr(10296) + 'm',
        'mother',     : chr(10256) + 'm',
        'much',       : 'm' + chr(10273),
        'must',       : 'm' + chr(10252),
        'myself',     : 'myf',
        'name',       : chr(10256) + 'n',
        'necessary',  : 'nec',
        'neither',    : 'nei',
        'of',         : chr(10295),
        'one',        : chr(10256) + 'o',
        'oneself',    : chr(10256) + 'of',
        'ought',      : chr(10256) + chr(10291),
        'ourselves',  : chr(10291) + 'rvs',
        'paid',       : 'pd',
        'part',       : chr(10256) + 'p',
        'perceive',   : 'p' + chr(10299) + 'cv',
        'perceiving', : 'p' + chr(10299) + 'cvg',
        'perhaps',    : 'p' + chr(10299) + 'h',
        'question',   : chr(10256) + 'q',
        'quick',      : 'qk',
        'receive',    : 'rcv',
        'receiving',  : 'rcvg',
        'rejoice',    : 'rjc',
        'rejoicing',  : 'rjcg',
        'right',      : chr(10256) + 'r',
        'said',       : 'sd',
        'should',     : chr(10281) + 'd',
        'some',       : chr(10256) + 's',
        'spirit',     : chr(10296) + 's',
        'such',       : 's' + chr(10273),
        'the',        : chr(10286),
        'their',      : chr(10296) + chr(10286),
        'themselves', : chr(10286) + 'mvs',
        'there',      : chr(10256) + chr(10286),
        'these',      : chr(10264) + chr(10286),
        'those',      : chr(10264) + chr(10297),
        'through',    : chr(10256) + chr(10297),
        'thyself',    : chr(10297) + 'yf',
        'time',       : chr(10256) + 't',
        'today',      : 'td',
        'together',   : 'tgr',
        'tomorrow',   : 'tm',
        'tonight',    : 'tn',
        'under',      : chr(10256) + 'u',
        'upon',       : chr(10264) + 'u',
        'where',      : chr(10256) + chr(10289),
        'whose',      : chr(10264) + chr(10289),
        'with',       : chr(10302),
        'word',       : chr(10264) + 'w',
        'work',       : chr(10256) + 'w',
        'world',      : chr(10296) + 'w',
        'would',      : 'wd',
        'young',      : chr(10256) + 'y',
        'your',       : 'yr',
        'yourself',   : 'yrf',
        'yourselves', : 'yrvs',
        }

# only used when the word stands alone or
# when followed by an apostrophe and one of the following end of words:
# ['d', 'll', 're', 's', 't', 've',]
# HOWEVER do not use when it is an acronym e.g. US for United States
alphabetic_wordsigns = {
        'but',         : 'b',
        'can',         : 'c',
        'do',          : 'd',
        'every',       : 'e',
        'from',        : 'f',
        'go',          : 'g',
        'have',        : 'h',
        'just',        : 'j',
        'knowledge',   : 'k',
        'like',        : 'l',
        'more',        : 'm',
        'not',         : 'n',
        'people',      : 'p',
        'quite',       : 'q',
        'rather',      : 'r',
        'so',          : 's',
        'that',        : 't',
        'us',          : 's',
        'very',        : 'v',
        'it',          : 'x',
        'you',         : 'y',
        'as',          : 'z',
        'will',        : 'w',
        }

# use the strong wordsign when standing alone
# or can be used when followed by apostrophe and one of these end of words
# ['d', 'll', 're', 's', 't', 've',]
strong_wordsigns = {
        'child',       : chr(10273),
        'shall',       : chr(10281),
        'this',        : chr(10297),
        'which',       : chr(10289),
        'out',         : chr(10291),
        'still',       : chr(10252),
        }

# use the strong contraction whenever it appears unless blocked by another rule
strong_contractions = {
        chr(10287): 'and',
        chr(10303): 'for',
        chr(10295): 'of',
        chr(10286): 'the',
        chr(10302): 'with',
        }

# use strong groupsigns wherever the letter it represents occur unless
# blocked by another rule
# however, these cannot be their own words. do not use for Sh!, St, Wh-? etc)
# 'ing' can only be used if it is not at the beginning of a word (ingenious vs. ginger)
strong_groupsigns = {
        'ch',         : chr(10273),
        'gh',         : chr(10275),
        'sh',         : chr(10281),
        'th',         : chr(10297),
        'wh',         : chr(10289),
        'ed',         : chr(10283),
        'er',         : chr(10299),
        'ou',         : chr(10291),
        'ow',         : chr(10282),
        'st',         : chr(10252),
        'ing',        : chr(10284),
        'ar',         : chr(10268),
        }

# use lower wordsigns
# [be, were, his, was,] can only be used standing alone, and
# not touching any punctuation sign
# 'enough' can also be used capitalized
# 'in' only occurs whenever it is in a sequence with an upper dot
''' need to check the rule for these to nail it down '''
lower_wordsigns = {
        'be',          : chr(10246),
        'enough',      : chr(10274),
        'were',        : chr(10294),
        'his',         : chr(10278),
        'in',          : chr(10260),
        'was',         : chr(10292),
        }

# [be, con, dis,] are used when they are prefixes only
# [ea, bb, cc, ff, gg] are used when they are middle only
# [en, in] are used wherever possible, but not when en is standing alone
lower_groupsigns = {
        'ea',          : chr(10242),
        'be',          : chr(10246),
        'bb',          : chr(10246),
        'con',         : chr(10258),
        'cc',          : chr(10258),
        'dis',         : chr(10290),
        'en',          : chr(10274),
        'ff',          : chr(10262),
        'gg',          : chr(10294),
        'in',          : chr(10260),
        }

initial_letter_contractions = (
        ilc_45,
        ilc_456,
        ilc_5,
        )

ilc_45 = {
        'upon'         : chr(),
        'these'         : chr(),
        'those'         : chr(),
        'whose'         : chr(),
        'word'         : chr(),
        }

ilc_456 = {
        'cannot'         : chr(),
        'had'         : chr(),
        'many'         : chr(),
        'spirit'         : chr(),
        'their'         : chr(),
        'world'         : chr(),
        }

ilc_5 = {
        'day'           : chr(),
        'ever'          : chr(),
        'father'        : chr(),
        'here'          : chr(),
        'know'          : chr(),
        'lord'          : chr(),
        'mother'        : chr(),
        'name'          : chr(),
        'one'           : chr(),
        'part'          : chr(),
        'question'      : chr(),
        'right'         : chr(),
        'some'          : chr(),
        'time'          : chr(),
        'under'         : chr(),
        'young'         : chr(),
        'there'         : chr(),
        'character'     : chr(),
        'through'       : chr(),
        'where'         : chr(),
        'ought'         : chr(),
        'work'          : chr(),
        }

# these are things that must be full words to get aliased
word_aliases = {
        'its',         : 'xs',
        }

contractions_A = {
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

punctuation_A = {
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

numbers_A = {
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
