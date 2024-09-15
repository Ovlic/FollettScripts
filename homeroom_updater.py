
from patron import Patron # Import the Patron class
from veracross_patron import Veracross_Patron # Import the Veracross_Patron class

# CONFIG SETTINGS:
input_file = "input.csv" # The input file to get the data from
veracross_input = "prek_fifth.csv" # The input file to get the data from Veracross
output_file = "output.csv" # The output file to write the data to
output_incorrect = False # Whether or not to output the incorrect patrons to a file


homerooms = {
    "Baum": "Pre-K - Baum",
    "Lasher": "Pre-K - Lasher",
    "Maultsby": "Grade 1 - Maultsby",
    "McGrady": "Grade 1 - McGrady",
    "Brown": "Grade 2 - Brown",
    "Davis": "Grade 2 - Davis",
    "Choudhary": "Grade 3 - Choudhary",
    "Rando": "Grade 3 - Rando",
    "Abraham": "Grade 4 - Abraham",
    "Turnbull": "Grade 4 - Turnbull",
    "Elkins": "Grade 5 - Elkins",
    "None": "Grade 5 - New Teacher", # To be updated in follett once the teacher is known
    "Linquist": "Grade 6 - Linquist",
    "Fishback": "Grade 7 - Fishback",
    "Hanley": "Grade 7 - Hanley",
    "Larson": "Grade 8 - Larson"
}

patrons: list[Patron] = [] # Create a list of patrons
veracross_patrons: list[Veracross_Patron] = [] # Create a list of patrons from Veracross
incorrect_patrons = [] # Create a list of patrons that caused an error

first_line = "" # Create a variable for the first line of the CSV

with open(input_file, 'r') as f: # Open CSV #newinput2.csv
    for line in f: # For each line in CSV
        if line.startswith('"Almaden Country Day School Lib"'): 
            first_line = line # Save the first line
            continue # Skip the first line
        linesplt = line.split(",") # Split the line by commas
        if linesplt[len(linesplt) - 1].endswith("N"): # If the last element ends with N
            linesplt.append("") # Add an empty string to the end
            print(len(linesplt))
        for i in range(len(linesplt)): # Loop through each element
            if linesplt[i] == "": # If the element is empty
                if i != 5 and i != 6 and i != 7: # If the element is not the grade, homeroom, or graduation year
                    linesplt[i] = '""' # Replace the element with an empty string
        line = ",".join(linesplt).strip() # Join the line back together
        line += ",\"\"" # Add an empty string to the end
        patrons.append(Patron(line)) # Add the patron to the list

with open(veracross_input, 'r') as f: # Open CSV
    for line in f: # For each line in CSV
        if line.startswith("Homeroom Teacher"): continue # Skip the first line
        line = line.strip() # Strip the line of whitespace
        veracross_patrons.append(Veracross_Patron(line)) # Turn the patron into Veracross_Patron and add it to the list


for patron in patrons: # For each patron
    try: # Try to fix the email
        fixemaillst = patron.address_1_email.split("@") # Split the email by @
        if fixemaillst[1] == "acsstudent.org": # If the email address is old
            patron.email = fixemaillst[0] + "@ACDSstudent.org" # Fix the email
    except Exception as e: # If there is an error
        incorrect_patrons.append(patron) # Add the patron to the list of incorrect patrons
        print("error")

    for veracross_patron in veracross_patrons: # For each patron in Veracross
        # If the patron's first and last name match the current patron in Veracross
        if patron.first_name == veracross_patron.first_name and patron.last_name == veracross_patron.last_name:
            # If the patron has a homeroom teacher (except fifth grade)
            if veracross_patron.homeroom_teacher != None or veracross_patron.grade == "5":
                success = False
                for teacher, raw_str in homerooms.items(): # For each homeroom teacher
                    if veracross_patron.homeroom_teacher == None: # If the patron is in fifth grade
                        patron.homeroom = "Grade 5 - New Teacher" # Set the homeroom
                        success = True
                        break # Break the loop
                    elif teacher in veracross_patron.homeroom_teacher: # If the teacher is in the homeroom dictionary
                        patron.homeroom = raw_str # Set the homeroom
                        success = True
                        break # Break the loop
                if not success: # If the homeroom teacher is not in the dictionary
                    incorrect_patrons.append(patron) # Add the patron to the list of incorrect patrons

            
            if veracross_patron.advisor: # If the patron has an advisor set
                patron.location_1 = veracross_patron.advisor # Set the advisor
            
            if patron.grade != "Alumni": # If the patron is not an alumni
                patron.grade = veracross_patron.grade # Set the grade
            patron.graduation_year = veracross_patron.graduation_year # Set the graduation year
            break # Break the loop

with open(output_file, 'w') as f: # Open CSV
    f.write(first_line) # Write the first line
    for patron in patrons: # For each patron
        print(str(patron))
        f.write(str(patron) + "\n") # Write the patron to the CSV

if output_incorrect: # If the user wants to output the incorrect patrons
    with open('incorrect.csv', 'w') as f: # Open CSV
        for patron in incorrect_patrons: # For each incorrect patron
            print(str(patron))
            f.write(str(patron) + "\n") # Write the patron to the CSV