import random

# Randomly selected selected number form 1 to 100
n = random.randrange(1,100)

guess = int(input("Enter a number: "))
while guess != n:
    if guess > n:
        print("Try lower")
        guess = int(input("Enter the number again: "))
    elif guess < n:
        print("Try higer")
        guess = int(input("Enter the number again: "))
    else:
        break
print("That's correct!")