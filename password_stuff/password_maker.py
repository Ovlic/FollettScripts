used_words = [] # Fill this up with used words to avoid duplicates (manual input)
words = [] # Fill this up with words to use (manual input)

USE_THIS = ["among", "horse", "unity", "drove", "exist", "craft", "billy", "teach", "booth", "grace"] # dont remember what this was for

# Websites for generating words:
 # https://randomwordgenerator.com/
 # try this one too: https://perchance.org/fiveletter


import random, pyperclip
# Pyperclip is a python module that allows you to copy and paste text to and from your clipboard

# from pynput.keyboard import Key, Listener

word_index = 0

def make_password():
    global word_index
    # choose the word by getting the word at the index and capitalize the first letter, and add a four digit number (0000-9999)
    in_used_words = True
    while in_used_words:
        # if words[word_index] in used_words:
        if USE_THIS[word_index] in used_words:
            #print(f"word {words[word_index]} is in used words")
            print(f"word {USE_THIS[word_index]} is in used words")
            word_index += 1
        else:
            in_used_words = False
    
    # password = words[word_index].capitalize() + str(random.randint(0, 9999)).zfill(4)
    password = USE_THIS[word_index].capitalize() + str(random.randint(0, 9999)).zfill(4)
    return password

pswrds = ""
for i in range(0,95):
    pw = make_password()
    print(pw)
    pswrds += pw + "\n"
    word_index += 1

pyperclip.copy(pswrds)

