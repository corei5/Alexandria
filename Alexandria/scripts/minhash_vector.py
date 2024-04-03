from datasketch import MinHash
import numpy as np

def create_minhash_vector(text, num_perm=16):
    """
    Erstellt einen MinHash-Vektor für einen gegebenen String.

    :param text: Der Text, für den der MinHash-Vektor erstellt werden soll.
    :param num_perm: Anzahl der Permutationen für MinHash, bestimmt die Größe des Vektors.
    :return: Ein Tuple, das den MinHash-Vektor als NumPy-Array und als String repräsentiert.
    """
    # Initialisiere MinHash
    m = MinHash(num_perm=num_perm)

    # Teile den Text in Wörter und füge sie zum MinHash hinzu
    for word in text.split():
        m.update(word.encode('utf8'))

    # Konvertiere MinHash zu einem NumPy-Array
    minhash_vector = np.array(m.hashvalues)


    return minhash_vector
