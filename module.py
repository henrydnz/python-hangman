import random as rd
from os import name, system
from strings import boldStr, separator, wlist, strings_dictionary as strings

# clears terminal
def clear() -> None:
    if name == 'nt':
        system('cls') # windows
    else:
        system('clear') # other

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