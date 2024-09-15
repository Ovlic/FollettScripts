
from veracross_data import Veracross_Data
from patron import Patron

import json
# CONFIG SETTINGS:
patrons_file = "the_patrons.csv" # The input file to get the user data from
parent_file = "parent_info.json" # The input file to get the parent data from
output_file = "output.csv" # The output file to write the data to




patrons: list[Patron] = [] # Create a list of patrons
first_line = "" # Create a variable for the first line of the CSV

with open(patrons_file, 'r') as f: # Open CSV 
    for line in f: # For each line in CSV
        if line.startswith('"Almaden Country Day School Lib"'):
            first_line = line # Save the first line
            continue # Skip the first line
        linesplt = line.split(",") # Split the line by commas
        if linesplt[len(linesplt) - 1].endswith("N"): # If the last element ends with N
            linesplt.append("") # Add an empty string to the end

        for i in range(len(linesplt)): # Loop through each element
            if linesplt[i] == "": # If the element is empty
                if i != 5 and i != 6 and i != 7: # If the element is not the grade, homeroom, or graduation year
                    linesplt[i] = '""' # Replace the element with an empty string
        line = ",".join(linesplt).strip() # Join the line back together
        line += ",\"\"" # Add an empty string to the end
        patrons.append(Patron(line)) # Add the patron to the list

child_info: list[Veracross_Data] = [] # Create a list of child info

with open(parent_file, 'r') as f: # Open parent json
    parent_data = json.loads(f.read()) # Load the parent data
    for item in parent_data:
        child_info.append(Veracross_Data(item))

    
for patron in patrons:
    first_name = patron.first_name
    last_name = patron.last_name
    # if the grade is 6th and above, only add the kids email, otherwise add two parent emails
    if patron.grade == "Alumni": continue
    if patron.patron_type == "Faculty": continue
    if patron.grade == "5" or patron.grade == "6" or patron.grade == "7" or patron.grade == "8": # add 5th since they will shift up to 6th
        if patron.graduation_year != -1: # If the grad year is set
            patron.address_1_email = f"{patron.first_name}{patron.last_name}{patron.graduation_year}@acdsstudent.org" # Set the email
            print(f"{first_name} {last_name} ({patron.graduation_year}): Student email added")
    else:
        # if the grade is 5th and below, add two parent emails
        for child in child_info:
            if child.first_name == first_name and child.last_name == last_name:
                patron.address_1_email = child.parent_1_email
                patron.address_2_email = child.parent_2_email
                print(f"{first_name} {last_name} ({patron.graduation_year}): Parent emails added")
                break
        

with open(output_file, 'w') as f: # Open the output file
    f.write(first_line) # Write the first line
    for patron in patrons: # For each patron
        # print(str(patron))
        f.write(str(patron) + "\n") # Write the patron to the file

