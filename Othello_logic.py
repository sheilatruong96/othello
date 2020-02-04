# Sheila Truong 53588737
# Project 5

class GameState:
    
    def __init__(self, rows, columns, turn, color, win):
        
        self._rows = rows
        self._columns = columns
        self._turn = turn
        self._color = color
        self._win = win
        self._board = []


    def _valid_row(self, row):
        '''checks if the row is valid'''
        return 0 < row <= self._rows
    

    def _valid_col(self, col):
        '''checks if the columns are valid'''
        return 0 < col <= self._columns 


    def build_board(self):
        '''builds the board with the given rows and columns'''
        middle_row = int(self._rows / 2) - 1
        middle_col = int(self._columns / 2 ) - 1

        
        
        for row in range(self._rows):
            game_board = []
            for numb in range(self._columns):
                game_board.append('.')
            self._board.append(game_board)

        self._board[middle_row][middle_col] = self._color
        self._board[middle_row+1][middle_col+1] = self._color
        
        if self._color == 'B':
            self._board[middle_row+1][middle_col] = 'W'
            self._board[middle_row][middle_col+1] = 'W'
        else:
            self._board[middle_row+1][middle_col] = 'B'
            self._board[middle_row][middle_col+1] = 'B'
            
        return self._board
        


    def pieces_to_flip(self, row, col):
        '''returns a list of the pieces to flip'''
        directions = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        flip = []
        for item in directions:
            new_x = row + item[0]
            new_y = col + item[1]
            if self._valid_row(new_x) and self._valid_col(new_y):
                surroundings = self._board[new_x-1][new_y-1] 
                opposite = self._opposite_turn()
                possibly_flip = []
                while surroundings == opposite:
                    possibly_flip.append((new_x, new_y))
                    new_x += item[0]
                    new_y += item[1]
                    possibly_flip.append((new_x, new_y))
                    if self._valid_row(new_x) and self._valid_col(new_y):
                        if self._board[new_x-1][new_y-1] == self._turn:
                            flip.extend(possibly_flip[:-1])
                            
                    else:
                        break
        return flip
                               
    def flipped_pieces(self, row, col):
        '''goes through the list of pieces to flip and flip those pieces'''
        to_flip = self.pieces_to_flip(row, col)
        if len(to_flip) != 0:
            for self.item in to_flip:
                self._board[self.item[0]-1][self.item[1]-1] = self._turn
            return True
        else:
            return False
                
        
    def _opposite_turn(self):
        '''returns the opposite turn'''
        if self._turn == 'B':
            return 'W'
        else:
            return 'B'
        
    
    def drop(self, move):
        '''checks if the spot the user wants to drop, and if it is valid
        make the drop and do the correct flipping'''

        if self._board[int(move[0])-1][int(move[1])-1] == '.':
            if self.flipped_pieces(int(move[0]), int(move[1])):
                self._board[int(move[0])-1][int(move[1])-1] = self._turn #counting the row and col start with 0

                score = self.score()

                
                if self.winner():
                    return self.winner()
                else:
                    self._turn = self._opposite_turn()

                    return 'VALID'


            

    def score(self):
        '''returns the score of the game'''
        B_score = 0
        W_score = 0

        for element in self._board:
            for letter in element:
                if letter == 'B':
                    B_score += 1
                elif letter == 'W':
                    W_score += 1
        return [("B",B_score),("W",W_score)]


    def winner(self):
        '''checks to see who is the winner if the board is filled'''
        score_stuff = self.score()
        winning_Score = int(score_stuff[0][1]),int(score_stuff[1][1])
        empty_space = self.give_empty_spaces()
        if len(empty_space) == 0:
            if max(winning_Score) == min(winning_Score):
                return 'WINNER:', 'NONE'
            elif self._win == '>':
                score_to_return = max(winning_Score)
                if score_to_return == score_stuff[0][1]:
                    return "WINNER:",score_stuff[0][0]
                return "WINNER:",score_stuff[1][0]
            elif self._win == '<':
                score_to_return = min(winning_Score)
                if score_to_return == score_stuff[0][1]:
                    return "WINNER:",score_stuff[0][0]
                return "WINNER:",score_stuff[1][0]
     
                    



    def give_empty_spaces(self):
        '''gives a list of the empty spaces'''
        empty_space = []
        for row in range(self._rows):
            for col in range(self._columns):
                if self._board[row][col] == '.':
                    empty_space.append((row+1, col+1))
        return empty_space


    def empty_cell_winners(self):
        '''if there is empty space and no valid moves can be made then
        count the pieces and return the winner'''
        
        score_stuff = self.score() #[("B",B_score),("W",W_score)]
        winning_Score = (int(score_stuff[0][1]),int(score_stuff[1][1]))
        opposite = self._opposite_turn()
        empty_space = self.give_empty_spaces()



        for item in empty_space:
            if len(self.pieces_to_flip(item[0], item[1])) != 0:
                return
        print("No valid moves for turn", self._turn)
        self._turn = self._opposite_turn()
        print("It is ", self._turn, "'s turn.")

        for item in empty_space:
            if len(self.pieces_to_flip(item[0], item[1]))!= 0: #checks oppo empty space valid
                return
                
        if max(winning_Score) == min(winning_Score):
                return 'WINNER:', "NONE"
        elif self._win == '>':
            score_to_return = max(winning_Score)
            if score_to_return == score_stuff[0][1]:
                return "WINNER:",score_stuff[0][0]
            return "WINNER:",score_stuff[1][0]
        elif self._win == '<':
            score_to_return = min(winning_Score)
            if score_to_return == score_stuff[0][1]:
                return "WINNER:",score_stuff[0][0]
            return "WINNER:",score_stuff[1][0]
  











    

