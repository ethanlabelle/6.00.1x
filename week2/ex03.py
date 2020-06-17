print('Please think of a number between 0 and 100!')
min = 0
max = 100
guess = (int)((min + max) /2)
print('Is your secret number {}?'.format(guess))
ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while (ans != 'c'):
    if ans == 'h':
        max = guess
    elif ans == 'l':
        min = guess
    else:
        print('Sorry, I did not understand your input.')
    guess = (int)((min + max) / 2)
    print('Is your secret number {}?'.format(guess))
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print('Game over. Your secret number was: {}'.format(guess))