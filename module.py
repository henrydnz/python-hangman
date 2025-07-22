from os import name, system

# clears terminal
def clear() -> None:
    if name == 'nt':
        system('cls') # windows
    else:
        system('clear') # other

# returns bolded string
def boldStr(string: str | list) -> str: 
    return f'\033[1m{string}\033[0m'