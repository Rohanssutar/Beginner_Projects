from random import randint

secret = randint(1,10)
maxtries = 3

for attempt in range(1, maxtries + 1):
    try:
        guess = int(input(f"Take a guess {attempt}/{maxtries}: "))
    except ValueError:
        continue

    if guess == secret:
        print(f"Correct!🎉 You guessed in {attempt} tries.")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")
else:
    print(f"You lost 🥲, the secret number is {secret}")
    
