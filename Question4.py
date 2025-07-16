
# First of all we should define a function which accepts two numbers as follows:

def evaluate_max(num1, num2):
    if num1 > num2:
        print(f"{num1}")
    elif num1 < num2:
        print(f"{num2}")
    else: 
        print("{num1} and {num2} are equal")

# Now we can ask two number 

first_number = float(input("Enter the first number:"))
second_number = float(input("Enter the second number:"))

# Then call the function 

evaluate_max(first_number, second_number)