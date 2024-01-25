from regex_tasks.task2 import validate_date


def test_date():
    date_to_validate1 = '10/10/2023'
    date_to_validate2 = '10.10.2001'
    date_to_validate3 = '11/24/2024'
    date_to_validate4 = '12/21/2011'
    date_to_validate5 = '08.10.2023'
    date_to_validate6 = '07/24/2023'

    assert validate_date(date_to_validate1) == '10/10/2023 is validate'
    assert validate_date(date_to_validate2) == '10.10.2001 is not validate'
    assert validate_date(date_to_validate3) == '11/24/2024 is validate'
    assert validate_date(date_to_validate4) == '12/21/2011 is validate'
    assert validate_date(date_to_validate5) == '08.10.2023 is not validate'
    assert validate_date(date_to_validate6) == '07/24/2023 is validate'
