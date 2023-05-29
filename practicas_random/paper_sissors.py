
from enum import Enum

class GameChoice(Enum):
    INVALID = -1
    PAPER = 0
    ROCK = 1
    SCISSORS = 2
    QUIT = 3


def game_loop():
    """
    Arranca el bucle principal del juego
    """
    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cuando no quiera parar
        if not is_exit(user_choice):
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: salgo
            break


def read_user_choice():
    """
    Imprime un menu de instrucciones y lee la respuesta del usuario
    mediante una llamada a `input`.
    Devuelve lo que haya elegido el usario, como una cadena
    """
    user_choice = GameChoice.INVALID

    while user_choice == GameChoice.INVALID:
        print('Select one number:')
        print(f'{GameChoice.PAPER.value}. Paper')
        print(f'{GameChoice.ROCK.value}. Rock')
        print(f'{GameChoice.SCISSORS.value}. Scissors')
        print('-------------------')
        print(f'{GameChoice.QUIT.value}. Quit the game')
        
        try:
            user_choice = GameChoice(int(input('Enter your choice:')))
        except ValueError: # ha escrito algo que no se puede 
                        # convertir en int o en un UserChoice
            user_choice = GameChoice.INVALID
        

        # validamos lo que haya escrito
        if user_choice != GameChoice.INVALID: 
            break   # OK, nos vamos
        else:
            user_choice = GameChoice.INVALID    # antes te cansarás tú
    
    return user_choice 

def is_exit(user_choice):
    """
    Predicado que recib ela respuesta del usuario y devuelve `True` si
    ha pedido salir del juego
    """
    return user_choice == GameChoice.QUIT


def generate_computer_choice():
    """
    Genera una jugada del ordenador de forma aleatoria. El ordenador no puede elegir
    para el juego, solo Piedra, Papel o Tijera
    """
    from random import choice

    return choice([GameChoice.PAPER, GameChoice.ROCK, GameChoice.SCISSORS])




def evaluate_move(user_choice, computer_choice):
    """
    Recibe dos jugadas, determina cual ha ganado y devuelve un mensaje con el resultado.
    Por ejemplo: recibe Papel y Piedra, y devuelve "Papel envuelve Piedra"
    """
    assert user_choice != GameChoice.INVALID and user_choice != GameChoice.QUIT
    assert computer_choice != GameChoice.INVALID and computer_choice != GameChoice.QUIT

    result = ''
    if user_choice == GameChoice.PAPER:
        if computer_choice == GameChoice.PAPER:
            result = "It's a tie!"
        elif computer_choice == GameChoice.ROCK:
            result = "You win! Paper covers Rock."
        elif computer_choice == GameChoice.SCISSORS:
            result = "You lose! Scissors cut Paper"
        
    elif user_choice == GameChoice.ROCK:
        if computer_choice == GameChoice.ROCK:
            result = "It's a tie!"
        elif computer_choice == GameChoice.PAPER:
            result = "You lose! Paper covers Rock."
        elif computer_choice == GameChoice.SCISSORS:
            result = "You win! Rock smashes Rock"

    elif user_choice == GameChoice.SCISSORS:
        if computer_choice == GameChoice.SCISSORS:
            result = "It's a tie!"
        elif computer_choice == GameChoice.ROCK:
            result = "You lose! Rock smashes Scissors."
        elif computer_choice == GameChoice.PAPER:
            result = "You win! Scissors cut Paper"
    
    assert result != ''
    return result

def print_result(result):
    """
    Imprime en plan bonito el resultado.
    No devuelve nada
    """
    print('\n\n----------------------')
    print('Game Over!')
    print(result)
    print('----------------------\n\n')


def log_error(error):
    """
    Recibe una excepción del tipo que sea y guarda toda la info
    en sentry.io o lo que sea
    """
    print('Unhandled Exception!')
    print(error)


if __name__ == "__main__":

    try:
        game_loop()
    except Exception as error:
        # Si algo ha llegado hasta aquí, 
        # es un pánico del copón. Poco se puede hacer
        # registra toda la info y palma
        log_error(error)