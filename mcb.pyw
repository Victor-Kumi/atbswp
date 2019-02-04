#! /home/victor/atbswp/venv/bin/python3.6

#Requirements.txt has pyperclip

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    #a = pyperclip.paste()
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1] not in mcbShelf and sys.argv[1].lower() == 'delete':
        for keyword in list(mcbShelf.keys()):
            del mcbShelf[keyword]
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]


mcbShelf.close()
