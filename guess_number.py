number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? (Enter 'q' to quit) ")

if guess == 'q':
    print(f"The number was {number}.")
elif int(guess) == number:
    print("Congratulations! You guessed the right number.")
else:
    while int(guess) != number:
        print("Sorry! That's not the number I'm thinking of. Try again.")
        guess = input("What number am I thinking of? (Enter 'q' to quit) ")
        if guess == 'q':
            print(f"The number was {number}.")
            break
    else:
        print("Congratulations! You guessed the right number.")