"""
    BMI Calculator: The calculation is (height in m) squared, divided by weight.
"""

print("Please enter your height in cm")
user_height = float(input())
user_height_in_m = user_height / 100
user_height_squared = user_height_in_m * user_height_in_m

print("Please enter your weight in kg")
user_weight = float(input())

bmi = (user_weight / user_height_squared)
formatted_bmi = "{:.2f}".format(bmi)
print(f"Your BMI is {formatted_bmi}")

if float(formatted_bmi) <= 18.5:
    print("You are underweight")
elif float(formatted_bmi) > 18.5 and float(formatted_bmi) <= 24.9:
    print("You are healthy")
elif float(formatted_bmi) >= 25 and float(formatted_bmi) <= 29.9:
    print("You are overweight")
else:
    print("You are obese")
