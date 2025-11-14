# DZ 12.1. Clean text from html tags
import re

def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> str:
    """
    Cleans the text of an HTML file from tags and empty lines.

    html_file: path to the HTML file to clean
    result_file: path to the file where the cleaned text will be written cleaned.txt

    Return: the cleaned text as a str.
    """
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    cleaned_content = re.sub(r'<.*?>', '', html, flags=re.DOTALL)

    cleaned_lines = [line.strip() for line in cleaned_content.splitlines() if line.strip()]
    cleaned_text = '\n'.join(cleaned_lines)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    return cleaned_text

if __name__ == "__main__":
    delete_html_tags('draft.html', 'cleaned.txt')
