import re


def email_divide(email):
    name_pattern = re.compile(r'\b[A-z0-9._%+-]+[^@]')
    domen_name_pattern = re.compile(r'[^@]+[A-z0-9.-]+\.[a-z]{2,}\b')
    return [re.search(name_pattern, email).group(), re.search(domen_name_pattern, email).group()]
