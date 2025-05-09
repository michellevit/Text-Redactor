"""
HOW TO RUN:
cd redactor
python redactor.py
"""

import re

# Dictionary of word replacements (case-insensitive)
WORDS_TO_REDACT = {
    'secret': 's',
}

# Normalize keys to lowercase for case-insensitive matching
REPLACEMENTS = {k.lower(): v for k, v in WORDS_TO_REDACT.items()}

def replace_words(text, replacements):
    def replacer(match):
        word = match.group()
        replacement = replacements[word.lower()]
        # Preserve original capitalization (e.g., 'Hi' -> 'Hello')
        if word.isupper():
            return replacement.upper()
        elif word[0].isupper():
            return replacement.capitalize()
        else:
            return replacement

    # Build regex pattern for all words to replace, case-insensitive
    pattern = re.compile('(' + '|'.join(re.escape(word) for word in replacements) + ')', re.IGNORECASE)
    return pattern.sub(replacer, text)

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        original_text = f.read()

    updated_text = replace_words(original_text, REPLACEMENTS)

    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(updated_text)

    print("Replacement complete. See 'output.txt'.")

if __name__ == '__main__':
    main()