n = int(input("Enter digit: "))
rnumber = ''
while (n != 0):
    a = n % 10
    rnumber += str(a)
    n = n//10
print(int(rnumber))
