
import re
from patron import Patron

# CONFIG SETTINGS:
input_file = "input.csv" # The input file to get the data from
output_file = "output.csv" # The output file to write the data to
school_year = 2024 # The current or next school year (end year)


patrons: list[Patron] = [] # Create a list of patrons
first_line = "" # Create a variable for the first line of the CSV

with open(input_file, 'r') as f: # Open CSV 
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


for patron in patrons:
    if patron.homeroom == "PreK": patron.homeroom = "Pre-K" # Fix Pre-K
    if patron.patron_type == "Faculty": continue # Skip faculty
    
    if patron.graduation_year == -1: # If the graduation year is -1 (not set)
        if patron.address_1_email: # If the email is set
            try: # Try to get the grad year from the email
                # If the email contains the grad year, set the grad year
                patron.graduation_year = [int(s) for s in re.findall(r'\d+', patron.address_1_email)][0]
            except IndexError: # If the email does not contain the grad year
                pass # Do nothing
    
    if not patron.address_1_email: # If the email is not set
        if patron.graduation_year != -1: # If the grad year is set
            patron.address_1_email = f"{patron.first_name}{patron.last_name}{patron.graduation_year}@acdsstudent.org" # Set the email
        elif patron.patron_type == "Faculty": # If the patron is faculty
            patron.address_1_email = f"{patron.first_name[:1].lower()}{patron.last_name.lower()}@almadencountryday.org" # Set the email

    if isinstance(patron.graduation_year, int) and patron.graduation_year != -1: # If the grad year is set 
        eq = patron.graduation_year - school_year # Get the difference between the grad year and 2024
        #if not patron.grade:
        if patron.graduation_year != -1: # If the grad year is set
            if eq < 0: # If the difference is less than 0
                patron.grade = "Alumni" # Set the grade to alumni
                patron.patron_status = "Inactive" # Set the patron status to inactive
            else:
                patron.grade = 8 - eq # Set the grade to 8 - the difference


        if patron.graduation_year != -1 and patron.grade != -1 and patron.patron_type == "Student": # If the grad year, grade, and patron type are set
            if eq < 0: # If they are alumni or faculty
                patron.homeroom = "" # Set the homeroom to empty

with open(output_file, 'w') as f: # Open the output file
    f.write(first_line) # Write the first line
    for patron in patrons: # For each patron
        print(str(patron))
        f.write(str(patron) + "\n") # Write the patron to the file
