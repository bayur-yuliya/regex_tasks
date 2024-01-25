from regex_tasks.task1 import find_email


def test_date():
    example_text = """
    Привет, Алексей!
    Надеюсь, этот email дошел до тебя. Если у тебя есть вопросы, не стесняйся написать мне на адрес alice@email.com. Мы можем обсудить все детали.
    В последнее время я активно работаю над новым проектом. Если у тебя есть интересные идеи или предложения, буду рад их услышать. Пиши мне на bob@gmail.com.
    Не забывай проверять почту на своем основном адресе, так как я иногда посылаю важные уведомления. Мой основной email: main.contact@mail.ru.
    Жду твоего ответа!
    С наилучшими пожеланиями,
    Алиса
    """
    example_text1 = """
    Привет! Мой электронный адрес для связи: john.doe@example.com.
    Если у вас есть вопросы, пожалуйста, напишите мне на info@example.org.
    Для более оперативной связи используйте feedback@example.net.
    """

    assert find_email(example_text) == ['alice@email.com', 'bob@gmail.com', 'main.contact@mail.ru']
    assert find_email(example_text1) == ['john.doe@example.com', 'info@example.org', 'feedback@example.net']
