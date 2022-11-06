from turtle import Turtle
LIVES = 9
FONT = ('Courier', 15, 'normal')


# Create a HangMan Class and inherit the Turtle Class
class HangMan(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.part_color = 'black'
        self.lives = LIVES
        self.goto(370, 360)
        self.write(f'Lives: {self.lives}', move=False, align='right', font=FONT)

# Display the hangman head when the user missed a guess
    def create_head(self):
        hangman_head = Turtle()
        hangman_head.shape('circle')
        hangman_head.color(self.part_color)
        hangman_head.shapesize(stretch_len=2, stretch_wid=2)
        hangman_head.penup()
        hangman_head.goto(250, 95)

# Display the hangman body when the user missed a guess
    def create_body(self):
        hangman_body = Turtle()
        hangman_body.shape('square')
        hangman_body.color(self.part_color)
        hangman_body.shapesize(stretch_len=0.1, stretch_wid=5)
        hangman_body.penup()
        hangman_body.goto(250, 20)

# Display the hangman right hand when the user missed a guess
    def create_right_hand(self):
        hangman_right_hand = Turtle()
        hangman_right_hand.shape('square')
        hangman_right_hand.color(self.part_color)
        hangman_right_hand.shapesize(stretch_len=0.1, stretch_wid=3)
        hangman_right_hand.setheading(45)
        hangman_right_hand.penup()
        hangman_right_hand.goto(275, 15)

# Display the hangman left hand when the user missed a guess
    def create_left_hand(self):
        hangman_left_hand = Turtle()
        hangman_left_hand.shape('square')
        hangman_left_hand.color(self.part_color)
        hangman_left_hand.shapesize(stretch_len=0.1, stretch_wid=3)
        hangman_left_hand.setheading(135)
        hangman_left_hand.penup()
        hangman_left_hand.goto(225, 15)

# Display the hangman right leg when the user missed a guess
    def create_right_leg(self):
        hangman_right_leg = Turtle()
        hangman_right_leg.shape('square')
        hangman_right_leg.color(self.part_color)
        hangman_right_leg.shapesize(stretch_len=0.1, stretch_wid=3)
        hangman_right_leg.setheading(45)
        hangman_right_leg.penup()
        hangman_right_leg.goto(275, -53)

# Display the hangman left leg when the user missed a guess
    def create_left_leg(self):
        hangman_left_leg = Turtle()
        hangman_left_leg.shape('square')
        hangman_left_leg.color(self.part_color)
        hangman_left_leg.shapesize(stretch_len=0.1, stretch_wid=3)
        hangman_left_leg.setheading(135)
        hangman_left_leg.penup()
        hangman_left_leg.goto(225, -53)

# Remove a live when the user missed a guess
    def decrease_live(self):
        self.lives -= 1
        self.clear()
        self.goto(370, 360)
        self.write(f'Lives: {self.lives}', move=False, align='right', font=FONT)

    # def reset_lives(self):
    #     self.clear()
    #     self.lives = LIVES
    #     self.goto(370, 360)
    #     self.write(f'Lives: {self.lives}', move=False, align='right', font=FONT)
