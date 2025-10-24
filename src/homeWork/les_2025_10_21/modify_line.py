#DZ 7.2. Modify a line

def correct_sentence(text):
    if text:
        text = text[0].upper() + text[1:]
        if not text.endswith('.'):
            text += '.'
        return text

print(correct_sentence("Greetings. Friends"))