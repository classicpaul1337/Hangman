from turtle import Turtle


# Create a wood Class and inherit the Turtle Class.
class Wood(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.branch_sizes = 'square'

# Display the first wood when the user missed a guess
    def first_branch(self):
        first_branch = Turtle()
        first_branch.shape(self.branch_sizes)
        first_branch.shapesize(stretch_wid=20, stretch_len=0.1)
        first_branch.color('black')
        first_branch.penup()
        first_branch.goto(350, 0)

# Display the second wood when the user missed a guess
    def second_branch(self):
        second_branch = Turtle()
        second_branch.shape(self.branch_sizes)
        second_branch.shapesize(stretch_wid=0.1, stretch_len=5)
        second_branch.color('black')
        second_branch.penup()
        second_branch.goto(300, 200)

# Display the third wood when the user missed a guess
    def third_branch(self):
        third_branch = Turtle()
        third_branch.shape(self.branch_sizes)
        third_branch.shapesize(stretch_wid=4, stretch_len=0.1)
        third_branch.color('black')
        third_branch.penup()
        third_branch.goto(250, 160)
