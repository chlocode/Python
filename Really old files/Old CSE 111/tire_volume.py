#import the necessary modules
import math
from datetime import datetime

#create variables for the parameters
w= int(input("width of tyre in mm:"))
a= int(input("aspect ratio of tyre:"))
d= int(input("diameter of wheel in inches:"))

#compute the volume of space in tyre
v= (math.pi*math.pow(w,2)* a*(w*a +(2540*d)))/10000000000
print(f"the volume of space in the tyre in litres: {v:.2f}")

#ask= input("Would you like to buy tyres with these dimensions?")
#if ask=="yes" or "Yes" or "yeah" or "Yeah":  
   # number=input("Please enter your number:")

#elif ask=="No" or "no" or "nah" or "Nah":
   # print("Okay. Thank you")



#the parameters for the priced tyres
m13w=155
m13a=65
m13d=13
price13="$53.99"

m14w=165
m14a=60
m14d=14
price14="$53.99"

m15w=175
m15a=65
m15d=15
price15="$60.99"

m16w=185
m16a=55
m16d=16
price16="$98.99"

"""
#exceeding the requirements
ask="yes"
if w==m13w and a==m13a and d==m13d:
    print(f"Price of tyre: {price13}" )
    mm=input("would you like to buy?")
    if mm==ask:
        mn=input("your number")
    else:
        print("okay")
elif w==m14w and a==m14a and d==m14d:
    print(f"Price of tyre: {price14}" )
    mm=input("would you like to buy?")
    if mm==ask:
        mn=input("your number")
    else:
        print("okay")
elif  w==m15w and a==m15a and d==m15d:
    print(f"Price of tyre: {price15}" )
    mm=input("would you like to buy?")
    if mm==ask:
        mn=input("your number")
    else:
        print("okay")
elif  w==m16w and a==m16a and d==m16d:
    print(f"Price of tyre: {price16}" )
    mm=input("would you like to buy?")
    if mm==ask:
        mn=input("your number")
    else:
        print("okay")
"""
#appending output to a file
Date_and_time=datetime.now()
#{Date_and_time:%Y-%m-%d}
with open ("volumes.txt", "at") as volumes_file:
    print(f"{Date_and_time:%Y-%m-%d}, {w}, {a}, {d}", file=volumes_file)


"""
a = 1
b = 3
c = -2
result = a + b * 7 % 4 - c
print(f"{result}")
"""
