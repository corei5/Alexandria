import re
def extract_reconstruction_content(text):
    """
    Extrahiert den Inhalt zwischen <kg> und </kg> in einem gegebenen Text.

    :param text: Der Text, aus dem der Inhalt extrahiert werden soll.
    :return: Der extrahierte Inhalt oder None, falls keine Übereinstimmung gefunden wurde.
    """
    match = re.search(r'<reconstruction>(.*?)</reconstruction>', text, re.DOTALL)
    if match:
        return match.group(1)

    else:
        return None