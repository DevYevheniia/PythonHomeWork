#DZ 7.3. Substring search

def second_index(text, some_str):
    sub = text.find(some_str)
    if sub != -1:
        filter_text = text.find(some_str, sub + 1)
        if filter_text != -1:
            return filter_text
    return None

print(second_index("Hello, hello", "lo"))