try:
    a = int(input("Enter a number: "))
    print(10 / a)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Enter a valid number!")