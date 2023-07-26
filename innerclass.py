class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop() #Creating object inside the class
        
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
        
    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8
            
        def show(self):
            print(self.brand,self.cpu,self.ram)
            
s1=Student('Lokita',1)
s1.show()
print(s1.lap.brand)#One way of accessing data
#Create object outside the class
#l1=Student.Laptop()

            