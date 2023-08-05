'''Program to Find the Sum of Digits of a Given Number '''
number=input("Enter number: ")
count=0
for i in number:
    intger=int(i)
    count+=intger
print(count)

'''Program to find the frequency of each element of an array'''
m=[]
p=[]
n=int(input("Enter number of items in list m: "))
for item in range(0,n):
    m.append(int(input("Enter item: ")))

for k in m:
    n=m.count(k)
    if k in p:
        continue
    else:
        print(k,' appears: ',n,' times')
    p.append(k)