import nltk
from nltk.tokenize import sent_tokenize

def text_to_sentences(text, language='english'):
    """
    Diese Funktion nimmt einen langen Text und teilt ihn in einzelne Sätze auf.
    :param text: Der lange Text, der in Sätze aufgeteilt werden soll.
    :param language: Die Sprache des Textes ('english' oder 'german').
    :return: Eine Liste von Sätzen.
    """
    sentences = sent_tokenize(text, language=language)
    return sentences

def sentences_to_large_strings(strings, min_length=400):
    """
    Takes a list of strings and returns a new list where each string is at least min_length characters long.

    :param strings: List of strings.
    :param min_length: The minimum length that each string should have.
    :return: A new list of strings that meet the length condition.
    """
    extended_strings = []
    extended_s = ""
    for s in strings:
        extended_s += s  # Always append the current string to the extended string.
        # Check if the extended string meets the minimum length.
        if len(extended_s) >= min_length:
            # If so, append it to the result list and reset the extended string.
            extended_strings.append(extended_s)
            extended_s = ""
    # After the loop, check if there is a remaining extended string that needs to be added.
    if extended_s:  # This checks if extended_s is not an empty string.
        extended_strings.append(extended_s)

    return extended_strings


