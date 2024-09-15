
class Veracross_Patron:
    def __init__(self, record):
        
        self.record = []
        if '"' in record:
            if record[0] == '"' or record.count('"') == 2: 
                temp = record.split('"')
                firstonelst = temp[1].split(",")
                temp[1] = f"{firstonelst[1]} {firstonelst[0]}"
                
            else:
                # if l.count('"') == 2:
                temp = record.split('"')
                firstonelst = temp[1].split(",")
                temp[1] = f"{firstonelst[1]} {firstonelst[0]}"
                
                otheronelst = temp[3].split(",")
                temp[3] = f"{otheronelst[1]} {otheronelst[0]}"

            finallst = []
            for i in range(len(temp)):
                if temp[i].startswith(" "): temp[i] = temp[i][1:]
                if temp[i] != "" and temp[i] != " ": finallst.append(temp[i])
            record = ''.join(finallst)
            if record[0] == " ": record = record[1:]
        
        self.record = record.split(",")

        for i in range(len(self.record)):
            if self.record[i].isnumeric():
                self.record[i] = int(self.record[i])
            
            if isinstance(self.record[i], str):
                if self.record[i] == '""':
                    self.record[i] = ""
                else:
                    self.record[i] = self.record[i].strip('"')
            if isinstance(self.record[i], str):
                if "<None>" in self.record[i]:
                    self.record[i] = None#""
                elif "None" in self.record[i]:
                    self.record[i] = None#""
        
        if "Grade" in self.record[4]: self.record[4] = self.record[4].split(" ")[1]

        print(self.record)
        self.homeroom_teacher = self.record[0]
        self.graduation_year = self.record[1]
        self.last_name = self.record[2]
        self.first_name = self.record[3]
        self.grade = self.record[4]
        self.homeroom = self.record[5]
        self.advisor = self.record[6]
        self.enrollment_status = self.record[7]
        self.role = self.record[8]