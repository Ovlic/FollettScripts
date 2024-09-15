import csv, json

csv_file = "input.csv"

class Barcode:
    def __init__(self, barcode: int):
        self.barcode = barcode

    def __init__(self, barcode: str):
        barcode_split = barcode.split("P ")
        try:
            if len(barcode_split) == 2 and barcode_split[0]:
                self.barcode = int(barcode_split[1])
            else:
                raise ValueError("Invalid barcode format")
        except:
            raise ValueError("Invalid barcode format")
    
    def __str__(self):
        return f"P {self.barcode}"

## Next patron barcode
#first_barcode = Barcode()

test = "P 27309"

tst = test.split("P ")
print(tst)
print(f"'{tst[0]}'")
if len(tst) == 2 and test[0]:
    print("Yes")
else:
    print("No")


# Convert from csv to json
data = []

# Open a csv reader called DictReader
with open(csv_file, encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
        
    # Convert each row into a dictionary 
    # and add it to data
    for rows in csvReader:
            
        # Assuming a column named 'No' to
        # be the primary key
        # key = rows['Person ID']
        # data[key] = rows
        data.append(rows)

for item in data:
    f_name = item['first_name']
    l_name = item['last_name']
    grade = item['grade']
    grad_year = item['grad_year']
    email = ""
    # check if grade string can be int
    if grade.isdigit():
        grade = int(grade)
        if grade == 6 or grade == 7 or grade == 8:
            email = f"{f_name}{l_name}{grad_year}@acdsstudent.org"
