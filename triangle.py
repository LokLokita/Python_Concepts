class triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def primeter(self):
        peri=self.a+self.b+self.c
        return peri
tri1=triangle(10,20,30)
ans=tri1.primeter()
print(ans)
        