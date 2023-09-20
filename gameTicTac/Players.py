import random

# класс Player - это класс игрока с основными функциями move- игрок делает ход, check_win - проверка на выйгрыш
# AutoPlayer - наследник класса  Player, с переопределенной функцией move - компьтер делает ход случайным образом. 
# Потом можно будет прописать более сложную логику хода.
class Player:

    def __init__(self,name:str,symbol:str):
        self.name=name
        self.symbol=symbol
        self.moves=set()
  
    def get_pos_player(self):
        return self.moves 
    
    def print_pos(self):
        print(self.moves)

    def move(self, pos :list)-> list:
        number=len(self.moves)
        while  number==len(self.moves):
            n=input(self.name+', input number of the place, where you want to place '+self.symbol+':  ')
            for i in range(0,9):
                if pos[i]==n:
                    pos[i]=self.symbol
                    self.moves.add(i)
            
        return pos
    
    def check_win(self):
        winCombin=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        if len(self.moves)>=3:
            for i in range(0,8):
                win=set(winCombin[i])
                if win==win.intersection(self.moves):
                    print(self.name+', Congratulations! You won!')
                    quit()


class AutoPlayer(Player):
    

    def move(self, pos :list)-> list:
          
        valid_choices = [element for element in pos if element in ['1','2','3','4','5','6','7','8','9']]
        random_choice = random.choice(valid_choices)

        for i in range(0,9):
            if pos[i]==random_choice:
                pos[i]=self.symbol
                self.moves.add(i)
                print(" ")
                    
        return pos
    

   