class Method:
    #class Variable
    school='LearnSchool'
    
    #constructor
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    #instance method using self as instance variable
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod  #class method
    def getSchool(cls):
        return cls.school

    @staticmethod #static method
    def info():
        print("Information about school")
        
s1=Method(34,56,78)
s2=Method(78,91,77)

print(s1.avg()) #Call instance method
print(s2.avg())
print(Method.getSchool()) # Call class Method
print(Method.info()) # Call static method