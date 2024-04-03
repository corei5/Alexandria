import random
def split_string_into_chunks(long_string, min_words=1000, max_words=1500):
    """
    Splits a long string into chunks with random lengths between min_words and max_words,
    with no overlap between chunks.

    :param long_string: The long string to split.
    :param min_words: Minimum number of words in a chunk.
    :param max_words: Maximum number of words in a chunk.
    :return: A list of string chunks.
    """
    words = long_string.split()
    chunks = []
    current_chunk = []
    meta = []
    chunknr = 0
    chunk_size = random.randint(min_words, max_words)

    for i, word in enumerate(words):
        current_chunk.append(word)

        # Check if the current chunk reaches the desired size
        if len(current_chunk) >= chunk_size:
            chunks.append(' '.join(current_chunk))
            meta.append([chunknr])
            chunknr += 1

            # Set up the next chunk
            current_chunk = []
            chunk_size = random.randint(min_words, max_words)

    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(' '.join(current_chunk))
        meta.append([chunknr])

    return chunks, meta
