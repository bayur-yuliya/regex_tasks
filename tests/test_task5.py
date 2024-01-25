from regex_tasks.task5 import split_sentences


def test_split_sentences():
    example_text = """You can't parse [X]HTML with regex. Because HTML can't be parsed by regex. Regex is not a tool that can be used to correctly parse HTML. As I have answered in HTML-and-regex questions here so many times before, the use of regex will not allow you to consume HTML. Regular expressions are a tool that is insufficiently sophisticated to understand the constructs employed by HTML."""
    example_text1 = "Это предложение номер один. И вот предложение номер два! А это третье? Вот и все."

    assert split_sentences(example_text) == ["You can't parse [X]HTML with regex.",
                 "Because HTML can't be parsed by regex.",
                 'Regex is not a tool that can be used to correctly parse HTML.',
                 'As I have answered in HTML-and-regex questions here so many times before, the use of regex will not allow you to consume HTML.',
                 'Regular expressions are a tool that is insufficiently sophisticated to understand the constructs employed by HTML.']
    assert split_sentences(example_text1) == ['Это предложение номер один.',
                 'И вот предложение номер два!',
                 'А это третье?',
                 'Вот и все.']
