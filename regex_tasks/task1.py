import re


def find_email(text):
    email_pattern = re.compile(r'\b[A-z0-9._%+-]+@[A-z0-9.-]+\.[a-z]{2,}\b')
    return re.findall(email_pattern, text)
