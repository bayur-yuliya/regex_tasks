import re


def validate_date(date):
    date_pattern = re.compile(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$')
    if bool(date_pattern.match(date)):
        return f'{date} is validate'
    else:
        return f'{date} is not validate'
