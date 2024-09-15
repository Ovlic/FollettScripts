
import csv

contents = []
newfile = ""

with open('patrons_7_11_24.csv') as f: # Open CSV
    for line in f: # For each line in CSV
        if line.startswith('"Almaden Country Day School Lib"'):
            newfile += line
            continue # Skip the first line
        # print(line)
        linesplt = line.strip().split(",") # Split the line by commas
        for i in range(len(linesplt)):
            if "@" in linesplt[i].lower():
                if "@acdsstudent.org" in linesplt[i].lower(): # If the element is an email
                    if linesplt[i] == linesplt[-1]: # If the element is the last element 
                        continue # Skip the element
                    linesplt[-1] = f'{linesplt[i]}' # Set the last element to the email
                    break

                elif linesplt[9] == '"Faculty"': 
                    if "@almadencountryday.org" in linesplt[i].lower():
                        if linesplt[i] == linesplt[-1]: # If the element is the last element 
                            continue # Skip the element
                        linesplt[-1] = f'{linesplt[i]}' # Set the last element to the email
                        break

                else:
                    print("Making email...")
                    if linesplt[9] != '"Student"': 
                        print(linesplt[9])
                        print("Not a student, skipping.")
                        continue

                    if linesplt[2] == '""':
                        print("No last name, skipping.")
                        continue
                    if linesplt[3] == '""':
                        print("No first name, skipping.")
                        continue
                    if linesplt[6] == '':
                        print(f"GY: '{linesplt[6]}'")
                        print("No grad year, skipping.")
                        continue
                    # no student email, have to make it
                    email = f'"{linesplt[3][1:-1]}{linesplt[2][1:-1]}{linesplt[6]}@acdsstudent.org"'
                    print(f"Email: {email}")
                    linesplt[-1] = email

                    break
        
        if linesplt[2] == '"Buck"': continue # Skipping me
        if linesplt[9] == '"Faculty"': continue # skipping teachers since they should already have usernames
        new_line = ",".join(linesplt).strip()
        newfile += new_line + "\n"
        
    
# for elem in contents[0]:
#     print(f"'{elem}'")

# print(newfile)
with open('patrons_7_11_24_USERNAMES.csv', 'w') as f:
    f.write(newfile) # Write the new file to the output file\

# Useful site for allowed field names
# https://destinyhelp212en.follettsoftware.com/content/r_PIC_Available_Destiny_fields.htm

# TO IMPORT UPDATES INTO FOLLETT, YOU HAVE TO LOG IN TO A DISTRICT ACCOUNT, THE DESTINYADMIN ACCOUNT WILL NOT WORK
# new acc credentials: 
    # username: districtadmin
    # password: fssdestiny