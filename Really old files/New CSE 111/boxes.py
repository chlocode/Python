import math

# variables for user input
items=int(input("please enter the number of items:"))
items_per_box=int(input("please enter the number of items per box:"))

#code to compute the number of boxes required
number_of_boxes= math.ceil(items/items_per_box)

#print out result
print(f"for {items} items, packing {items_per_box} items in each box, you will need {number_of_boxes} boxes.")