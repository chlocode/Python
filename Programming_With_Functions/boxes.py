import math
"""
This program computes the number of boxes needed to 
pack x number of items by requesting for the number of items
and the items per box from the user.
It calls a function (compute_per_box) to the main and prints directly
without storing the result of the called function in a variable.
"""

#computing function
def compute_per_box(x, y):
    items_per_box = math.ceil(x/y)
    return items_per_box

#user input
items = int(input("Enter the number of items: "))
per_box = int(input("Enter the number of itms per box:"))

#print computed function result
print(f"For {items} items, packing {per_box} items in each box, you will need {compute_per_box(items, per_box)} boxes.")