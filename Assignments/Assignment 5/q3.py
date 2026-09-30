# Question 3: Simple Number Checker Function

def check_number(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Enter a whole number: "))

result = check_number(number)

print(f"{number} is an {result} number.")
