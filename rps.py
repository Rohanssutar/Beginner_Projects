from random import choice

def rock_paper_scissors():
    win = 0
    loss = 0
    count = 0 
    tries = int(input("How many rounds do you want to play? "))

    while count < tries:
        user = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        if user not in ['rock','paper','scissors']:
            continue

        options = ['rock','paper','scissors']
        computer = choice(options)
        print(f"Computer chose: {computer}")

        if user == 'rock' and computer == 'scissors':
            print('You win!🎉')
            win += 1
            count += 1
        elif user == 'scissors' and computer == 'paper':
            print('You win!🎉')
            win += 1
            count += 1
        elif user == 'paper' and computer == 'rock':
            print("You win!🎉")
            win += 1
            count += 1
        elif user == computer:
            print("It's a tie!👀")
            count += 1
        else:
            print("You lost!🥲")
            loss += 1
            count += 1
        
    print(f"\nYou won: {win} times\nYou lost: {loss} times")

rock_paper_scissors()
