README:

# Redactor

[![Python](https://img.shields.io/badge/Python-3.13.1-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

A simple Python script that scans an input text file for specific words and replaces them with predefined alternatives.

## Getting Started

#### 1. Ensure you have Python downloaded to your system

#### 2. Clone the repo and navigate into the folder

powershell
git clone https://github.com/yourusername/redactor.git
cd redactor

#### 3. Define Your Redaction Rules

- Key: the word you want to redact
- Value: the replacement word that will appear instead
- Example:

python
WORDS_TO_REDACT = {
'secret': 's',
'sEcRET2': 'S2'
}

# 'secret' will be replaced with 's'

# 'SECRET2' or 'secret2' or 'sEcRET2' will be replaced with 'S2'

**NOTE:** This script performs case-insensitive matching - it will find the target word regardless of whether its letters are uppercase, lowercase, or mixed.

#### 4. Prepare your input file

- Rename the file 'input.txt.placeholder' to 'input.txt'

## How to Use

- Ensure the 'WORDS_TO_REDACT' dictionary in redactor.py is up-to-date
- Paste/type the text you'd like to redact into 'input.txt'
- Run the script

powershell
python redactor.py

- The redacted output will be saved to the file output.txt in the same directory
