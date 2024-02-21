class Student:
    def __init__(self, name, lastName, sNumber):
        self.name = name
        self.lastName = lastName
        self.sNumber = sNumber

    def information(self):
       return f"Öğrenci Bilgisi:  {self.name} {self.lastName} {self.sNumber}"
    

    def get_sNumber(self):
       return self.sNumber







