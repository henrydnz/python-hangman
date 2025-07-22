# returns bolded string
def boldStr(string: str | list) -> str: 
    return f'\033[1m{string}\033[0m'

separator: str = '~~~~~~~~~~~~~~~~\n'

wlist: list[list[str]] = [ 
    [
        'abacate', 'abajur', 'abelha', 'alface', 'berinjela', 
        'bicicleta', 'bola', 'bolo', 'borboleta', 'cachorro', 
        'cadeira', 'cama', 'caneca', 'capivara', 'computador', 
        'copo', 'coxinha', 'dado', 'dente', 'desafio', 
        'dicionario', 'dinossauro', 'elefante', 'escola', 'escova', 
        'escova de dente', 'espelho', 'faca', 'foca', 'foguete', 
        'fruta', 'futebol', 'gato', 'gaveta', 'girafa', 
        'girassol', 'guitarra', 'hamburguer', 'harpa', 'helice', 
        'hipopotamo', 'iate', 'igreja', 'ilha', 'internet', 
        'isca', 'jacare', 'janela', 'jogo', 'joia', 
        'lampiao', 'lapis', 'laranja', 'laranjeira', 'maca', 
        'maca do amor', 'mamao', 'margarida', 'mochila', 'navio', 
        'neve', 'notebook', 'nuvem', 'onibus', 'orquestra', 
        'ovo', 'palhaco', 'pao', 'pato', 'piramide', 
        'queijadinha', 'queijo', 'queimada', 'quero quero', 'raposa', 
        'ratoeira', 'relampago', 'relogio', 'rua', 'salada', 
        'sapato', 'sorvete', 'sorveteria', 'tambor', 'tartaruga', 
        'tesouro', 'travesseiro', 'unicornio', 'urna', 'urso', 
        'urubu', 'vaso', 'vassoura', 'vela', 'xadrez', 
        'xicara', 'yakisoba', 'zebra', 'ziper', 'zoologico'
    ],
    [
        'adventure', 'airplane', 'apple', 'astronaut', 'coconut' 
        'ball', 'balloon', 'banana', 'butterfly', 'ant', 
        'carrot', 'castle', 'cat', 'caterpillar', 'challenge', 
        'cheesecake', 'computer', 'crocodile', 'daisy', 'diamond', 
        'dog', 'dragon', 'drum', 'egg', 'elephant', 
        'cucumber', 'building', 'feather', 'fish', 'forest', 
        'globe', 'guitar', 'piano', 'hammer', 'hat', 
        'hippopotamus', 'house', 'ice cream', 'icecream', 'igloo', 
        'internet', 'island', 'jacket', 'jelly', 'jellyfish', 
        'kangaroo', 'king', 'kite', 'laptop', 'lemon', 
        'lemonade', 'lightning', 'lion', 'monkey', 'moon', 
        'mouse', 'necklace', 'nest', 'notebook', 'octopus', 
        'orange', 'salt', 'orchestra', 'owl', 'parrot', 
        'penguin', 'pizza', 'pyramid', 'queen', 'quilt', 
        'rainbow', 'rain', 'robot', 'rocket', 'skateboard', 
        'snowflake', 'star', 'sunflower', 'telescope', 'tiger', 
        'tree', 'umbrella', 'game', 'horse', 'unicorn', 
        'van', 'violin', 'volcano', 'waterfall', 'watermelon', 
        'whale', 'x ray', 'boat', 'xylophone', 'yacht', 
        'yak', 'yo yo', 'zebra', 'rabbit', 'tomato'
    ]
]

strings_dictionary: dict[str, dict[str, str]] = {
    'en' : {
        'set_idiom_description' : f'{boldStr('Idioms:')}\n\nEnglish (1)\nPortuguese (2)\nSet idiom (1,2): ',
        'set_idiom' : f'Choosen idiom: {boldStr('English')}.',
        'invalid_option' : 'Invalid option:',
        'set_difficulty' : 
            f'{boldStr('Difficulties:')}\n\n'
            'Easy (a): 7 tries\n'
            'Medium (b): 5 tries\n'
            'Hard (c): 3 tries\n'
            'Impossible (d): 1 try\n'
            'Select difficulty (a, b, c, d): ',
        'choosen_difficulty' : 'Choosen difficulty: ',
        'easy' : boldStr('-Easy-'),
        'medium' : boldStr('-Medium-'),
        'hard' : boldStr('-Hard-'),
        'impossible' : boldStr('-Impossible-'),
        'remaining_tries' : 'Remaining tries:',
        'type_guess' : 'Type a guess: ',
        'guess_incorrect' : 'Incorrect input. Type exactly one letter, please.',
        'already_guessed' : 'You already guessed the letter',
        'right_guess1' : 'Nice! The letter',
        'right_guess2' : 'is in the secret word!',
        'wrong_guess1' : 'Try again... The letter',
        'wrong_guess2' : 'isn\'t in the secret word.',
        'win' : boldStr('You win!'),
        'word' : 'The secret word was: ',
        'wrongs' : 'Wrong guesses: ',
        'tries_over1' : 'Your tries are over... The word was',
        'tries_over2' : '. Don\'t worry, you can do better!',
        'no_record' : 'No successful games played yet.',
        'play_again' : 'Do you want to play again? (y/n) ',
        'bye' : 'Thank you for playing!'
    },
    'pt' : {
        'set_idiom' : f'Idioma escolhido: {boldStr('Português')}.',
        'invalid_option' : 'Opção inválida:',
        'set_difficulty' : 
            f'{boldStr('Dificuldades:')}\n\n'
            'Fácil (a): 7 tentativas\n'
            'Médio (b): 5 tentativas\n'
            'Difícil (c): 3 tentativas\n'
            'Impossível (d): 1 tentativa\n'
            'Selecione a dificuldade (a, b, c, d): ',
        'choosen_difficulty' : 'Dificuldade escolhida: ',
        'easy' : boldStr('-Fácil-'),
        'medium' : boldStr('-Médio-'),
        'hard' : boldStr('-Difícil-'),
        'impossible' : boldStr('-Impossível-'),
        'remaining_tries' : 'Tentativas faltando:',
        'type_guess' : 'Escreva uma letra: ',
        'guess_incorrect' : 'Entrada incorreta. Escreva exatamente uma letra, por favor.',
        'already_guessed' : 'Você já escreveu a letra',
        'right_guess1' : 'Boa! A letra',
        'right_guess2' : 'está na palavra secreta!',
        'wrong_guess1' : 'Tente de novo... A letra',
        'wrong_guess2' : 'não está na palavra secreta.',
        'win' : boldStr('Você ganhou!'),
        'word' : 'A palavra secreta era: ',
        'wrongs' : 'Tentativas erradas: ',
        'tries_over1' : 'Suas tentativas acabaram... A palavra era',
        'tries_over2' : '. Não se preocupe, você consegue!',
        'no_record' : 'Nenhum jogo foi ganho ainda.',
        'play_again' : 'Você quer jogar de novo? (y/n) ',
        'bye' : 'Obrigado por jogar!'
    }
}