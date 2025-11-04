# DZ 10.2. Find the first word
def first_word(text: str) -> str:
    """
    The function returns the first word in a string.
    Return: str : first word
    """
    i = 0
    while i < len(text) and not text[i].isalpha():
        i += 1

    text = text[i:]

    word = ''
    for ch in text:
        if ch.isalpha() or ch == "'":
            word += ch
        else:
            break
    return word

print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))

