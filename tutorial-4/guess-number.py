from random import randint

from typing import Final

MAX_ATTEMPTS: Final = 5

attempts = 0

def ask_number(prompt: str):
  number = input(prompt)
  try:
    return int(number)
  except:
    return None

def get_random_number(min: int, max: int):
  return randint(min, max)

def is_guessed(hidden: int, guess: int):
  return hidden == guess

hidden_number = get_random_number(0, 20)

print(hidden_number)
while (attempts < MAX_ATTEMPTS):
  guessed_number = ask_number("Guess a number: ")
  attempts = attempts + 1

  if (guessed_number is None):
    continue
  
  if (guessed_number == hidden_number):
    break

  if (guessed_number > hidden_number):
    print("Your guess is too high!")
  else:
    print("Your guess is too low!")

if (attempts < MAX_ATTEMPTS):
  print(f"You got it in {attempts} attempts")
else:
  print(f"Not guessed! hidden number was: {hidden_number}")
