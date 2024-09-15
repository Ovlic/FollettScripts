

class Patron:
    # Add properties from the 35-field format patron record
    def __init__(self, record):
        self.record = record.split(",")
        #print("len(self.record)")
        #print(len(self.record))
        for i in range(len(self.record)):
            if self.record[i] == "":
                self.record[i] = -1
            elif self.record[i].isnumeric():
                self.record[i] = int(self.record[i])
            
            if isinstance(self.record[i], str):
                if self.record[i] == '""':
                    self.record[i] = ""
                else:
                    self.record[i] = self.record[i].strip('"')

        self.barcode = self.record[0]
        self.alternate_id = self.record[1] # District id
        self.last_name = self.record[2]
        self.first_name = self.record[3]
        self.middle_name = self.record[4]
        self.card_expiration_date = self.record[5]
        self.graduation_year = self.record[6]
        self.birth_date = self.record[7]
        self.gender = self.record[8] # U = not specified
        self.patron_type = self.record[9]
        self.patron_status = self.record[10]
        self.location_1 = self.record[11] # User_defined_1
        self.location_2 = self.record[12] # User_defined_2
        self.user_field_1 = self.record[13] # User_defined_3
        self.user_field_2 = self.record[14] # User_defined_4
        self.address_1_line_1 = self.record[15]
        self.address_1_line_2 = self.record[16]
        self.address_1_city = self.record[17]
        self.address_1_state = self.record[18]
        self.address_1_zip = self.record[19]
        self.address_1_email = self.record[20] # email_1
        self.address_1_phone_1 = self.record[21]
        self.address_1_phone_2 = self.record[22]
        self.address_2_line_1 = self.record[23]
        self.address_2_line_2 = self.record[24]
        self.address_2_city = self.record[25]
        self.address_2_state = self.record[26]
        self.address_2_zip = self.record[27]
        self.address_2_email = self.record[28] # email_2
        self.address_2_phone_1 = self.record[29]
        self.address_2_phone_2 = self.record[30]
        self.record_31 = self.record[31]
        # Dunno what 31 is
        self.grade = self.record[32]
        self.homeroom = self.record[33]
        self.nickname = self.record[34] 
        self.acceptable_use_policy = self.record[35] 
        self.user_defined_5 = self.record[36].strip() # User_defined_5

    def __init__(self, last_name, first_name, barcode, grade, graduation_year, username=None, email=None):
        thestr = ""
        thestr += f"{barcode},,{last_name},{first_name},,{graduation_year},,U,"


    def __str__(self):
        thestr = ""
        # print("len(self.__dict__.items())")
        # print(len(self.__dict__.items()))
        for key, value in self.__dict__.items():
            if key == "record":
                continue
            value = "" if value is None else value
            value = f"\"{value}\"" if isinstance(value, str) else value
            if value == -1: value = ""
            thestr += f"{value},"
        return thestr[:-1].strip()

"""    @property
    def barcode(self):
        return self.record[0]

    @property
    def alternate_id(self):
        return self.record[1]

    @property
    def last_name(self):
        return self.record[2]

    @property
    def first_name(self):
        return self.record[3]

    @property
    def middle_name(self):
        return self.record[4]

    @property
    def card_expiration_date(self):
        return self.record[5]

    @property
    def graduation_year(self):
        return self.record[6]

    @property
    def birth_date(self):
        return self.record[7]

    @property
    def gender(self):
        return self.record[8]

    @property
    def patron_type(self):
        return self.record[9]

    @property
    def patron_status(self):
        return self.record[10]

    @property
    def location_1(self):
        return self.record[11]

    @property
    def location_2(self):
        return self.record[12]

    @property
    def user_field_1(self):
        return self.record[13]

    @property
    def user_field_2(self):
        return self.record[14]

    @property
    def address_1_line_1(self):
        return self.record[15]

    @property
    def address_1_line_2(self):
        return self.record[16]

    @property
    def address_1_city(self):
        return self.record[17]

    @property
    def address_1_state(self):
        return self.record[18]

    @property
    def address_1_zip(self):
        return self.record[19]

    @property
    def address_1_email(self):
        return self.record[20]

    @property
    def address_1_phone_1(self):
        return self.record[21]

    @property
    def address_1_phone_2(self):
        return self.record[22]

    @property
    def address_2_line_1(self):
        return self.record[23]

    @property
    def address_2_line_2(self):
        return self.record[24]

    @property
    def address_2_city(self):
        return self.record[25]

    @property
    def address_2_state(self):
        return self.record[26]

    @property
    def address_2_zip(self):
        return self.record[27]

    @property
    def address_2_email(self):
        return self.record[28]

    @property
    def address_2_phone_1(self):
        return self.record[29]

    @property
    def address_2_phone_2(self):
        return self.record[30]"""

    #def __str__(self):
        

