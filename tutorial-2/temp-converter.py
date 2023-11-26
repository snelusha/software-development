def ask_choice(prompt: str, expected_choices: list = []):
  choice = input(prompt)
  while (choice not in expected_choices):
    choice = input("Invalid option! Pick an option: ")
  return choice

def format_converted_string(conversion: int, celsius: float, fahrenheit: float):
  """
  conversion: int
    1 - Celsius to Fahrenheit
    2 - Fahrenheit to Celsus
  """
  if (conversion == 1):
    return f"{celsius}°C = {fahrenheit}°F"
  else:
    return f"{fahrenheit}°F = {celsius}°C"

choice = ask_choice("""Temperature Converter
Pick an option
  1 - Celsius to Fahrenheit
  2 - Fahrenheit to Celsius
: """, ["1", "2"])

try:
  choice = int(choice)
except:
  print("Invalid input!")

if (choice == 1):
  celsius = input("Enter temperature in Celsius: ")
  try:
    celsius = float(celsius)
    fahrenheit = (celsius * 1.8) + 32
    print(format_converted_string(choice, celsius, fahrenheit))
  except:
    print(f"You entered '{celsius}' is cannot use as input!")
elif (choice == 2):
  fahrenheit = input("Enter temperature in Fahrenheit: ")
  try:
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * 1.8
    print(format_converted_string(choice, celsius, fahrenheit))
  except:
    print(f"You entered '{fahrenheit}' is cannot use as input!")
else:
  print("Invalid option!")
