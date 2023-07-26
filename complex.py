class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
        
    def add(self,number):
        r=self.real+number.real
        i=self.imag+number.imag 
        result=Complex(r,i)
        return result
    
n1=Complex(5,4)
n2=Complex(3,5)
ans=n1.add(n2)
print("real= ",ans.real)
print("imaginary= ",ans.imag)