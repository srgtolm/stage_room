__author__ = 'sereg'

import simplegui
import random
import math

secret_range = 100
advice_label = None
num_won = 0
num_lost = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, secret_range, allowed_guesses, guess_history
    global advice_label, advised_number, range_high, range_low

    allowed_guesses = int(math.ceil(math.log(secret_range, 2)))
    secret_number = random.randrange(0, secret_range)
    guess_history = []

    # setting up global variables range_high, range_low
    # changing label in the frame to suggest a proper number
    range_high = secret_range
    range_low = 0
    advised_number = range_high / 2
    if advice_label:
        advice_label.set_text("Suggested guess: " +
                              str(advised_number))

    print("New game. Range is from 0 to " +
          str(secret_range))
    print("Number of remaining guesses is " +
          str(allowed_guesses))
    print("")

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret_range
    secret_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret_range
    secret_range = 1000
    new_game()

def input_guess(guess):
    # main game logic goes here
    global guess_number, allowed_guesses, guess_history
    global num_lost, num_won
    guess_number = int(guess)
    guess_history.append(guess_number)
    print("Guess was " + str(guess_number))
    allowed_guesses = allowed_guesses - 1
    print("Number of remaining guesses is " +
          str(allowed_guesses))
    if guess_number == secret_number:
        num_won += 1
        print("Correct!")
        print("")
        new_game()
    else:
        advice_direction = ""
        if allowed_guesses <= 0:
            num_lost += 1
            print("You ran out of guesses. " +
                  "The number was " +
                  str(secret_number))
            print("")
            new_game()
        elif guess_number < secret_number:
            print("Higher!")
            update_advice("UP")
        else:
            print("Lower!")
            update_advice("DOWN")
    print("")

def update_advice(direction = ""):
    """ optional: updates the label with suggestion about next guess """
    global range_low, range_high, guess_number, advice_label, advised_number
    if advised_number == guess_number:
        if direction == "UP":
            range_low = advised_number
        if direction == "DOWN":
            range_high = advised_number
    else:
        if direction == "UP":
            range_low = max(range_low, guess_number)
        if direction == "DOWN":
            range_high = min(range_high, guess_number)
    advised_number = range_low + ((range_high - range_low) / 2)
    if advice_label:
        advice_label.set_text("Suggested guess: " +
                              str(advised_number))

def draw_handler(canvas):
    """ optional: prints game history with previous guesses for current game """
    global guess_history, num_won, num_lost
    canvas.draw_text("Games won: " + str(num_won) + "/" +
                     str(num_won + num_lost), (15, 15), 15,
                     "Green", "monospace")
    canvas.draw_text("History of guesses:", (15, 30), 15,
                     "Green", "monospace")
    for (i, guess) in enumerate(guess_history):
        canvas.draw_text(str(guess) + " (#" + str(i + 1) + ")",
                         (15, 45 + (i * 15)),
                         15,
                          "Green",
                          "monospace")

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
button100 = frame.add_button("Range: 0 - 100", range100, 200)
button1000 = frame.add_button("Range: 0 - 1000", range1000, 200)
inp = frame.add_input("What is your guess?", input_guess, 200)

# optional :)
advice_label = frame.add_label("")
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()

# call new_game
new_game()

# always remember to check your completed program against the grading rubric
