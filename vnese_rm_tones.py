# -*- coding: utf-8 -*-
import re


REPLACES_DICT_STR = {
    '\xe1\xbb\x8b': 'i', '\xc3\x8a': 'E', '\xc3\x89': 'E', '\xc3\x88': 'E',
    '\xe1\xbb\x8f': 'o', '\xe1\xbb\x8e': 'O', '\xc3\x8d': 'I', '\xc3\x8c': 'I',
    '\xc3\x83': 'A', '\xc3\x82': 'A', '\xc3\x81': 'A', '\xc3\x80': 'A',
    '\xe1\xbb\x87': 'e', '\xe1\xbb\x86': 'E', '\xe1\xbb\x85': 'e',
    '\xe1\xbb\x84': 'E', '\xe1\xbb\x9b': 'o', '\xc3\x9a': 'U', '\xc3\x99': 'U',
    '\xe1\xbb\x88': 'I', '\xe1\xbb\x9f': 'o', '\xe1\xbb\x9e': 'O',
    '\xc3\x9d': 'Y', '\xe1\xbb\x9c': 'O', '\xc3\x93': 'O', '\xc3\x92': 'O',
    '\xe1\xbb\x91': 'o', '\xe1\xbb\x90': 'O', '\xe1\xbb\x97': 'o',
    '\xe1\xbb\x96': 'O', '\xc3\x95': 'O', '\xc3\x94': 'O', '\xe1\xbb\xab': 'u',
    '\xc3\xaa': 'e', '\xc3\xa9': 'e', '\xc3\xa8': 'e', '\xe1\xbb\xaf': 'u',
    '\xe1\xbb\x8c': 'O', '\xc3\xad': 'i', '\xc3\xac': 'i', '\xc3\xa3': 'a',
    '\xc3\xa2': 'a', '\xc3\xa1': 'a', '\xc3\xa0': 'a', '\xe1\xbb\xa7': 'u',
    '\xe1\xbb\xa6': 'U', '\xe1\xbb\xa5': 'u', '\xe1\xbb\xa4': 'U', '\xc3\xba':
    'u', '\xc3\xb9': 'u', '\xe1\xbb\xb8': 'Y', '\xc3\xbd': 'y',
    '\xe1\xbb\x82': 'E', '\xc3\xb3': 'o', '\xc3\xb2': 'o', '\xe1\xbb\xb1': 'u',
    '\xe1\xbb\xb0': 'U', '\xe1\xbb\xb7': 'y', '\xe1\xbb\x81': 'e',
    '\xc3\xb5': 'o', '\xc3\xb4': 'o', '\xc6\xb0': 'u', '\xe1\xbb\xa0': 'O',
    '\xe1\xbb\x80': 'E', '\xe1\xbb\x8d': 'o', '\xe1\xbb\xb3': 'y',
    '\xe1\xbb\xb2': 'Y', '\xe1\xbb\xb9': 'y', '\xe1\xba\xa8': 'A',
    '\xe1\xba\xa9': 'a', '\xe1\xba\xaa': 'A', '\xe1\xba\xab': 'a',
    '\xe1\xba\xac': 'A', '\xe1\xba\xad': 'a', '\xe1\xba\xae': 'A',
    '\xe1\xba\xaf': 'a', '\xe1\xba\xa0': 'A', '\xe1\xba\xa1': 'a',
    '\xe1\xba\xa2': 'A', '\xe1\xba\xa3': 'a', '\xe1\xba\xa4': 'A',
    '\xe1\xba\xa5': 'a', '\xe1\xba\xa6': 'A', '\xe1\xba\xa7': 'a',
    '\xe1\xba\xb8': 'E', '\xe1\xba\xb9': 'e', '\xe1\xba\xba': 'E',
    '\xe1\xba\xbb': 'e', '\xe1\xba\xbc': 'E', '\xe1\xba\xbd': 'e',
    '\xe1\xba\xbe': 'E', '\xe1\xba\xbf': 'e', '\xe1\xba\xb0': 'A',
    '\xe1\xba\xb1': 'a', '\xe1\xba\xb2': 'A', '\xe1\xba\xb3': 'a',
    '\xe1\xba\xb4': 'A', '\xe1\xba\xb5': 'a', '\xe1\xba\xb6': 'A',
    '\xe1\xba\xb7': 'a', '\xe1\xbb\x9d': 'o', '\xe1\xbb\x83': 'e',
    '\xe1\xbb\x93': 'o', '\xe1\xbb\xa9': 'u', '\xe1\xbb\x9a': 'O',
    '\xe1\xbb\x92': 'O', '\xc6\xa0': 'O', '\xc5\xa9': 'u', '\xc5\xa8': 'U',
    '\xc6\xa1': 'o', '\xe1\xbb\x99': 'o', '\xe1\xbb\x8a': 'I',
    '\xe1\xbb\x95': 'o', '\xe1\xbb\x94': 'O', '\xe1\xbb\xb6': 'Y',
    '\xe1\xbb\xaa': 'U', '\xc4\x82': 'A', '\xc4\x83': 'a', '\xe1\xbb\x98': 'O',
    '\xe1\xbb\x89': 'i', '\xe1\xbb\xa8': 'U', '\xe1\xbb\xb5': 'y',
    '\xc4\x90': 'D', '\xc4\x91': 'd', '\xe1\xbb\xad': 'u', '\xc4\xa8': 'I',
    '\xc4\xa9': 'i', '\xe1\xbb\xac': 'U', '\xe1\xbb\xae': 'U',
    '\xe1\xbb\xa3': 'o', '\xe1\xbb\xa2': 'O', '\xe1\xbb\xb4': 'Y',
    '\xc6\xaf': 'U', '\xe1\xbb\xa1': 'o'}


REPLACES_DICT_UNICODE = {
    u'\u1ef0': 'U',  u'\u1ef7': 'y',  u'\u0111': 'd',  u'\u0110': 'D',
    u'\u1ef6': 'Y',  u'\u00fa': 'u',  u'\u00fd': 'y',  u'\u00c8': 'E',
    u'\u00c9': 'E',  u'\u1eb8': 'E',  u'\u00c2': 'A',  u'\u00c3': 'A',
    u'\u00c0': 'A',  u'\u00c1': 'A',  u'\u1ed1': 'o',  u'\u1ed0': 'O',
    u'\u1ed3': 'o',  u'\u1ed2': 'O',  u'\u1ed5': 'o',  u'\u1ed4': 'O',
    u'\u1ed7': 'o',  u'\u1ed6': 'O',  u'\u1ed9': 'o',  u'\u1eca': 'I',
    u'\u1ecb': 'i',  u'\u1ecc': 'O',  u'\u1ecd': 'o',  u'\u1ece': 'O',
    u'\u1ecf': 'o',  u'\u1eea': 'U',  u'\u1eef': 'u',  u'\u1ef4': 'Y',
    u'\u0128': 'I',  u'\u0129': 'i',  u'\u00f3': 'o',  u'\u00f2': 'o',
    u'\u00f5': 'o',  u'\u00f4': 'o',  u'\u00f9': 'u',  u'\u00cd': 'I',
    u'\u01af': 'U',  u'\u00cc': 'I',  u'\u00ca': 'E',  u'\u01b0': 'u',
    u'\u1ef1': 'u',  u'\u1ef3': 'y',  u'\u1ef9': 'y',  u'\u1ec8': 'I',
    u'\u1ec9': 'i',  u'\u1edc': 'O',  u'\u1edb': 'o',  u'\u1ede': 'O',
    u'\u1edd': 'o',  u'\u1ef2': 'Y',  u'\u1edf': 'o',  u'\u1ec0': 'E',
    u'\u1ec1': 'e',  u'\u1ec2': 'E',  u'\u1ec3': 'e',  u'\u1ec4': 'E',
    u'\u1ec5': 'e',  u'\u1ec6': 'E',  u'\u1ec7': 'e',  u'\u00e8': 'e',
    u'\u00e9': 'e',  u'\u1ed8': 'O',  u'\u00e0': 'a',  u'\u00e1': 'a',
    u'\u00e2': 'a',  u'\u00e3': 'a',  u'\u00da': 'U',  u'\u01a0': 'O',
    u'\u00dd': 'Y',  u'\u1eb7': 'a',  u'\u1eb6': 'A',  u'\u1eb5': 'a',
    u'\u1eb4': 'A',  u'\u1eb3': 'a',  u'\u1eb2': 'A',  u'\u1eb1': 'a',
    u'\u1eb0': 'A',  u'\u1eaf': 'a',  u'\u01a1': 'o',  u'\u1ead': 'a',
    u'\u1eae': 'A',  u'\u1eab': 'a',  u'\u1eac': 'A',  u'\u1eb9': 'e',
    u'\u1eaa': 'A',  u'\u1eeb': 'u',  u'\u1eec': 'U',  u'\u1eda': 'O',
    u'\u0168': 'U',  u'\u0169': 'u',  u'\u1eed': 'u',  u'\u1eee': 'U',
    u'\u00d9': 'U',  u'\u1ea8': 'A',  u'\u00d3': 'O',  u'\u00d2': 'O',
    u'\u0102': 'A',  u'\u0103': 'a',  u'\u00d5': 'O',  u'\u00d4': 'O',
    u'\u1ef8': 'Y',  u'\u1ef5': 'y',  u'\u00ed': 'i',  u'\u00ea': 'e',
    u'\u00ec': 'i',  u'\u1ee2': 'O',  u'\u1ee3': 'o',  u'\u1ee0': 'O',
    u'\u1ee1': 'o',  u'\u1ee6': 'U',  u'\u1ee7': 'u',  u'\u1ee4': 'U',
    u'\u1ee5': 'u',  u'\u1ee8': 'U',  u'\u1ee9': 'u',  u'\u1ebf': 'e',
    u'\u1ebe': 'E',  u'\u1ebd': 'e',  u'\u1ebc': 'E',  u'\u1ebb': 'e',
    u'\u1eba': 'E',  u'\u1ea9': 'a',  u'\u1ea6': 'A',  u'\u1ea7': 'a',
    u'\u1ea4': 'A',  u'\u1ea5': 'a',  u'\u1ea2': 'A',  u'\u1ea3': 'a',
    u'\u1ea0': 'A',  u'\u1ea1': 'a'}

"""
# Code creat "REPLACES_DICT_STR" and "REPLACES_DICT_UNICODE"
# File "unicode.csv" created from http://vietunicode.sourceforge.net/charset/

FILE_NAME = 'unicode.csv'


# string like "'LATIN SMALL LETTER Y WITH TILDE'" to "Y"
def get_char(str_need_get_char):
    if 'SMALL' in str_need_get_char.split():
        return str_need_get_char[str_need_get_char.find('WITH') - 2].lower()
    else:
        return str_need_get_char[str_need_get_char.find('WITH') - 2].upper()


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
            unicode_code_dict.update(
                {unicode(unicode_code.lower()): get_char(a[2])})
    return unicode_code_dict


# for key, value in get_unicode_code_dict().iteritems():
#     print "u'%s': '%s', " % (key, value),


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
import unittest


# Unittest
VN_CHAR_NO_TONES_STR = (
    "AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaA"
    "aAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOo"
    "OoOoOoUuUuUuUuUuUuUuYyYyYyYy")
VN_CHAR_STR = (
    "ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨ"
    "ẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜ"
    "ờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ")

VN_CHAR_NO_TONES_STR_2 = "Mot cau De Test"
VN_CHAR_STR_2 = "Một câu Để Test"


VN_CHAR_UNICODE = u"ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơ"
VN_CHAR_NO_TONES_UNICODE = u"AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOo"

VN_CHAR_NO_TONES_UNICODE_2 = u"Mot Cau De test"
VN_CHAR_UNICODE_2 = u"Một Câu Để test"


class MyTest(unittest.TestCase):

    def test_vnese_rm_tones_str(self):
        self.assertEqual(VN_CHAR_NO_TONES_STR, vnese_rm_tones(VN_CHAR_STR))
        self.assertEqual(VN_CHAR_NO_TONES_STR_2, vnese_rm_tones(VN_CHAR_STR_2))

    def test_vnese_rm_tones_unicode(self):
        for idx in range(len(VN_CHAR_UNICODE)):
            self.assertEqual(
                vnese_rm_tones(VN_CHAR_UNICODE[idx]),
                VN_CHAR_NO_TONES_UNICODE[idx])

        self.assertEqual(
            VN_CHAR_NO_TONES_UNICODE_2, vnese_rm_tones(VN_CHAR_UNICODE_2))

if __name__ == "__main__":
    unittest.main()
"""
