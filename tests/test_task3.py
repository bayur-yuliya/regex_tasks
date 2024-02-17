from regex_tasks.task3 import email_divide


def test_email():
    email1 = "test1@gmail.com"
    email2 = "example@gmail.com"
    email3 = "test2@gmail.com"

    assert email_divide(email1) == ['test1', 'gmail.com']
    assert email_divide(email2) == ['example', 'gmail.com']
    assert email_divide(email3) == ['test2', 'gmail.com']
