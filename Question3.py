
# First ask the user's actual property 

actual_value = float(input("What is the actual value of your property? "))

# According the explanation in question:

assessment_value = actual_value * 0.6  
tax = assessment_value * (0.72/100)

# So we can print the results:

print(f"The assesment value is: {assessment_value}")
print(f"The tax is: {tax}")