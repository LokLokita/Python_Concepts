class A:
    def __init__(self):
        print("init A")
        
    def feature1(self):
        print("Feature1-A is working")
    
    def feature2(self):
        print("Feature2 is working")
        
class B:
#class B(A):
    def __init__(self):
        super().__init__() #to access constructor of parent class as well from child class
        print("init B")
        
    def feature1(self):
        print("Feature1-B is working")
    
    def feature4(self):
        print("Feature4 is working")
class C(A,B):
    def __init__(self):
        super().__init__() 
        print("init C")
        
    def feat(self):
        super().feature2() #super method can be used to access other methods of super class as well
            
a1=C()
a1.feature1()
a1.feat()
'''
#class C(A,B):#multiple inheritence if class A And Class B are separate classes(not inheriting each other)
class C(B):
    def feature5(self):
        print("Feature5 is working")
    
    def feature6(self):
        print("Feature6 is working")
        
a1=A() # parent class Super class
a1.feature1()
a1.feature2()
b1=B() #Child Class Sub Class
b1.feature1() # till here it shows Single level Inheritence
c1=C()# till here it shows Mutlilevel level Inheritence
c1.feature4()'''


        