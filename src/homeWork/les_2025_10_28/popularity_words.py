# DZ 9.1. Determine the popularity of certain words in the text
def popular_words(text: str, words: list[str]) -> dict[str, int]:
    """
    The function counts the number of occurrences of each word from the list in the text.
    return: Dictionary {word: number of occurrences}.
    """
    text = text.lower().split()
    result = {word: text.count(word) for word in words}
    return result


print(popular_words
    (
    '''When I was One I had just begun When I was Two I was nearly new ''',
    ['i', 'was', 'three', 'near']
))
