import math
from datetime import datetime
"""
This program computes the volume of a tyre in litres
by requesting for 3 tyre parameters from the user namely:
width, aspect ratio and diameter.
"""

def compute_vol(w, a, d):
    v = (math.pi * (w** 2) * a*((w*a) + 2540*d)) / 10000000000
    return v

#main function
#create variables for tyre parameters and request user input
width = int(input("Enter the width of the tyre in mm: "))
aspect_ratio = int(input("Enter the aspect ratio of the tyre: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

#Getting current date from OS
Current_date = datetime.now()

#call compute_vol function and store result in another variable
volume = compute_vol(width, aspect_ratio, diameter)
#print result
print(f'The approximate volume is {volume: .2f} litres')

#exceeding the requirements 1
#printing price for user
if(width == 155 and aspect_ratio == 65 and diameter == 13):
    print(f"The price of this tyre is $53.99")
elif(width == 165 and aspect_ratio == 60 and diameter == 14):
    print(f"The price of this tyre is $53.99")
elif(width == 175 and aspect_ratio == 65 and diameter == 15):
    print(f"The price of this tyre is $60.99")
elif(width == 185 and aspect_ratio == 55 and diameter == 16):
    print(f"The price of this tyre is $98.99")

#exceeding the requirements 2
#asking if user would like to purchase
ask = input("Would you like to purchase? (Y/N)")
if(ask == "yes" or ask == "y" or ask == "Y" or ask == "Yes" or ask == "YES"):
    number = input("please enter your phone number: ")
    #appending parameters, computed volume and phone number to volumes.txt file
    with open ("volumes.txt", "at") as volumes_file:
        print(f"{Current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter: .0f}, {volume: .2f}, {number}", file=volumes_file)
    print("Thank you for choosing our service!")
else:
    #appending parameters and computed volume to volumes.txt file 
    with open ("volumes.txt", "at") as volumes_file:
        print(f"{Current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter: .0f}, {volume: .2f}", file=volumes_file)
    print("Thank you for choosing our service!")

"""
End of program
"""