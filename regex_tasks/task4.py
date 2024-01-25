import re


def validate_phone_number(phone_number):
    number_pattern = re.compile(r'380\d{3}\d{2}\d{2}\d{2}')
    if bool(number_pattern.match(phone_number)):
        return f'{phone_number} is validate'
    else:
        return f'{phone_number} is not validate'
