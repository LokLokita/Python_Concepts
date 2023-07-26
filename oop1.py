class Student:
    def Check_pass(self):
        if self.marks>=40:
            return True
        else:
            return False
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

Student1=Student("Henry",85)
print("Name: "+Student1.name)
print(Student1.marks)
   
class Computer:
    def config(self):
        print("i5,16gb,1tb")   
        
comp1=Computer()
Computer.config(comp1) #This is one method to call method for particular object 
comp1.config() # This is another approach which is commonly used 

'''Student1=Student()
Student2=Student()
Student1.name="om"
Student1.marks=85
did_pass=Student1.Check_pass()
print(did_pass)
Student2.name="Henry"
Student2.marks=30
did_pass=Student2.Check_pass()
print(did_pass)'''
