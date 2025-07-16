
# First of all we should write a code to ask the customer's purchase:

dvd_purchase = int(input("How many dvd did you purchase in this month? "))

# Then we can write if codition and statements
if dvd_purchase == 0:
    print(f"You did not earn any points as a reward!")
elif dvd_purchase == 1:
    print(f"Conguratulations! You have earn 2 points as a reward!")
elif dvd_purchase == 2:
    print(f"Conguratulations! You have earn 5 points as a reward!")
elif dvd_purchase == 3:
    print(f"Conguratulations! You have earn 10 points as a reward!")
else:
    print(f"Conguratulations! You have earn 25 points as a reward!")







