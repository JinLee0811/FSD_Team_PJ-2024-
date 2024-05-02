import re

class Utils:
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@university\.com$')
    PASSWORD_REGEX = re.compile(r'^[A-Z][a-zA-Z]{5,}\d{3,}$')

