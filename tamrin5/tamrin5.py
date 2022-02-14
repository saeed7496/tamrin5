
from colorama import Fore
from datetime import datetime
def check():
    n=len(game)
    l, k, m=[], [], []
    result=0
    for i in range(n):
         l.append(game[i][i])           #ghotr asli#
         
         k.append(game[i][2-i])         #ghotr faree#
         
         m.clear()                      #sotoon ha#
         for j in range(n):
             m.append(game[j][i])     
         
         if game[i] == n*['X']:         #satr ha#
             result=1
             break
         elif game[i] == n*['O']:
             result=2
             break
         elif l ==  n*['X']:
             result=1
             break         
         elif l == n*['O']:
             result=2
             break
         elif k == n*['X']:
             result=1
             break
         elif k== n*['O']:
             result=2
             break
         elif m== n*['X']:
             result=1
             break
         elif m== n*['O']:
             result=2
             break
    if result==1:
        print(Fore.WHITE+'player 1 is winer')
    elif result == 2:
        print(Fore.WHITE+'player 2 is winer')
    if result==1 or result==2:
        result=1
    return result

def row_col(n):
    while True:
        row=int(input('choose row: '))
        col=int(input('choose column: '))
        if 0<= row <=2 and 0 <= col <=2 and game[row][col]=='_':
            if n%2==0:
                game[row][col]='X'
            else:
                game[row][col]='O'
            break
        else:
            print('try again')
            
def show_game():
    for i in range(3):
        for j in range((3)):
            if game[i][j]=='X':
                print(Fore.YELLOW+game[i][j],end=' ')
                
            elif game[i][j]=='_':
                print(Fore.RESET+game[i][j],end=' ')
                                
            elif game[i][j]=='O':
                print(Fore.CYAN+game[i][j],end=' ')
            else:print('error') 
        print()
    print()


def choose_computer():
    n=len(game)
    while True:
        import random
        i=random.randint(0, n-1)
        j=random.randint(0, n-1)
        game[i][j]
        if game[i][j]=='_':
            game[i][j]='O'
            break


while True:
    game=[['_','_','_'],
          ['_','_','_'],
          ['_','_','_']]
    show_game()
    ask=input('pc or person? ')    
    n=0
    start=datetime.now()
    while n<=9:              
        print(Fore.WHITE+'player1',end='')
        row_col(n)
        show_game()
        n+=1
        c=check()
        if c==1 :break
        if n==9 and c== 0:
            print('game is equal')
            break
        if ask=='pc':
            print(Fore.WHITE+'player 2')
            choose_computer() 
            show_game()
            n+=1
            c=check()
            if c==1: break
            elif c==0 and n>=9:
                print(Fore.WHITE+'game is equal')
        if ask=='person':
            print(Fore.WHITE+'player 2')
            row_col(n)
            show_game()
            n+=1
            c=check()
            if c==1: break
            elif c==0 and n>=9:
                print(Fore.WHITE+'game is equal')
    print(Fore.WHITE+datetime.now()-start)
    ex=input(Fore.WHITE+'game or exit?')
    if ex =='exit':
        print(Fore.WHITE+'tank you')
        break
   