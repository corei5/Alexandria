
def equalize_list_lengths(list1, list2):
    """
    Truncates the longer of two lists to make their lengths equal.

    Parameters:
    - list1 (List): First list.
    - list2 (List): Second list.

    Returns:
    - Tuple[List, List]: A tuple containing the two lists adjusted to the same length.
    """
    # Determine the minimum length of the two lists
    minimum_length = min(len(list1), len(list2))
    # Truncate both lists to the minimum length
    return list1[:minimum_length], list2[:minimum_length]
