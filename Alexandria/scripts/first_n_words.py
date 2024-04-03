def get_first_n_words(text,n=1000):
    """
    Extracts the first 1000 words from a given text.

    Parameters:
    - text (str): The text from which to extract the words.

    Returns:
    - str: A string containing the first 1000 words of the input text or the entire text if it contains fewer than 1000 words.
    """
    # Splitting the text into a list of words using whitespace as the delimiter.
    words = text.split()

    # Extracting the first 1000 words.
    first_1000_words = words[:1000]

    # Joining the extracted words back into a string with spaces.
    result_text = ' '.join(first_1000_words)

    return result_text