#2-Player Guessing Game

import time

player1 = input("Player 1, enter your name: \n")
player2 = input("Player 2, enter your name: \n")
# gets user names

print(player2,"close your eyes!\n")
time.sleep(2)
print(player1 + ", please note that your word may not contain any special characters or be longer than 5 characters.\n")
time.sleep(2)
secret_word = input(player1 + " enter a secret word: \n").lower()
print('\n...\n\n')

sw_character_length = []
sw_character_length.extend(secret_word)
sw_character_length.append('')
x = 0
sw_length_test = 0

while sw_character_length[x] != '':
    sw_length_test += 1
    x += 1

while sw_length_test > 5:
    print(player1 + ", your word is too long.\n")
    secret_word = input(player1 + ", please provide a different word less than 6 characters: \n")
    print('\n...\n\n')
    sw_character_length.clear()
    sw_character_length.extend(secret_word)
    sw_character_length.append('')
    x = 0
    sw_length_test = 0
    while sw_character_length[x] != '':
        sw_length_test += 1
        x += 1
else:
     time.sleep(0.1)



if secret_word != '':
    i=1
    while i <= 30:
        print('...')
        i+=1
# player1 enters secret word

guess = ""
guess_count = 0
guess_limit = int(input("How many guesses should " + player2 + " have? \nNote: minimum amount of guesses is 5\n"))

if guess_limit < 5:
    print("\nERROR: Guess Limit (" + str(guess_limit) + ") was too low; now (5)")
    while guess_limit < 5:
        guess_limit += 1
# making sure player2 has at least 5 guesses

sw_makeup = []
sw_makeup.extend(secret_word)
sw_makeup.append('')
# outputs: ['w', 'h', 'a', 't', '']
# (assuming that the word is 'what')

letter_count = 0
n = 0
while sw_makeup[n] != '':
    letter_count += 1
    n += 1

print("\n\n...\n\n\nHINT: The Secret Word starts with the letter '" + str(sw_makeup[0]) + "' and is a total of " + str(letter_count) + " letters long.\nGood Luck!")
# gives hint to the player

while guess != secret_word:
    if guess_count < guess_limit:
        print('\n...\n')
        guess = input(player2 + " guess the secret word: \n").lower()
        print('\n')
        if guess != secret_word:
            print(player2 + " that is incorrect. Remaining guesses: " + str((guess_limit-1) - guess_count) + ".")
            guess_count += 1
    elif guess == secret_word:
        print(player2 + " has guessed the word. GG.")
        break
    else:
        print("\n\n...\n\n\nGAME OVER:\n" + player2 + " failed to guess the word. " + player1 + " wins. GG")
        break
# guess input, game ends when player guesses the word

if guess == secret_word:
    print("...\n\n\n\nGAME OVER:\n" + player2 + " has guessed the word. GG.")
