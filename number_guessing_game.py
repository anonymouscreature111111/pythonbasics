import random

numbers = list(range(1, 10 + 1))  

original = random.choice(numbers)

print("Numbers list:", numbers)

guess = int(input("Guess the number: "))

if guess == original:
    print("Correct! You guessed the right number.")
elif guess > original:
    print("Your guess is higher than the original number.")
else:
    print("Your guess is smaller than the original number.")

print(f"(The original number was: {original})")
