# Sheila Truong 53588737
# Project 4


import Othello_game_logic


def user_row():
    '''user inputs the number of rows, has to be
    even integer between 4 and 16 (inclusive)'''

    user = int(input())

    if user % 2 == 0:
        if user >= 4 and user <= 16:
            return user

def user_column():
    '''user inputs the number of columns, has to be an even integer
    between 4 and 16(inclusive) does not have to be the same number as
    the number of rows'''

    user = int(input())

    if user % 2 == 0:
        if user >= 4 and user <= 16:
            return user

def player_turn():
    ''' allows the player to pick either B (black) or W (white) goes
    first'''
    
    return str(input())

def color_position():
    '''the player picks which color B (black) or W (white) to go in the
    top left position in the center of the board'''

    return str(input())

def win_option():
    '''user gets to chooose > (player with the most discs on the board
    at the end of game wins), < (player with the fewest discs on the
    board at the end of the game wins)'''

    return str(input())

def current_move():
    '''user choose where to place their discs, two integers on a line,
    separated by a space (first num = row, second num = col)'''

    return str(input())

    
def handle_inputs():
    '''takes the value from the functions and sends it to
    the class module to be initialized'''

    rows = user_row()

    columns = user_column()

    turn = player_turn()

    color = color_position()

    win = win_option()

    board = Othello_game_logic.GameState(rows, columns, turn, color, win)

    return board

def play_game():
    print('FULL')
    
    board = handle_inputs()
    
    print('B: 2  W: 2')
    
    board.build_board()



    while True:
        condition = board.empty_cell_winners()
        if condition != None:
            print(condition[0],condition[1])
            break
        
        move = current_move()

        winner = board.drop(move)

        if winner != None:
            print(winner[0],winner[1])
            break




        

        

        

    
if __name__ == '__main__':

    play_game()





    

    
