from hangman_pic import HANGMAN_PICS as HP
from module import get_random_word, display_board, get_guess, play_again


words = {'color': 'red orange yellow green blue indigo violet white black brown'.split(), 'shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(), 'animal':'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()}


print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMH':
    print('Enter difficulty level: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()

if difficulty == 'M':
    del HP[8]
    del HP[7]
if difficulty == 'H':
    del HP[8]
    del HP[7]
    del HP[5]
    del HP[3]

missed_letters = ''
correct_letters = ''
secret_word, secret_set = get_random_word(words)
game_is_done = False

while True:
    print('The secret word is in the set of: ' + secret_set)
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters += guess

        found_all_letter = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letter = False
                break
        
        if found_all_letter:
            print('Yes!, The secret word is "' + secret_word + '"! You have won!')
            game_is_done = True
    
    else:
        missed_letters += guess

        if len(missed_letters) == len(HP) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '"')
            game_is_done = True

    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word, secret_set = get_random_word(words)
        else:
            break