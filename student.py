class Student:
    school = "AkiraChix"
    def __init__(self,first_name,last_name,age,origin_country) :
        self.first_name = first_name
        self.last_name = last_name
        self.origin_country = origin_country
        self.age = age
    def full_name(self):
       return f"Hello {self.first_name} {self.last_name}" 
   
    def year_of_birth(self):
        return 2022-self.age
        
    def initials(self):
        return f"My initial are {self.first_name[0]} {self.last_name[0]}"
        
        