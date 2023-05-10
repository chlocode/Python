import random
"""This is a guessing game.
The user tries to guess a number between 1 and 10 which the computer has chosen
"""
def main():
    pimil_beonho = random.randrange(1, 10)
    guess = 0

    while guess != pimil_beonho:
        guess = float(input("Guess a number between 1 and 10: "))
        if(guess < pimil_beonho and guess > 0):
            print("You could dig the ground and jump in as you'd love to show us how low you can go. Try again")
        elif (guess > pimil_beonho and guess < 10):
            print("Whoa there buddy, aim high with your dreams, not this game. Try again")
        elif (guess > 10 or guess < 0):
            print(f"*bombastic side eye*")
    print("Congrats. Now, go do something productive.")

if __name__ == "__main__":
    main()
