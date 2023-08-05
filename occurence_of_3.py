'''Find the number of times digit 3 occurs in each and every number from 0 to n'''
n=int(input("Enter number till where to check: "))
count=0
for item in range(0,n):
    t=str(item)
    for i in t:
        if i == '3':
            count+=1
        else:
            continue

print(count)
