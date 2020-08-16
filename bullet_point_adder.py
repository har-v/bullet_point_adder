#! python3
# Adds bullet points to the start of each line that has been copied to the
# clipboard.

import pyperclip
text = pyperclip.paste()

# Separates the lines and add asterisk
lines = text.split('\n')
for i in range(len(lines)): # Loops through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i] # Adds a star to each string in 'lines' list
text = '\n'.join(lines)
pyperclip.copy(text)
