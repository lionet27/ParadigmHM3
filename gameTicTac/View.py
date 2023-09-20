from Game import GameXO
from Players import Player, AutoPlayer

# функция start_game - запрашивает у пользователя вариант игры: между людьми или с компьютером. Так же запрашивает имена игроков и символы, которыми каждый игрок будет ходить.
# на основании введенных пользователем данных запускает игру
def start_game():

    choice_game=input("Input 1 - if two people want to play, input other symbol- if you want to play with computer:  ")
    name1=input("Input name player1: ")
    symbol1=input("Input symbol for player1: ")
    name2=input("Input name player2: ")
    symbol2=input("Input symbol for player2: ")
    player1=Player(name1,symbol1)
    if choice_game=='1':
        player2=Player(name2,symbol2)
    else:
        player2=AutoPlayer(name2,symbol2)

    game1=GameXO(player1,player2)
    game1.play_game()