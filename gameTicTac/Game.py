from Field_game import Field
from Players import Player

# класс GameXO - это класс, реализующий основную логику игры
class GameXO:
    def __init__(self,player1: Player, player2:Player):
        self.field=Field()
        self.player1=player1
        self.player2=player2

    

    def play_game(self):
        self.field.print_field_xo()
        self.field.change_position(self.player1.move(self.field.get_position()))
        self.field.print_field_xo()
               
        
        while (len(self.player1.get_pos_player())+len(self.player2.get_pos_player()))!=9:
            self.field.change_position(self.player2.move(self.field.get_position()))
            self.field.print_field_xo()
            self.player2.check_win()
            self.field.change_position(self.player1.move(self.field.get_position()))
            self.field.print_field_xo()
            self.player1.check_win()

        print('Draw. Play it again')