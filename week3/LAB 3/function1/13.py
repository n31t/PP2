import random


def game():
    guess = 0
    num = 0
    name = input("Hello! What is your name? \n")
    gnum = random.randint(1, 20)
    print("Well, {fn}, I am thinking of a number between 1 and 20.".format(
        fn=name))
    while num != gnum:
        num = int(input("Take a guess. \n"))
        if num < gnum:
            guess += 1
            print("Your guess is too low.")
        elif num > gnum:
            guess += 1
            print("Your guess is too big.")
        else:
            guess += 1
            print("Good job, {fn}! You guessed my number in {fguess} guesses!".format(
                fn=name, fguess=guess))
            break


game()
