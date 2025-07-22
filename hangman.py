import random as rd
from module import *
from strings import separator, wlist, strings_dictionary as strings

# choose game idiom
def set_idiom() -> str:
    while True:
        # show description
        print(strings['en']['set_idiom_description'], end = '')
        # user input
        idiom_choice: str = input()
        clear()

        # handle input error
        if idiom_choice not in ('1', '2'):
            print(strings['en']['invalid_option'], f'{boldStr(f'\'{idiom_choice}\'')}')
            print(separator)
            continue

        idiom = 'en' if idiom_choice == '1' else 'pt'

        print(strings[idiom]['set_idiom'])
        print(separator)

        return idiom

# choose game difficulty
def set_difficulty(idiom: str) -> int:
    while True:
        # show description
        print(strings[idiom]['set_difficulty'], end='')

        # user input
        difficulty: str = input()
        clear()

        # handle input error
        if not difficulty.isalpha() or difficulty.lower() not in ('a', 'b', 'c', 'd'): 
            print(strings[idiom]['invalid_option'], f'{boldStr(f'\'{difficulty}\'')}\n')
            continue

        # options
        print(strings[idiom]['choosen_difficulty'], end='')
        match difficulty:
            case 'a': 
                print(strings[idiom]['easy'])
                return 7
            case 'b':
                print(strings[idiom]['medium'])
                return 5
            case 'c':
                print(strings[idiom]['hard'])
                return 3        
            case 'd':
                print(strings[idiom]['impossible'])
                return 1

# random word choosing
def set_word(idiom) -> str:
    return rd.choice(wlist[idiom == 'en'])

# display words in '_ _ _ a _' format
def display_word(word: str, guessed_letters: list):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# main game
def game(idiom) -> int | None:
    # set round secret word
    word: str = set_word(idiom) 
    # set round tries count
    tries: int = set_difficulty(idiom)
    # all guessed letters. contains space character to be able to be printed in display_word
    guessed_letters: list[str] = [' ']
    # game() output. counter of wrong guesses. 
    wrong_guesses: int = 0

    # main loop
    while tries > 0:
        # ==== current stats description
        print(separator)
        print(display_word(word, guessed_letters))
        print(strings[idiom]['remaining_tries'], f'{tries}\n', end='')

        # ==== letter guess input
        letter = input(strings[idiom]['type_guess']).lower()
        clear()

        # ==== error handling

        # input is too big or is not a letter
        if len(letter) != 1 or not letter.isalpha(): 
            print(strings[idiom]['guess_incorrect'])
            continue

        # gues has been already made
        if letter in guessed_letters:
            print(strings[idiom]['already_guessed'], f'\'{letter}\'!')
            continue
            
        # ==== game logic

        # letter is right
        if letter in word:
            if tries > 1:
                print(strings[idiom]['right_guess1'], f"'{letter.upper()}'", strings[idiom]['right_guess2'])
            guessed_letters.append(letter)
        # letter is wrong
        else:
            if tries > 1:
                print(strings[idiom]['wrong_guess1'], f"'{letter.upper()}'", strings[idiom]['wrong_guess2'])
            guessed_letters.append(letter)
            # counters updating
            wrong_guesses += 1
            tries -=1

        # show winning message
        if set(word).issubset(set(guessed_letters)):
            print(separator)
            print(strings[idiom]['win'])
            print(strings[idiom]['word'], boldStr(word))
            print(strings[idiom]['wrongs'], wrong_guesses)
            
            # return wrong guesses counter
            return wrong_guesses
    
    # show game over (tries are over) message
    else: 
        print(strings[idiom]['tries_over1'], boldStr(word), end='')
        print(strings[idiom]['tries_over2'])
        return None

# list of high scores
best = []
# game initialization and play again
def play(best: list) -> None:
    clear()

    # boolean to game idiom
    idiom: str = set_idiom()

    # initializes the game and append high score
    high_score: int | None = game(idiom)
    if high_score is not None:
        best.append(high_score)

    # display high score after game ends
    print('Record: ' if idiom == 'en' else 'Recorde: ', end='')
    if best:
        print(min(best), 'tries' if idiom == 'en' else 'tentativas')
    else:
        print(strings[idiom]['no_record'], '\n')

    # play again loop
    while True:
        # choose option
        play_again_input: str = input(strings[idiom]['play_again']).lower()
        # handle input error
        if not play_again_input.isalpha() or play_again_input not in ('y', 'n'):
            print(strings[idiom]['invalid_option'], f'(\'{play_again_input}\')')
            continue
            
        # options
        if play_again_input == 'y':
            clear()
            play(best)
        else:
            print(separator, strings[idiom]['thanks'])
            break
            
# execute
play(best)