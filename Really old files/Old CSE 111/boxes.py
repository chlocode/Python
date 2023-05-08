import math

Mi=int(input("Number of manufactured items:"))
IpB=int(input("Number of items per box:"))

Number_of_boxes=Mi/(IpB)
Total=math.ceil(Number_of_boxes)
print(Total)