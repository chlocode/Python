#Import date and class from the datetime module
from datetime import datetime
#store user input in a variable
subtotal=float(input("Please enter the subtotal:"))

#Compute the total for the discounted subtotal and the regular subtotal
totalDue=subtotal+(0.06*subtotal)
discountTotal=subtotal-(0.1*subtotal)
#call the now() method to get current date and time as a datetime object from the computer's OS
current_date_and_time=datetime.now()
day_of_the_week=current_date_and_time.weekday()
#day_of_the_week= 2

#if else statements to apply the computations made in lines 7-8
#it was frustrating getting this line to work.  i joined the date numbers using the or but the solution was to separate them in different statements
if subtotal>=50 and day_of_the_week==2 or day_of_the_week== 1: 
    newsub=discountTotal+(0.06*discountTotal)
    print(f"sales tax amount: {0.06* subtotal}  day_of_the_week")
    print(f"total: {newsub}")
else:
    print(f"Sales tax amount: {0.06* subtotal:.2f}")
    print(f"Total: {totalDue:.2f}")
