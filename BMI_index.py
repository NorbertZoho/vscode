height = input("Enter your height in meter: ")
weight = input("Enter your weight in kg: ")

height = float(height)
weight = float(weight)

BMI = weight / (height**2)

print("BMI: " + " " + str(round(BMI, 2)))