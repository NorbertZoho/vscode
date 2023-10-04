#importing OS module to clear the "screen"
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

print("Welcome to the Rollercoaster!")

#Asking the height
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay 500 ISK")
    elif age <= 18:
        print("Please pay 700 ISK")
    else:
        print("Please pay 1000 ISK")  
else:
    print("Sorry, you have to grow taller before you can ride")              