
# import the variable scripts from _scripts.py
from _scripts import scripts

# Loop through each row in the filenames string
for filename, script in scripts:

    # Create a new file with the filename and write the script to it
    with open(filename, 'w') as f:
        f.write(script)

# These scripts are used to create the student accounts using a USB Rubber Ducky
# The account create script looks something like this:
"""
DEFAULTDELAY 100
DELAY 500
STRING FirstnameLastnameGradyear@ACDSstudent.org
ENTER
DELAY 3500
STRING password
ENTER
DELAY 5000
STRING password
ENTER
DELAY 1000
STRING password
ENTER
"""
    
# The login script looks something like this:
"""
DEFAULTDELAY 100
DELAY 500
STRING FirstnameLastnameGradyear@ACDSstudent.org
ENTER
DELAY 3500
STRING password
ENTER
DELAY 5000
STRING password
ENTER"""