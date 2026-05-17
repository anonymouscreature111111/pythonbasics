class student: 
    grade = 10
    name = "Penguin"

    def introduction(self):
        print('hi i am a student')

    def details(self):
        print('My name is', self.name)
        print("I study in Grade", self.grade)
    
ob = student()
ob.introduction()
ob.details()