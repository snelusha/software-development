from random import randint

coin = randint(0, 1)

print("Heads" if bool(coin) else "Tails")
