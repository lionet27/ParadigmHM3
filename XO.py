# Создайте программу для игры в ""Крестики-нолики"". Это программа в процедурном стиле.

import random


pos=['1','2','3','4','5','6','7','8','9']
posX=set()
posO=set()
winCombinations=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def printXO(position:list):
    print('-----------')
    print(f' {position[0]} | {position[1]} | {position[2]} ')
    print('-----------')
    print(f' {position[3]} | {position[4]} | {position[5]} ')
    print('-----------')
    print(f' {position[6]} | {position[7]} | {position[8]} ')

def X(pos :list):
    numberX=len(posX)
    while  numberX==len(posX):
        n=input('Игрок1, введите номер места,куда вы хотите поставить X: ')
        for i in range(0,9):
            if pos[i]==n:
                pos[i]='X'
                posX.add(i)
    
    if len(posX)>=3:
        for i in range(0,8):
            win=set(winCombinations[i])
            if win==win.intersection(posX):
                printXO(pos)
                print('Поздравляю Игрок1(X)! Вы выиграли!')
                quit()
    return pos

def O(pos:list):
    numberO=len(posO)
    while  numberO==len(posO):
        n=input('Игрок2, введите номер места,куда вы хотите поставить O: ')
        for i in range(0,9):
            if pos[i]==n:
                pos[i]='O'
                posO.add(i)
                
    if len(posO)>=3:
        for i in range(0,8):
            win=set(winCombinations[i])
            if win==win.intersection(posO):
                printXO(pos)
                print('Поздравляю Игрок2(O)! Вы выиграли!')
                quit()
    return pos 

def auto_O(pos:list):
    valid_choices = [element for element in pos if element in ['1','2','3','4','5','6','7','8','9']]
    random_choice = random.choice(valid_choices)
    
    for i in range(0,9):
        if pos[i]==random_choice:
            pos[i]='O'
            posO.add(i)
            print(" ")
                
    if len(posO)>=3:
        for i in range(0,8):
            win=set(winCombinations[i])
            if win==win.intersection(posO):
                printXO(pos)
                print('Поздравляю Игрок2(O)! Вы выиграли!')
                quit()
    return pos   


printXO(pos) 
pos=X(pos)

while (len(posX)+len(posO))!=9:
    printXO(pos)
    pos=auto_O(pos)
    printXO(pos)  
    pos=X(pos)
print('Ничья. Сыграйте еще раз')




 