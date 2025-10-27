#DZ 8.2. Paliander

def is_palindrome(text):
    lower_text = text.lower()
    filtered = ""
    for ch in lower_text:
        if ch.isalnum():
            filtered += ch
    if filtered == filtered[::-1]:
        return True
    else:
        return False

print(is_palindrome('A man, a plan, a canal: Panama'))