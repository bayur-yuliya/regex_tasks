import re


def split_sentences(text):
    sentence_pattern = re.compile(r'(?<!\w\.\w.)(?<![А-я][A-z]\.)(?<=\.|\?|\!)\s')
    sentences = sentence_pattern.split(text)
    return sentences
