from regex_tasks.task4 import validate_phone_number


def test_validate_phone_number():
    phone_number1 = '380507653546'
    phone_number2 = '380950876536'
    phone_number3 = "380676089479"
    phone_number4 = "380676089"
    phone_number5 = "35276089479"

    assert validate_phone_number(phone_number1) == '380507653546 is validate'
    assert validate_phone_number(phone_number2) == '380950876536 is validate'
    assert validate_phone_number(phone_number3) == "380676089479 is validate"
    assert validate_phone_number(phone_number4) == "380676089 is not validate"
    assert validate_phone_number(phone_number5  ) == "35276089479 is not validate"
