from datasketch import MinHash
import numpy as np

def create_minhash_vector(text, num_perm=16):
    """
    Creates a MinHash vector for a given string.

     :param text: The text for which the MinHash vector should be created.
     :param num_perm: Number of permutations for MinHash, determines the size of the vector.
     :return: A tuple representing the MinHash vector as a NumPy array and as a string.
    """
    # Initialisiere MinHash
    m = MinHash(num_perm=num_perm)

    # Teile den Text in Wörter und füge sie zum MinHash hinzu
    for word in text.split():
        m.update(word.encode('utf8'))

    # Konvertiere MinHash zu einem NumPy-Array
    minhash_vector = np.array(m.hashvalues)


    return minhash_vector
