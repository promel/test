from datetime import datetime
class Person:
    def __init__(self,name,date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        dob = self.date_of_birth.split('-')
        year = int(dob[2])
        month = int(dob[1]) 
        day = int(dob[0]) 
        self.days = (datetime.today() - datetime(year,month, day)).days
        self.age = round(self.days//365.25)