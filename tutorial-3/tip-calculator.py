def ask_something(propmt: str, parser: type = str, retry: bool = False, retry_prompt: str | None = None):
  answer = input(propmt)
  try:
    parsed_answer = parser(answer)
    return parsed_answer
  except:
    if (retry):
      if (retry_prompt is not None):
        return ask_something(retry_prompt, parser, retry)
      return ask_something(propmt, parser, retry)
    return None

def calculate_tip(level: int):
  match (satisfaction):
    case 1:
      return cost * 2 / 10
    case 2:
      return cost / 10
    case 3:
      return 0
    case _:
      return None

cost = ask_something("Enter the cost of the meal: ", float, True, "Invalid amount! Please enter valid amount: ")

print("""Satisfaction level

(1) - Totally Satisfied
(2) - Satisfied
(3) - Dissatisfied
""")

satisfaction = ask_something("Enter satiscation level - (1, 2, 3): ", int, True, "Invalid satisfaction level: ")

tip = calculate_tip(satisfaction)

if (tip is None):
  print("Invalid satisfaction level!")
  exit()

print(f"Your tip is Rs. {tip}")
  