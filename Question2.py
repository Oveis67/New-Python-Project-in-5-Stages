
# First we should import "math" module
import math as mt

# Then we can ask the weight and height of the user 

weight = float(input("Enter your weight in KG? "))
height = float(input("Enter your height in meter? "))

bmi = weight / mt.pow(height,2)

# Then we can use if conditions and statements for Body Mass Index (BMI)

if bmi < 18.5:
    print("You are Underweight")
elif 18.5 <= bmi <= 29.99:
    print("You are Normal weight")
else: 
    print("You are Obese!")
