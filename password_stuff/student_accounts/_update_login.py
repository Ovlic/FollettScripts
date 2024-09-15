
# loop through all the files in the folder "login_user_acc" and remove the last three lines and save it.

import os

def update_login():
    for file in os.listdir("login_user_acc"):
        if file.endswith(".txt"):
            with open("login_user_acc/" + file, "r") as f:
                lines = f.readlines()
            with open("login_user_acc/" + file, "w") as f:
                f.writelines([item for item in lines[:-3]])
    print("Files updated successfully in login_user_acc folder")

update_login()