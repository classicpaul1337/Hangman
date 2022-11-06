import turtle
from turtle import Screen
from hangman import HangMan
from wood import Wood
from words import HangManWords
from score_board import Score
import os
import sys
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('green')
screen.title('GUI Hangman Game by Classic')
screen.tracer(0)
wood = Wood()
word = HangManWords()
score = Score()
hangman = HangMan()


game_is_on = True
while game_is_on:
    screen.update()
# Ask the user to input a letter
    guess = turtle.textinput('Guess a letter :D', prompt='').lower()
# Check the guess letter if it is in word
    if word.check_word(guess):
        score.increase_score()
        word.generate_new_word()
# Display error message if the guess is incorrect, so the user lose a live
    elif word.error_message(guess):
        hangman.decrease_live()
        screen.tracer(1)
        if hangman.lives == 8:
            wood.first_branch()
        if hangman.lives == 7:
            wood.second_branch()
        if hangman.lives == 6:
            wood.third_branch()
        if hangman.lives == 5:
            hangman.create_head()
        if hangman.lives == 4:
            hangman.create_body()
        if hangman.lives == 3:
            hangman.create_right_hand()
        if hangman.lives == 2:
            hangman.create_left_hand()
        if hangman.lives == 1:
            hangman.create_right_leg()
        if hangman.lives == 0:
            hangman.create_left_leg()
            word.display_word()
            if score.game_not_over():
                score.check_high_score()
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                score.check_high_score()
                game_is_on = False
                score.game_over()
                time.sleep(5)
                turtle.bye()
        screen.tracer(0)

screen.exitonclick()
