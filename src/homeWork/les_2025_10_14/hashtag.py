#DZ 5.3. hashtag
import string

user_text = input("Enter the string: ")

clean_input_text = ''.join(ch for ch  in user_text if ch not in string.punctuation)
clean_words = clean_input_text.split()

if not clean_words:
    print("Unable to create hashtag")
else:

    capitalized_word = [word.capitalize() for word in clean_words]

    add_heshtag = "#" + "".join(capitalized_word)

    if len(add_heshtag) > 140:
        add_heshtag = add_heshtag[:140]
    print(add_heshtag)