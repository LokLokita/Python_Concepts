'''Program to replace all 0's with 1 in a given integer.
Given an integer as an input, all the 0's in the number has to be replaced with 1.'''
n=int(input("Enter number: "))
t=str(n)
m=[]
for item in t:
    if item == '0':
        m.append(1) 
    else:
        h=int(item)
        m.append(h)
        
number=0
for i in m:
    number=number*10+i
print(number)
