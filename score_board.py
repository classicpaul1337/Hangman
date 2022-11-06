import turtle
from turtle import Turtle
FONT = ('Courier', 15, 'normal')


# Create a score Class and inherit the Turtle Class.
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.question = ''
        with open('score.txt') as score:
            self.high_score = score.read()
        self.penup()
        self.update_board()

# Update the score line and high score.
    def update_board(self):
        self.clear()
        self.goto(60, 360)
        self.write(f'High Score: {self.high_score}', move=False, align='right', font=FONT)
        self.goto(-300, 360)
        self.write(f'Score: {self.score}', move=False, align='right', font=FONT)

# Increase score when guess is correct.
    def increase_score(self):
        self.score += 1
        self.update_board()
        self.check_high_score()

# Check if the current score is higher than the high score then make the current score the new High score.
    def check_high_score(self):
        if self.score > int(self.high_score):
            with open('score.txt', mode='w') as score:
                score.write(str(self.score))
            self.high_score = self.score
            self.update_board()

# Ask the user if he/she wants to play again.
    def game_not_over(self):
        self.question = turtle.textinput(title='Do you wish to play again? Yes or No', prompt='').lower()
        if self.question == 'yes':
            self.score = 0
            self.update_board()
            return True
        else:
            return False

# Print out game over message when the user choose not to play again
    def game_over(self):
        self.goto(-20, -50)
        self.write('GAME OVER', move=False, align='center', font=('Courier', 30, 'normal'))
        self.goto(-20, -80)
        self.write('This screen will close in 5 seconds', move=False, align='center', font=FONT)
