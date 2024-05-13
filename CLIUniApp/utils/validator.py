import re


def validate_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com$")
    return pattern.match(email) is not None


def validate_password(password):

    pattern = re.compile(r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$")
    return pattern.match(password) is not None
