#! python3
# Adds bullet points to the start of each line that has been copied to the
# clipboard.

""" Instructions for use:
    1. Open command prompt
    2. Enter @py.exe C:/[path where you saved this file]\password_locker.py [account name]
"""

import pyperclip
text = pyperclip.paste()

# Separates the lines and add asterisk
lines = text.split('\n')
for i in range(len(lines)): # Loops through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i] # Adds a star to each string in 'lines' list
text = '\n'.join(lines)
pyperclip.copy(text)
