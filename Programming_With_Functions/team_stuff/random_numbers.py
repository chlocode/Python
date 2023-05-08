import random
"""This program creates a list of numbers, appends more numbers to it
and prints the list.
"""
def main():
    #create the list
    numbers = [16.2, 75.1, 52.3]
    #print list 
    print(numbers)
    #call append_random_numbers function with one argument
    append_random_numbers(numbers)
    #print modified list
    print(numbers)
    #call append_random_numbers function with two arguments
    append_random_numbers(numbers, 3)
    #print modified list
    print (numbers)

def append_random_numbers(list, quantity=1):
    """Generates random floating point numbers and appends them to the
    end of a list.
    Parameter(s): numbers_list, quantity
    Returns: nothing
    """
    #Use loop to generate and append quantity amount of numbers
    for i in range(quantity):
        number = random.uniform(1, 4)
        list.append(round(number, 1))

#call main function
main()