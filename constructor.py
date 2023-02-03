
# __init___ method( constructor)
class Employee:
    company="Amazon"

    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getinfo(self):
        print(f"The name of Programmmer is{self.name} and product is{self.product}")
      
saize=Employee("saize","tft")
saif=Employee("rohit","amazon")
saize.getinfo()
saif.getinfo()