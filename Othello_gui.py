# Sheila Truong 53588737
# Project 5

import tkinter
import Othello_logic

_DEFAULT_FONT = ('Helvetica', 24)



class OthelloDialogBox:
    def __init__(self, game_logic: Othello_logic.GameState):

        self.game_logic = game_logic
        # dialog window
        self._dialog_window = tkinter.Tk()
        self._dialog_window_canvas = tkinter.Canvas(
            master = self._dialog_window, width = 100, height = 300)
        self._dialog_window.title('Options')

        
        


        title_label = tkinter.Label(master = self._dialog_window, text = 'Othello Game Options(FULL)', font = _DEFAULT_FONT)

        title_label.grid(
            row = 0, column = 0, columnspan = 5, padx = 5, pady = 5, sticky = tkinter.N)

        
        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.rowconfigure(6, weight = 1)


        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)
        self._dialog_window.columnconfigure(2, weight = 1)
        self._dialog_window.columnconfigure(3, weight = 1)


        

            #row box

        row_label = tkinter.Label(master = self._dialog_window, text = 'Row:')
        
        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10, columnspan = 3, sticky = tkinter.W)

        self._row_spinbox = tkinter.Spinbox(
            self._dialog_window,from_ = 4, to = 16, increment = 2, wrap = True)

        self._row_spinbox.grid(
            row = 1, column = 1, padx = 10, pady = 10, sticky = tkinter.E, columnspan = 2)


            #column box

        column_label = tkinter.Label(master = self._dialog_window, text = 'Column:')

        column_label.grid(
            row = 2, column = 0, padx = 10,
            pady = 10, sticky = tkinter.W)

        self._col_spinbox = tkinter.Spinbox(
            self._dialog_window, from_ = 4, to = 16, increment = 2, wrap = True)

        self._col_spinbox.grid(
            row = 2, column = 1, padx = 10, pady = 10, sticky = tkinter.E, columnspan = 2)


            # Black or white first

        first_player_label = tkinter.Label(master = self._dialog_window, text = 'Starting Player:')

        first_player_label.grid(
            row = 3, column= 0, padx = 10,
            pady = 10, sticky = tkinter.W)

        self._first_player = tkinter.StringVar()

        self._first_player_radiobutton = tkinter.Radiobutton(self._dialog_window,
                                                             text = 'Black', variable = self._first_player, value = 'Black')
        self._first_player_radiobutton2 = tkinter.Radiobutton(self._dialog_window,
                                                             text = 'White', variable = self._first_player, value = 'White')

        self._first_player_radiobutton.grid(
            row = 3, column = 1, padx = 10, pady = 10, sticky = tkinter.E)

        self._first_player_radiobutton2.grid(
            row = 3, column = 2, padx = 10, pady = 10, sticky = tkinter.E)

            # Center upper left color

        upper_left_center_label = tkinter.Label(master = self._dialog_window,
                                                text = 'Upper Left Disc Color:')

        upper_left_center_label.grid(
            row = 4, column = 0, padx = 10,
            pady = 10, sticky = tkinter.W)

        self._upper_left_center = tkinter.StringVar()

        self._upper_left_center_radiobutton = tkinter.Radiobutton(self._dialog_window,
                                                                  text = 'Black', variable = self._upper_left_center, value = 'Black')
        self._upper_left_center_radiobutton2 = tkinter.Radiobutton(self._dialog_window,
                                                                   text = 'White', variable = self._upper_left_center, value = 'White')
        self._upper_left_center_radiobutton.grid(
            row = 4, column = 1, padx = 10, pady = 10, sticky = tkinter.E)

        self._upper_left_center_radiobutton2.grid(
            row = 4, column = 2, padx = 10, pady = 10, sticky = tkinter.E)

            # Winner options

        winner_option_label = tkinter.Label(master = self._dialog_window,
                                            text = 'Winner Option:')

        winner_option_label.grid(
            row = 5, column = 0, padx = 10,
            pady = 10, sticky = tkinter.W)

        self._winner_option = tkinter.StringVar()

        self._winner_option_radiobutton = tkinter.Radiobutton(self._dialog_window,
                                                             text = 'More Discs', variable = self._winner_option, value = 'More Discs')
        self._winner_option_radiobutton2 = tkinter.Radiobutton(self._dialog_window,
                                                               text = 'Less Discs', variable = self._winner_option, value = 'Less Discs')
        self._winner_option_radiobutton.grid(
            row = 5, column = 1, padx = 10, pady = 10, sticky = tkinter.E)

        self._winner_option_radiobutton2.grid(
            row = 5, column = 2, padx = 10, pady = 10, sticky = tkinter.E)

            # Play button 



        play_button = tkinter.Button(
            master = self._dialog_window, text = 'PLAY',
            command = self._on_play_button)

        play_button.grid(
            row = 6, column = 1, sticky = tkinter.E)


            # Cancel Button
            
        cancel_button = tkinter.Button(
            master = self._dialog_window, text = 'CANCEL',
            command = self._on_cancel_button)
        
        cancel_button.grid(
            row = 6, column = 0, sticky = tkinter.E)
        

        #variables 

        self._start_clicked = False




    def _on_play_button(self) -> None:
        '''get inputs from user choices, and send that to
        othelloapplication, then destory dialog box'''
        
        self._start_clicked = True
        
        row = self._row_spinbox.get()
        col = self._col_spinbox.get()
        first = self._first_player.get()
        upper = self._upper_left_center.get()
        winner = self._winner_option.get()


        MainOthelloApp = OthelloApplication(row, col, first, upper, winner, self.game_logic)
        
        
        self._dialog_window.destroy()

        
    def _on_cancel_button(self) -> None:
        '''when user clicks cancel, destory the dialog box'''
        
        self._dialog_window.destroy()

    def start(self) -> None:
        '''keeps dialog window running until it gets destroyed '''
        self._dialog_window.mainloop()


        

class OthelloApplication:
    def __init__(self, row, col, first, upper, winner, game_logic: Othello_logic.GameState):
        

        self.game_logic = game_logic

        # variables

        self._row = row
        self._col = col
        self._first = first
        self._upper = upper
        self._winner = winner
        
        self.coordinates = {}
        self.frac_coord = {}

        #frac coordinates of the circles
        self.frac_points = []
        
        self.circles = []
        self.top_leftxy = ''
        self.bottom_rightxy = ''

 #       self.othello_game_state = ''
        self.othello_game_state = self.game_logic(int(self._row), int(self._col), self._first[0], self._upper[0], self._winner)

        # canvas board
        
        self._root_window = tkinter.Tk()
        self._root_window.title('Othello Game')

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 500,
            background = 'forest green')

        self._canvas.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)



        self._canvas.bind('<Button-1>', self._redraw_circle)
        self._canvas.bind('<Configure>', self._on_canvas_resized)




        #Status box

        self.status_frame = tkinter.Frame(master = self._root_window, background = 'gray')
 
        self.status_frame.grid(
            row = 1, sticky = tkinter.S + tkinter.N + tkinter.E + tkinter.W)

        self.status_label = tkinter.Label(master = self.status_frame, text = 'Turn: ', font = _DEFAULT_FONT, background = 'gray')
        self.status_label.grid(
            row = 1, column = 0, sticky = tkinter.W)

        status_label = tkinter.Label(master = self.status_frame, text = self._first, font = _DEFAULT_FONT, background = 'gray')
        status_label.grid(
            row = 1, column = 2, columnspan = 2, sticky = tkinter.E)


        status_label2 = tkinter.Label(master = self.status_frame, text = 'Score: ', font = _DEFAULT_FONT, background = 'gray')
        status_label2.grid(
            row = 2, column = 0, sticky = tkinter.W)

        
        score_label = tkinter.Label(master = self.status_frame, text = 'B: 2 W: 2', font = _DEFAULT_FONT, background = 'gray')
        score_label.grid(
            row = 2, column = 2, sticky = tkinter.E)

        
    def build_board(self) -> None:
        '''when resized it will delete the canvas and redraws grid, and
        the center four circles'''

        self._canvas.delete(tkinter.ALL)
        
        # create the rectangles 
        width = self._canvas.winfo_width() 
        height = self._canvas.winfo_height()
        each_col = width / int(self._col)
        each_row = height / int(self._row)

        for row in range(int(self._row)):
            for col in range(int(self._col)):
                
                top_x = col * each_col
                top_y = row * each_row

                bottom_x = top_x + each_col
                bottom_y = top_y + each_row

                self._canvas.create_rectangle(top_x, top_y, bottom_x, bottom_y)

                frac_topx = top_x / width

                frac_topy = top_y / height

                frac_bottomx = bottom_x / width

                frac_bottomy = bottom_y / height

                self.coordinates[row+1, col+1] = (top_x, top_y), (bottom_x, bottom_y)
                self.frac_coord[row + 1, col+ 1] = (frac_topx, frac_topy),(frac_bottomx, frac_bottomy)


                
        # create the circles in the center of the board
        
        self.othello_game_state.build_board()


        for row in range(int(self._row)):
            for col in range(int(self._col)):
                   
                top_x = col * each_col
                top_y = row * each_row

                bottom_x = top_x + each_col
                bottom_y = top_y + each_row
                
                if self.othello_game_state._board[row][col] != '.':
                    
                    if self.othello_game_state._board[row][col] == 'B':                        
                        self._canvas.create_oval(top_x, top_y, bottom_x, bottom_y, fill = 'black')
                        
                    else:
                        self._canvas.create_oval(top_x,top_y, bottom_x, bottom_y, fill = 'white')

        #redraw circles when resize

        for item in self.frac_points:
                x, y = item
                coord_x, coord_y = x
                pixel = coord_x * width
                pixel2 = coord_y * height

                coord2_x, coord2_y = y
                pixel3 = coord2_x * width
                pixel4 = coord2_y * height
                self._canvas.create_oval(pixel, pixel2, pixel3, pixel4, fill = 'black')






           

                
    def _redraw_circle(self, event: tkinter.Event) -> None:
        '''redraws the circles when it gets resized'''

        
        width = self._canvas.winfo_width() 
        height = self._canvas.winfo_height()

        
        pixel_click_point = (event.x, event.y)
    

        for item in self.coordinates:
            x = self.coordinates[item]
            if x[0][0] <= pixel_click_point[0] <= x[1][0]:
                if x[0][1] <= pixel_click_point[1] <= x[1][1]:
                            
                    if self.othello_game_state.drop(item) == 'VALID':

                        self.frac_points.append(self.frac_coord[item])

                        if self.othello_game_state._turn == 'B':
                            self._canvas.create_oval(x, fill = 'white')
                            
                            status_label = tkinter.Label(master = self.status_frame, text = 'Black', font = _DEFAULT_FONT, background = 'gray')
                            status_label.grid(
                                row = 1, column = 2, sticky = tkinter.E)
                            
                        else:
                            self._canvas.create_oval(x, fill = 'black')
                            status_label = tkinter.Label(master = self.status_frame, text = 'White', font = _DEFAULT_FONT, background = 'gray')
                            status_label.grid(
                                row = 1, column = 2, sticky = tkinter.E)


           
        for value in self.othello_game_state._board:
            for position in value:
                if position == 'B':
                    self._canvas.create_oval(self.coordinates[self.othello_game_state.item], fill = 'black')
                if position == 'W':
                    self._canvas.create_oval(self.coordinates[self.othello_game_state.item], fill = 'white')



                    

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''when canvas is resized it will draw everything back from the board'''

        self.build_board()


    def start(self) -> None:
        '''keeps root window running until it gets cancelled'''
        self._root_window.mainloop()



    


    
    
        
        
        


if __name__ == '__main__':
    OthelloDialogBox(Othello_logic.GameState).start()









    
