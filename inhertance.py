class Employee:
    company="amazon"

    def ajay(self):
        print("this is an employee")

class Programmer(Employee):
    language="java"
    company="google"

    def ram(self):
        print("this is a programmer")

    def ajay(self):
        print(f"language is{self.language}")


e=Employee()
e.ajay()
p=Programmer()
p.ram()
p.ajay()