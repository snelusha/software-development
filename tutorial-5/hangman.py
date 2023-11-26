import random

class Hangman:
  secret_word: str | None
  retry_count: int
  guessed_word: list[str]

  def __init__(self, secret_words: list[str]):
    self.secret_word = self.get_secret_word(secret_words)
    self.retry_count = len(self.secret_word)
    self.guessed_word = ["_" for _ in self.secret_word]

    while (self.retry_count > 0 and not self.guessed):
      self.display()

      user_input = self.ask_letter()
      if (len(user_input) > 1):
        continue

      if (user_input not in self.secret_word):
        self.retry_count = self.retry_count - 1
        continue
      
      if (user_input in self.guessed_word):
        continue

      for i, c in enumerate(self.secret_word):
        if (user_input == c):
          self.guessed_word[i] = c
          
    self.display()
        
  @property
  def guessed(self):
    return "_" not in self.guessed_word
  
  def get_secret_word(self, words):
    return random.choice(words)
  
  def print_guessed_word(self):
    print(" ".join(self.guessed_word))

  def ask_letter(self, prompt: str = "Guess a letter: "):
    return input(prompt)
  
  def interpolate(self, start, end, t):
    return start + t * (end - start)
  
  def map(self, input_min: int, input_max: int, output_min: int, output_max: int, value: int):
    return int((value - input_min) * (output_max - output_min) / (input_max - input_min) + output_min)

  
  def clear_display(self):
    import sys
    import os

    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

  def display(self):
    self.clear_display()
    print("Let's play Guess the Word!")
    if (self.retry_count == 0):
      print("You out of guesses! You loose!")
    if (self.retry_count < 4):
      print(f"You have only {self.retry_count} to guess the word!")
    else:
      print(f"You have {self.retry_count} to guess the word!")
    print()

    self.print_guessed_word()

    print()
    if (self.guessed):
      print("You guessed secret word!")
    elif (self.retry_count == 0):
      print("You have killed that poor man!")

secret_words = ["elephant", "paradox", "pineapple", "sunny", "cloud", "water", "house"]

game = Hangman(secret_words)
