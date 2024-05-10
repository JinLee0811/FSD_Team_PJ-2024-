import re

def validate_email(email):
    # Email regex should ensure that the dot ( . ), the (@ ) and the ( university.com ) are present
    # ex) -> jin.lee@university.com
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@university\.com$")
    return pattern.match(email) is not None


def validate_password(password):
    # Password regex should ensure that entered passwords are:
    # Start with upper case
    # Minimum 6 letters
    # Following by minimum 3-digits
    # ex) -> Abcdef123

    pattern = re.compile(r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$")
    return pattern.match(password) is not None
