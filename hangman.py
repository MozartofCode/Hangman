"""
Hangman Game

@author: Bertan Berker
@Language: Python
"""

import turtle as t
import random

list_of_words = [
    "hello", "name", "sample", "computer", "science",
    "rainbow", "rain", "winter", "happiness", "love",
    "money", "goals", "basketball", "lacrosse", "phone", "art", "winning", "success"
    ]

WORD = random.choice(list_of_words).upper()


def init():
    """
    This function initializes the turtle canvas and also starts the game

    :precondition: Turtle is looking right and pen is down
    :postcondition: Same as precondition

    :return: None
    """

    t.penup()
    t.right(90)
    t.fd(200)
    t.left(90)
    t.back(200)
    t.pendown()

    t.fd(100)
    t.bk(200)
    t.fd(100)
    t.left(90)
    t.fd(400)
    t.right(90)
    t.fd(400)
    t.right(90)
    t.fd(50)
    t.left(90)

    print("Let's play Hangman!!!")


def punishment(mistake):
    """
    This function draws the head, body, legs and the arms according to the number of mistakes

    :precondition: Turtle is looking right and pen is down
    :postcondition: same as precondition

    :param mistake: An integer value that is used for representing the situation of the hangman

    :return: None
    """

    if mistake == 5:
        t.penup()
        t.right(90)
        t.fd(100)
        t.left(90)
        t.pendown()
        t.circle(50)

    elif mistake == 4:
        t.right(90)
        t.fd(150)
        t.left(90)

    elif mistake == 3:
        t.right(45)
        t.fd(75)
        t.back(75)
        t.left(45)

    elif mistake == 2:
        t.right(135)
        t.fd(75)
        t.back(75)
        t.left(135)

    elif mistake == 1:
        t.left(90)
        t.fd(75)
        t.right(45)
        t.fd(75)
        t.back(75)
        t.right(45)

    else:
        t.left(135)
        t.fd(75)
        t.back(75)
        t.right(135)


def is_complete(guess):
    """
    This function determines whether the player (user) found the word or not

    :param guess: user's completed word, guess

    :return: True if the guess is the same as word
    """

    if guess == WORD:
        return True

    return False


def gameplay():
    """
    This is the main gameplay function, in which the necessary functions are called and the game is played

    :return: None
    """

    current_guess = []
    mistake_num = 6

    for _ in WORD:
        current_guess.append("_")

    while mistake_num != 0:

        letter_guess = input("Guess a letter: ")

        if len(letter_guess) != 1:
            print("Guess a Letter Please!!!")

        else:

            if letter_guess.upper() in current_guess:
                print("You already put that letter!")

            elif letter_guess.upper() in WORD:
                print("Yes!!")

                for i in range(0, len(WORD)):
                    if WORD[i] == letter_guess.upper():
                        current_guess[i] = letter_guess.upper()

            else:
                print(letter_guess + " is not in the secret word!")
                mistake_num = mistake_num - 1
                punishment(mistake_num)

            for letter in current_guess:
                print(letter, end=" ")
            print(" ")
            print(" ")

            guess = ""
            guess = guess.join(current_guess)

            if is_complete(guess):
                print("Congrats, You win!!!")
                print("The secret word was " + WORD)

                return

    print("You lost!!!!")
    print("The secret word was: " + WORD)


if __name__ == "__main__":
    init()
    gameplay()
    t.done()
