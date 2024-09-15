
# Creating a class that works for a row in a csv table following this format:
# Person ID,Full Name,Parent 1 Email,Parent 2 Email,Current Grade,Advisor,Enrollment Status,Roles

# Split full name into first and last name by comma

#{
    #     "Person ID": "27366",
    #     "Full Name": "Abraham, Quinn",
    #     "Parent 1 Email": "anthonyabraham@mac.com",
    #     "Parent 2 Email": "katnelson2009@gmail.com",
    #     "Current Grade": "Pre-Kindergarten",
    #     "Advisor": "None",
    #     "Enrollment Status": "RE: Pending Re-Enrollment",
    #     "Roles": "Student (PK), rsf, Niece of Faculty"
    # }

def gdrn(value):
    """get_data_replace_none"""
    if isinstance(value, str):
        if value == "None":
            return None
    return value

class Veracross_Data:
    def __init__(self, row):
        self.person_id = gdrn(row["Person ID"])
        self.full_name = gdrn(row["Full Name"])
        self.first_name = self.full_name.split(", ")[1]
        self.last_name = self.full_name.split(", ")[0]
        self.parent_1_email = gdrn(row["Parent 1 Email"])
        self.parent_2_email = gdrn(row["Parent 2 Email"])
        self.current_grade = gdrn(row["Current Grade"])
        self.advisor = gdrn(row["Advisor"])
        self.enrollment_status = gdrn(row["Enrollment Status"])
        self.roles = gdrn(row["Roles"])
