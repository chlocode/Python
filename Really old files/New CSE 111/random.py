import random
def main():
    numbers= [ 16.2, 75.1, 52.3 ]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    
    
    append_random_numbers(numbers, 3)
    print(numbers)

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        rn= random.uniform(0,100)
        rounding=round(rn, 1)
        numbers_list.append(rounding)


if __name__ == "__main__":
    main()