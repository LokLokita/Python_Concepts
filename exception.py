a=5
b=2

try:
    print("Resource Open")
    print(a/b)
    k=int(input("Enter a number: "))
except ZeroDivisionError as e:
    print("You can divide number by zero",e)
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print(e)
finally:
    print("Resource Closed")#Will be executed even if code runs or if it does not run
print("Bye")