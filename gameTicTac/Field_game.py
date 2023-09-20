# класс, отвечающий за значение и отрисовку поля игры
class Field:
    
    def __init__(self):
       
        self.position=['1','2','3','4','5','6','7','8','9']

    def print_field_xo(self):
        print('-----------')
        print(f' {self.position[0]} | {self.position[1]} | {self.position[2]} ')
        print('-----------')
        print(f' {self.position[3]} | {self.position[4]} | {self.position[5]} ')
        print('-----------')
        print(f' {self.position[6]} | {self.position[7]} | {self.position[8]} ')  

    def get_position(self):
        return self.position  
    
    def change_position(self,pos:list):
        self.position=pos