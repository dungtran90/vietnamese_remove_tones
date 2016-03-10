# -*- coding: utf-8 -*-
import re

REPLACES_DICT_STR = {
    '\xe1\xbb\x8b': 'i', '\xc3\x8a': 'e', '\xc3\x89': 'e', '\xc3\x88': 'e',
    '\xe1\xbb\x8f': 'o', '\xe1\xbb\x8e': 'o', '\xc3\x8d': 'i', '\xc3\x8c': 'i',
    '\xc3\x83': 'a', '\xc3\x82': 'a', '\xc3\x81': 'a', '\xc3\x80': 'a',
    '\xe1\xbb\x87': 'e', '\xe1\xbb\x86': 'e', '\xe1\xbb\x85': 'e',
    '\xe1\xbb\x84': 'e', '\xe1\xbb\x9b': 'o', '\xc3\x9a': 'u', '\xc3\x99': 'u',
    '\xe1\xbb\x88': 'i', '\xe1\xbb\x9f': 'o', '\xe1\xbb\x9e': 'o',
    '\xc3\x9d': 'y', '\xe1\xbb\x9c': 'o', '\xc3\x93': 'o', '\xc3\x92': 'o',
    '\xe1\xbb\x91': 'o', '\xe1\xbb\x90': 'o', '\xe1\xbb\x97': 'o',
    '\xe1\xbb\x96': 'o', '\xc3\x95': 'o', '\xc3\x94': 'o', '\xe1\xbb\xab': 'u',
    '\xc3\xaa': 'e', '\xc3\xa9': 'e', '\xc3\xa8': 'e', '\xe1\xbb\xaf': 'u',
    '\xe1\xbb\x8c': 'o', '\xc3\xad': 'i', '\xc3\xac': 'i', '\xc3\xa3': 'a',
    '\xc3\xa2': 'a', '\xc3\xa1': 'a', '\xc3\xa0': 'a', '\xe1\xbb\xa7': 'u',
    '\xe1\xbb\xa6': 'u', '\xe1\xbb\xa5': 'u', '\xe1\xbb\xa4': 'u',
    '\xc3\xba': 'u', '\xc3\xb9': 'u', '\xe1\xbb\xb8': 'y', '\xc3\xbd': 'y',
    '\xe1\xbb\x82': 'e', '\xc3\xb3': 'o', '\xc3\xb2': 'o', '\xe1\xbb\xb1': 'u',
    '\xe1\xbb\xb0': 'u', '\xe1\xbb\xb7': 'y', '\xe1\xbb\x81': 'e',
    '\xc3\xb5': 'o', '\xc3\xb4': 'o', '\xc6\xb0': 'u', '\xe1\xbb\xa0': 'o',
    '\xe1\xbb\x80': 'e', '\xe1\xbb\x8d': 'o', '\xe1\xbb\xb3': 'y',
    '\xe1\xbb\xb2': 'y', '\xe1\xbb\xb9': 'y', '\xe1\xba\xa8': 'a',
    '\xe1\xba\xa9': 'a', '\xe1\xba\xaa': 'a', '\xe1\xba\xab': 'a',
    '\xe1\xba\xac': 'a', '\xe1\xba\xad': 'a', '\xe1\xba\xae': 'a',
    '\xe1\xba\xaf': 'a', '\xe1\xba\xa0': 'a', '\xe1\xba\xa1': 'a',
    '\xe1\xba\xa2': 'a', '\xe1\xba\xa3': 'a', '\xe1\xba\xa4': 'a',
    '\xe1\xba\xa5': 'a', '\xe1\xba\xa6': 'a', '\xe1\xba\xa7': 'a',
    '\xe1\xba\xb8': 'e', '\xe1\xba\xb9': 'e', '\xe1\xba\xba': 'e',
    '\xe1\xba\xbb': 'e', '\xe1\xba\xbc': 'e', '\xe1\xba\xbd': 'e',
    '\xe1\xba\xbe': 'e', '\xe1\xba\xbf': 'e', '\xe1\xba\xb0': 'a',
    '\xe1\xba\xb1': 'a', '\xe1\xba\xb2': 'a', '\xe1\xba\xb3': 'a',
    '\xe1\xba\xb4': 'a', '\xe1\xba\xb5': 'a', '\xe1\xba\xb6': 'a',
    '\xe1\xba\xb7': 'a', '\xe1\xbb\x9d': 'o', '\xe1\xbb\x83': 'e',
    '\xe1\xbb\x93': 'o', '\xe1\xbb\xa9': 'u', '\xe1\xbb\x9a': 'o',
    '\xe1\xbb\x92': 'o', '\xc6\xa0': 'o', '\xc5\xa9': 'u', '\xc5\xa8': 'u',
    '\xc6\xa1': 'o', '\xe1\xbb\x99': 'o', '\xe1\xbb\x8a': 'i',
    '\xe1\xbb\x95': 'o', '\xe1\xbb\x94': 'o', '\xe1\xbb\xb6': 'y',
    '\xe1\xbb\xaa': 'u', '\xc4\x82': 'a', '\xc4\x83': 'a', '\xe1\xbb\x98': 'o',
    '\xe1\xbb\x89': 'i', '\xe1\xbb\xa8': 'u', '\xe1\xbb\xb5': 'y',
    '\xc4\x90': 'd', '\xc4\x91': 'd', '\xe1\xbb\xad': 'u', '\xc4\xa8': 'i',
    '\xc4\xa9': 'i', '\xe1\xbb\xac': 'u', '\xe1\xbb\xae': 'u',
    '\xe1\xbb\xa3': 'o', '\xe1\xbb\xa2': 'o', '\xe1\xbb\xb4': 'y',
    '\xc6\xaf': 'u', '\xe1\xbb\xa1': 'o'}


REPLACES_DICT_UNICODE = {
    u'\u1EF9': 'y', u'\u1EAF': 'a', u'\u1EAD': 'a', u'\u1EAE': 'a',
    u'\u0111': 'd', u'\u1EAC': 'a', u'\u1EAA': 'a', u'\u1EEB': 'u',
    u'\u1EEC': 'u', u'\u1EEA': 'u', u'\u1EEF': 'u', u'\u1EF5': 'y',
    u'\u1EED': 'u', u'\u1ED3': 'o', u'\u00ED': 'i', u'\u1EF4': 'y',
    u'\u00EA': 'e', u'\u00EC': 'i', u'\u1EB7': 'a', u'\u1EB6': 'a',
    u'\u00F3': 'o', u'\u00F2': 'o', u'\u00F5': 'o', u'\u1EB2': 'a',
    u'\u1EB1': 'a', u'\u1EB0': 'a', u'\u00F9': 'u', u'\u1EF2': 'y',
    u'\u1EF1': 'u', u'\u1EF0': 'u', u'\u1EF7': 'y', u'\u1EF6': 'y',
    u'\u1EB9': 'e', u'\u1EB8': 'e', u'\u01B0': 'u', u'\u00DD': 'y',
    u'\u1ECB': 'i', u'\u0128': 'i', u'\u0129': 'i', u'\u1ECC': 'o',
    u'\u1EAB': 'a', u'\u0110': 'd', u'\u00FA': 'u', u'\u1EBF': 'e',
    u'\u1EBE': 'e', u'\u1EBD': 'e', u'\u1EBC': 'e', u'\u1EBB': 'e',
    u'\u1EBA': 'e', u'\u1EE6': 'u', u'\u1EF3': 'y', u'\u1EE7': 'u',
    u'\u1EE2': 'o', u'\u1EE3': 'o', u'\u1EE0': 'o', u'\u1EE1': 'o',
    u'\u00E8': 'e', u'\u00E9': 'e', u'\u1EE4': 'u', u'\u1EE5': 'u',
    u'\u1ECE': 'o', u'\u1EE8': 'u', u'\u1EE9': 'u', u'\u00E0': 'a',
    u'\u00E1': 'a', u'\u00E2': 'a', u'\u00E3': 'a', u'\u1EA8': 'a',
    u'\u1EA9': 'a', u'\u1EA6': 'a', u'\u1EA7': 'a', u'\u1EA4': 'a',
    u'\u1EA5': 'a', u'\u1EA2': 'a', u'\u1EA3': 'a', u'\u1EA0': 'a',
    u'\u1EA1': 'a', u'\u01A1': 'o', u'\u1ECA': 'i', u'\u00CD': 'i',
    u'\u01AF': 'u', u'\u1ECD': 'o', u'\u00CC': 'i', u'\u1ECF': 'o',
    u'\u00CA': 'e', u'\u01A0': 'o', u'\u1ED8': 'o', u'\u1ED1': 'o',
    u'\u1ED0': 'o', u'\u00D9': 'u', u'\u1ED2': 'o', u'\u1ED5': 'o',
    u'\u1ED4': 'o', u'\u1ED7': 'o', u'\u1ED6': 'o', u'\u00D3': 'o',
    u'\u00D2': 'o', u'\u00D5': 'o', u'\u00D4': 'o', u'\u0168': 'u',
    u'\u0169': 'u', u'\u1EEE': 'u', u'\u1ED9': 'o', u'\u0102': 'a',
    u'\u0103': 'a', u'\u1EDA': 'o', u'\u1EDC': 'o', u'\u1EB4': 'a',
    u'\u1EDE': 'o', u'\u1EDD': 'o', u'\u1EDB': 'o', u'\u1EDF': 'o',
    u'\u00C1': 'a', u'\u1EB3': 'a', u'\u00DA': 'u', u'\u00FD': 'y',
    u'\u00F4': 'o', u'\u00C2': 'a', u'\u1EC5': 'e', u'\u1EC8': 'i',
    u'\u1EC9': 'i', u'\u1EB5': 'a', u'\u1EF8': 'y', u'\u00C0': 'a',
    u'\u00C8': 'e', u'\u00C9': 'e', u'\u1EC0': 'e', u'\u1EC1': 'e',
    u'\u1EC2': 'e', u'\u1EC3': 'e', u'\u1EC4': 'e', u'\u00C3': 'a',
    u'\u1EC6': 'e', u'\u1EC7': 'e'}

"""
Code creat "REPLACES_DICT_STR" and "REPLACES_DICT_UNICODE"
File "unicode.csv" created from http://vietunicode.sourceforge.net/charset/
"""

"""
FILE_NAME = 'unicode.csv'


# string like "'LATIN SMALL LETTER Y WITH TILDE'" to "Y"
def get_char(str_need_get_char):
    if str_need_get_char.find('SMALL'):
        return str_need_get_char[str_need_get_char.find('WITH') - 2].lower()
    else:
        return str_need_get_char[str_need_get_char.find('WITH') - 2]


def get_str_dict():
    with open(FILE_NAME, 'r') as f:
        unicode_dict = {}
        for line in f:
            a = line.split(',')
            unicode_dict.update({a[0]: get_char(a[2])})
    return unicode_dict

# print get_str_dict()


# Get unicode
def get_unicode_code_dict():
    with open(FILE_NAME, 'r') as f:
        unicode_code_dict = {}
        for line in f:
            a = line.split(',')
            unicode_code = r"\u" + a[1][2:]
            unicode_code_dict.update({unicode(unicode_code): get_char(a[2])})
    return unicode_code_dict
print get_unicode_code_dict()


def get_unicode_dict():
    with open(FILE_NAME, 'r') as f:
        unicode_dict = {}
        for line in f:
            a = line.split(',')
            unicode_dict.update({a[0]: get_char(a[2])})
    return unicode_dict

# print get_unicode_dict()
"""


def vnese_rm_tones(str_need_convert):
    if isinstance(str_need_convert, str):
        r = re.compile("|".join(REPLACES_DICT_STR.keys()))
        return r.sub(lambda m: REPLACES_DICT_STR[m.group(0)], str_need_convert)
    if isinstance(str_need_convert, unicode):
        r = re.compile("|".join(REPLACES_DICT_UNICODE.keys()))
        return r.sub(
            lambda m: REPLACES_DICT_UNICODE[m.group(0)], str_need_convert)


"""
import unicodedata
def convert_str(str_need_convert):
    return unicodedata.normalize('NFKD', str_need_convert).encode('ascii')
"""
