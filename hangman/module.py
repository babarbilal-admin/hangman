import random
from hangman_pic import HANGMAN_PICS as HP 

def get_random_word(word_dict):
    word_key = random.choice(list(word_dict.keys()))
    word_index = random.randint(0, len(word_dict[word_key]) - 1)
    return [word_dict[word_key][word_index], word_key]

def display_board(missed_letters, correct_letters, secret_word):
    print(HP[len(missed_letters)])
    print()

    print('Missed Letters.', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    
    for letter in blanks:
        print(letter, end=' ')
    print()

def get_guess(already_guess):
    while True:
        print('Guess a letter.')
        guess = input().lower().strip()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guess:
            print('You have already guessed the letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def play_again():
    print('Do you want to play again? (yes/no)')
    return input().lower().strip().startswith('y')