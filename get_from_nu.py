
# Get data from newusers.csv
# colums are: 
# First Name [Required],Last Name [Required],Email Address [Required],Password [Required],Password Hash Function [UPLOAD ONLY],Org Unit Path [Required]

# We only care about the first name, last name, email address, and org unit path

# The org unit path we can split to get the grade level from and use that to determine the graduation year.

# Convert all of this into the patron class like a csv

# Patron csv looks like this:
# "P 27221","9999999","Last Name","First Name","MiddleName",20020202,2001,20000101,"U","Student","Active","userdefined1","userdefined2","userdefined3","userdefined4","Address 1 Line 1","Address 1 Line 2","City 1","State 1","Zip 1","email1","Phone 1-1","Phone 1-2","Address 2 Line 1","Address 2 Line 2","City 2","State 2","Zip 2","email2","Phone 2-1","Phone 2-2","N","Grade Level","Alumni","Nickname","Y","userdefined5"

import csv

current_year = 2025
starting_barcode = 27317

def to_patron_csv(barcode, last_name: str, first_name: str, grad_year:int, grade:str, email:str, middle_name:str=None, nickname:str=None, patron_type:str="Student", gender:str="U", status:str="Active", homeroom:str=None):
    def q(x=""):
        if isinstance(x, int): return x if x != -1 else ""
        return f'"{x}"' if x else '""'

    barcode = f"P {barcode}"
    middle_name = "" if middle_name is None else middle_name
    nickname = "" if nickname is None else nickname
    homeroom = "" if homeroom is None else homeroom
    email = "" if grad_year > 2027 else email
    # Should look similar to this:
    # "P 17822","","Leggett","Maren","",,2025,,"U","Student","Active","","","","","","","","","","MarenLeggett2025@ACDSstudent.org","","","","","","","","","","","N","7","Grade 7","","N",""
    thestr = f"{q(barcode)},{q()},{q(last_name)},{q(first_name)},{q(middle_name)},,{q(grad_year)},,{q('U')},{q(patron_type)},{q(status)},{q()},{q()},{q()},{q()},{q()},{q()},{q()},{q()},{q()},{q(email)},{q()},{q()},{q()},{q()},{q()},{q()},{q()},{q()},{q()},{q()},{q('N')},{q(grade)},{q(homeroom)},{q()},{q('N')},{q()}"
    print(thestr)
    # compare_str = '''"P 17822","","Leggett","Maren","",,2025,,"U","Student","Active","","","","","","","","","","MarenLeggett2025@ACDSstudent.org","","","","","","","","","","","N","7","Grade 7","","N",""'''
    # print(thestr == compare_str)
    # split_str = thestr.split(",")
    # compare_split = compare_str.split(",")
    # for i in range(len(split_str)):
    #     print(f"{split_str[i]} == {compare_split[i]}: {split_str[i] == compare_split[i]}")

    return thestr



class newUser:
    def __init__(self, data):
        self.first_name = data['First Name']
        self.last_name = data['Last Name']
        self.email = data['Email Address']
        self.org_unit_path = data['Org Unit Path']

        # get grad year from email
        self.grad_year = int(self.email.split("@")[0][-4:])
        # print(self.grad_year)

        # get grade from org unit
        # org unit looks something like this: /Students/Elementary/SY 2023-2024 Grade 3
        self.grade = self.org_unit_path.split("Grade ")[1]
        # print(self.grade)
        print(self.org_unit_path)
    


# open newusers.csv
data = []
with open("newusers.csv", encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
        
    # Convert each row into a dictionary 
    # and add it to data
    first = True
    for rows in csvReader:
        if first:
            first = False
            continue
            
        # Assuming a column named 'No' to
        # be the primary key
        # key = rows['Person ID']
        # data[key] = rows
        data.append(rows)

# print(data[0])
tst = newUser(data[0])

userdata = ""

for user in data:
    tst = newUser(user)
    # print(tst.first_name, tst.last_name, tst.email, tst.org_unit_path)
    userdata += to_patron_csv(starting_barcode, tst.last_name, tst.first_name, tst.grad_year, tst.grade, tst.email)
    userdata += "\n"
    starting_barcode += 1

print(userdata)
import pyperclip
pyperclip.copy(userdata)

# "P 17822","","Leggett","Maren","",,2025,,"U","Student","Active","","","","","","","","","","MarenLeggett2025@ACDSstudent.org","","","","","","","","","","","N","7","Grade 7","","N",""

# to_patron_csv(
#     barcode=17822,
#     last_name="Leggett",
#     first_name="Maren",
#     grad_year=2025,
#     grade="7",
#     email="MarenLeggett2025@ACDSstudent.org",
#     homeroom="Grade 7"
# )
