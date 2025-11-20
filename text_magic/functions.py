import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from string import punctuation

PUNCTUATIONS = punctuation+"“”"

def clean_to_lower(text:str) -> str:
    return text.lower()


def clean_punctuation(text:str) -> str:
    output_string = ""
    for character in text:
        if character not in PUNCTUATIONS:
            output_string += character
    return output_string


def clean_strip(text:str) -> str:
    for _ in range(10):
        text = text.replace("  ", " ")
    return text.strip()


def clean_stopwords(text: str, language:str = "english"):
    """Removes stopwords from a text
    
    :param text: Input text to be cleaned
    :type text: str
    :param language: The stopword language to be used
    :type language: str
    :return: Cleaned text
    :rtype: str
    """
    words = text.split(" ")
    clean_text = []
    for word in words:
        if word not in stopwords.words(language):
            clean_text.append(word)
    return " ".join(clean_text)


def pipeline(text:str, **kwargs) -> str:
    text = clean_to_lower(text)
    text = clean_punctuation(text)
    text = clean_strip(text)
    text = clean_stopwords(text, **kwargs)
    return text