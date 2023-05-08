#import the necessary modules
import math
from datetime import datetime

#declare the date variable
DT=datetime.now()

#get user input
w= int(input("width of tyre in mm:"))
a= int(input("aspect ratio of tyre:"))
d= int(input("diameter of wheel in inches:"))

#compute the volume of space in tyre
v= (math.pi*math.pow(w,2)* a*(w*a +(2540*d)))/10000000000
print(f"the volume of space in the tyre in litres: {v:.2f}")

#exceeding the requirements
if w==155 and a==65 and d==13:
    buy_tyres=input("Would you want to buy tyres with these dimensions?")
    if buy_tyres=="yes":
        print("Price: $53.99")
        number=input("please input your number:")
        print("An agent will reach out to you shortly.")
    else:
            print("Okay. Thank you")
elif w==165 and a==60 and d==14:
    buy_tyres=input("Would you want to buy tyres with these dimensions?")
    if buy_tyres=="yes":
        print("Price: $53.99")
        number=input("please input your number:")
        print("An agent will reach out to you shortly.")
    else:
        print("Okay. Thank you")
elif w==175 and a==65 and d==15:
    buy_tyres=input("Would you want to buy tyres with these dimensions?")
    if buy_tyres=="yes":
        print("Price: $60.99")
        number=input("please input your number.")
        print("An agent will reach out to you shortly.")
    else:
            print("Okay. Thank you")
elif w==185 and a==55 and d==16:
    buy_tyres=input("Would you want to buy tyres with these dimensions?")
    if buy_tyres=="yes":
        print("Price: $98.99")
        number=input("please input your number:")
        print("An agent will reach out to you shortly.")
    else:
        print("Okay. Thank you")
else:
    buy_tyres=input("Would you want to buy tyres with these dimensions?")
    if buy_tyres=="yes":
        number=input("please input your number:")
        print("An agent will reach out to you shortly.")
    else:
        print("Okay. Thank you")

#append to volumes.txt file
with open("volumes.txt", "at") as volumes_file:
    print(f"{DT:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {number}", file=volumes_file)
