from turtle import Turtle
import random
FONT_20 = ('Courier', 20, 'normal')
FONT_15 = ('Courier', 15, 'normal')

with open('words.txt') as words:
    WORD = words.read().split('\n')
WORDS = list(WORD)


# Create a HangManWords Class and inherit the Turtle Class.
class HangManWords(Turtle):
    def __init__(self):
        super().__init__()
        self.hangman_word = random.choice(WORDS)
        self.word_hint = ' '.join(len(self.hangman_word) * '_')
        self.not_in = 'is not in word :('
        self.lost_a_live = 'You loss a life, guess again!'
        self.hideturtle()
        self.penup()
        self.goto(330, 230)
        self.write(f'Word: {self.word_hint}', move=False, align='right', font=FONT_15)
        self.word_hint = list(len(self.hangman_word) * '_')

# Check the guess letter if it in the generated word
    def check_word(self, guess):
        for letter in range(len(self.hangman_word)):
            if guess == self.hangman_word[letter]:
                self.word_hint[letter] = guess
                self.clear()
                self.goto(80, 100)
                self.write(f'Nice guess mate! :D', move=False, align='right', font=FONT_20)
                self.update_board()
        if ''.join(self.word_hint) == self.hangman_word:
            return True

# Generate a new word when the user gets the letters correctly
    def generate_new_word(self):
        self.clear()
        self.hangman_word = random.choice(WORDS)
        self.word_hint = ' '.join(len(self.hangman_word) * '_')
        self.word_hint = list(len(self.hangman_word) * '_')
        self.update_board()

# Update the word text
    def update_board(self):
        self.word_hint = list(self.word_hint)
        self.goto(330, 230)
        self.write('Word: ' + ' '.join(self.word_hint), move=False, align='right', font=FONT_15)

# Display an error message when the user guess is incorrect
    def error_message(self, guess):
        if guess not in self.hangman_word:
            self.clear()
            self.goto(100, 120)
            self.write(f'letter "{guess.upper()}" ' + self.not_in, move=False, align='right', font=FONT_20)
            self.goto(100, 100)
            self.write(self.lost_a_live, move=False, align='right', font=FONT_20)
            self.update_board()
            return True

# Display the word when the user life gets to Zero
    def display_word(self):
        self.clear()
        self.goto(330, 230)
        self.write(f'Word: {self.hangman_word}', move=False, align='right', font=FONT_15)
