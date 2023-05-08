"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
#define function that determines maximum heart rate
def rate_arithmetic(age):
    max_rate = 220 - age
    return max_rate

#define function that determines slowest heart rate
def slowest_rate(age):
    slow = (65/100) * rate_arithmetic(age)
    return slow

#define function that determines fastest heart rate
def fastest_rate(age):
    fast = (85/100) * rate_arithmetic(age)
    return fast

age = int(input("Please enter your age: "))
min_rate = slowest_rate(age)
max_rate = fastest_rate(age)
print(f"When you exercise to strengthen your heart, you should keep your heart rate between{min_rate: .0f} and{max_rate: .0f}")