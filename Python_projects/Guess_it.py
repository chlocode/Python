import random
"""This program does sth. not sure of it yet hehe
"""
def main():
    pimil_beonho = random.randrange(1, 10)
    guess = 0

    while guess != pimil_beonho:
        guess = float(input("Guess a number between 1 and 10: "))
        if(guess < pimil_beonho and guess > 0):
            print("Kuku dig ground eneter as you wanna show us how low you can go")
        elif (guess > pimil_beonho and guess < 10):
            print("Relax, if you aimed as high with your dreams, you wouldn't be playing game and failing like this. Try again")
        elif (guess > 10 or guess < 0):
            print(f"*bombastic side eye*")
    print("Congrats. Now go do sth right with your life.")

if __name__ == "__main__":
    main()