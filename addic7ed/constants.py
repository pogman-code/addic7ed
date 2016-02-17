from os.path import expanduser
from configparser import ConfigParser

ADDIC7ED_URL = "http://www.addic7ed.com"

# Language code - "ISO 639-1" - except for 3 letters code
LANG_ISO = {
    'all': {'code': 0, 'lang': 'All languages'},
    'ar': {'code': 38, 'lang': 'Arabic' },
    'az': {'code': 48, 'lang': 'Azerbaijani' },
    'bg': {'code': 35, 'lang': 'Bulgarian' },
    'bn': {'code': 47, 'lang': 'Bengali' },
    'bs': {'code': 44, 'lang': 'Bosnian' },
    'ca': {'code': 12, 'lang': 'Català' },
    'cs': {'code': 14, 'lang': 'Czech' },
    'da': {'code': 30, 'lang': 'Danish' },
    'de': {'code': 11, 'lang': 'German' },
    'el': {'code': 27, 'lang': 'Greek' },
    'en': {'code': 1, 'lang': 'English' },
    'es': {'code': 4, 'lang': 'Spanish' },
    'es-la': {'code': 6, 'lang': 'Spanish (Latin America)' },
    'es-es': {'code': 5, 'lang': 'Spanish (Spain)' },
    'et': {'code': 54, 'lang': 'Estonian' },
    'eu': {'code': 13, 'lang': 'Euskera' },
    'fa': {'code': 43, 'lang': 'Persian' },
    'fi': {'code': 28, 'lang': 'Finnish' },
    'fr': {'code': 8, 'lang': 'French' },
    'fr-ca': {'code': 53, 'lang': 'French (Canadian)' },
    'gl': {'code': 15, 'lang': 'Galego' },
    'he': {'code': 23, 'lang': 'Hebrew' },
    'hi': {'code': 55, 'lang': 'Hindi' },
    'hr': {'code': 31, 'lang': 'Croatian' },
    'hu': {'code': 20, 'lang': 'Hungarian' },
    'hy': {'code': 50, 'lang': 'Armenian' },
    'id': {'code': 37, 'lang': 'Indonesian' },
    'is': {'code': 56, 'lang': 'Icelandic' },
    'it': {'code': 7, 'lang': 'Italian' },
    'ja': {'code': 32, 'lang': 'Japanese' },
    'ko': {'code': 42, 'lang': 'Korean' },
    'lt': {'code': 58, 'lang': 'Lithuanian' },
    'lv': {'code': 57, 'lang': 'Latvian' },
    'mk': {'code': 49, 'lang': 'Macedonian' },
    'ms': {'code': 40, 'lang': 'Malay' },
    'nl': {'code': 17, 'lang': 'Dutch' },
    'no': {'code': 29, 'lang': 'Norwegian' },
    'pl': {'code': 21, 'lang': 'Polish' },
    'pt': {'code': 9, 'lang': 'Portuguese' },
    'pt-br': {'code': 10, 'lang': 'Portuguese (Brazilian)' },
    'ro': {'code': 26, 'lang': 'Romanian' },
    'ru': {'code': 19, 'lang': 'Russian' },
    'si': {'code': 60, 'lang': 'Sinhalese' },
    'sk': {'code': 25, 'lang': 'Slovak' },
    'sl': {'code': 22, 'lang': 'Slovene' },
    'sq': {'code': 52, 'lang': 'Albanian' },
    'sr': {'code': 39, 'lang': 'Serbian (Cyrillic)' },
    'sr-la': {'code': 39, 'lang': 'Serbian (Latin)' },
    'sv': {'code': 18, 'lang': 'Swedish' },
    'ta': {'code': 59, 'lang': 'Tamil' },
    'th': {'code': 46, 'lang': 'Thai' },
    'tr': {'code': 16, 'lang': 'Turkish' },
    'uk': {'code': 51, 'lang': 'Ukrainian' },
    'vi': {'code': 45, 'lang': 'Viêt Namese' },
    'zh-hans': {'code': 41, 'lang': 'Chinese (Simplified)' },
    'zh-hant': {'code': 24, 'lang': 'Chinese (Traditional)' }
}

LANG_DEFAULT = 'en'

CONFIG_FILE_NAME = ".addic7edrc"

