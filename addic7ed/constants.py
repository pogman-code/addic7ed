ADDIC7ED_URL = "http://www.addic7ed.com"
# LANG = 52  # Albanian
# LANG = 38  # Arabic
# LANG = 50  # Armenian
# LANG = 48  # Azerbaijani
# LANG = 47  # Bengali
# LANG = 44  # Bosnian
# LANG = 35  # Bulgarian
# LANG = 12  # Català
# LANG = 41  # Chinese (Simplified)
# LANG = 24  # Chinese (Traditional)
# LANG = 31  # Croatian
# LANG = 14  # Czech
# LANG = 30  # Danish
# LANG = 17  # Dutch
LANG = 1   # English
# LANG = 54  # Estonian
# LANG = 13  # Euskera
# LANG = 28  # Finnish
# LANG = 8   # French
# LANG = 53  # French (Canadian)
# LANG = 15  # Galego
# LANG = 11  # German
# LANG = 27  # Greek
# LANG = 23  # Hebrew
# LANG = 55  # Hindi
# LANG = 20  # Hungarian
# LANG = 56  # Icelandic
# LANG = 37  # Indonesian
# LANG = 7   # Italian
# LANG = 32  # Japanese
# LANG = 42  # Korean
# LANG = 57  # Latvian
# LANG = 58  # Lithuanian
# LANG = 49  # Macedonian
# LANG = 40  # Malay
# LANG = 29  # Norwegian
# LANG = 43  # Persian
# LANG = 21  # Polish
# LANG = 9   # Portuguese
# LANG = 10  # Portuguese (Brazilian)
# LANG = 26  # Romanian
# LANG = 19  # Russian
# LANG = 39  # Serbian (Cyrillic)
# LANG = 36  # Serbian (Latin)
# LANG = 60  # Sinhala
# LANG = 25  # Slovak
# LANG = 22  # Slovenian
# LANG = 4   # Spanish
# LANG = 6   # Spanish (Latin America)
# LANG = 5   # Spanish (Spain)
# LANG = 18  # Swedish
# LANG = 59  # Tamil
# LANG = 46  # Thai
# LANG = 16  # Turkish
# LANG = 51  # Ukrainian
# LANG = 45  # Vietnamese

from os.path import expanduser
from configparser import ConfigParser

config = ConfigParser()
config.read(expanduser("~") + "/.addic7edrc")
if "addic7ed" in config and "lang" in config["addic7ed"]:
    LANG = config["addic7ed"]["lang"]
