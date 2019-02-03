'''
Ryan Lueder
2 February 2019


Okay lets draw some stuff!
'''

from tkinter import *


class Window(Tk):
    '''
    This is my omega class that contains literally everything
    '''

    '''
    These were all global variables until I remembered about how you told me that one dude's
    grade dropped from an A to a D-. Not that this is even graded or anything. 
    '''
    WINDOW_DIM = 600
    LINE_SIZE = 3
    SQR_SIZE = 198
    XO_SIZE = 20

    COLOR_O = 'red4'
    COLOR_X = 'goldenrod2'
    COLOR_L = 'gray1'
    COLOR_DRAW ='gray40'

    '''
    just noticed some inconsistancy with how i named these variables however Python IDLE
    doesn't have a 'replace all' option, and i cant be bothered with copying this into the
    CS50 IDE
    '''
    TITLE_COLOR = 'cyan'
    GRID_COLOR = 'white'

    GRID_TITLE = 0
    GRID_GAME = 1
    GRID_DONE = 2

    #the boxes around the text were clipping through the text so i made this to make those boxes larger
    TOO_SMALL = 40

    #man i wish i knew why there are two __init__ statements but the tutorial i watched didnt go into it
    def __init__(self):
        Tk.__init__(self)
        self.canvas = Canvas(height=self.WINDOW_DIM, width=self.WINDOW_DIM, bg=self.TITLE_COLOR)
        self.canvas.pack()

        #need to track which player's turn it is
        self.player_turn = 0

        #makes an empty board so that it can check for a win
        self.board_space = [[0, 0, 0],[0, 0, 0],[0, 0, 0],]

        #when you click, it does something different for each game state. ie: when youre in the game, it makes an 'X'
        self.game_state = self.GRID_TITLE
        #shows the title screen
        self.title_screen()

        self.canvas.bind("<Button-1>", self.leftClick)


    #resets the board memory
    def game_reset(self):
        self.canvas.delete('all')
        self.game_state = self.GRID_DONE
        self.board_space = [[0, 0, 0],[0, 0, 0],[0, 0, 0],]


    #checks if the game is won
    def game_won(self):

        '''
        When any of these conditions are met they will:
        reset the board memory
        draw the end game screen based on who won (or if it ended in draw)
        reset player turn count
        '''

        #these are the 3 horizontal straight lines
        for x in range(3):

            if(self.board_space[x][0] == self.board_space[x][1] and self.board_space[x][1] == self.board_space[x][2] and (self.board_space[x][0] == 1 or self.board_space[x][0] == 2)):
                self.game_reset()
                #print("Win condition 1")
                if(self.player_turn%2 == 0):
                    self.end_screen_x()
                else:
                    self.end_screen_o()
                self.player_turn = 0


        #these are the 3 vertical straight lines
        for y in range(3):

            if(self.board_space[0][y] == self.board_space[1][y] and self.board_space[1][y] == self.board_space[2][y] and (self.board_space[0][y] == 1 or self.board_space[0][y] == 2)):
                self.game_reset()
                #print("Win condition 2")
                if(self.player_turn%2 == 0):
                    self.end_screen_x()
                else:
                    self.end_screen_o()
                self.player_turn = 0


        #this is the downward diagonal straight line
        if(self.board_space[0][0] == self.board_space[1][1] and self.board_space[1][1] == self.board_space[2][2] and (self.board_space[0][0] == 1 or self.board_space[0][0] == 2)):
            self.game_reset()
            #print("Win condition 3")
            if(self.player_turn%2 == 0):
                self.end_screen_x()
            else:
                self.end_screen_o()
            self.player_turn = 0


        #this is the upward diagonal straight line
        if(self.board_space[0][2] == self.board_space[1][1] and self.board_space[1][1] == self.board_space[2][0] and (self.board_space[0][2] == 1 or self.board_space[0][2] == 2)):
            self.game_reset()
            #print("Win condition 4")
            if(self.player_turn%2 == 0):
                self.end_screen_x()
            else:
                self.end_screen_o()
            self.player_turn = 0

        #if the move count gets nine and the previous if-statements havent been triggered that means no one has straight lines
        if(self.player_turn == 9):
            self.game_reset()
            self.end_screen_draw()
            #aprint("Win condition 5")
            self.player_turn = 0

    def leftClick(self, event=None):
        #these were my debugging statements
        #print(event.x)
        #print(event.y)

        #the first click you do draws the board
        if(self.game_state == 0):
            self.draw_board()
        #all proceding clicks makes X's and O's
        elif(self.game_state == 1):

            #splits the board into 9 squares instead of 600^2 squares
            for i in range(3):
                if(event.x > self.SQR_SIZE*i and event.x < self.SQR_SIZE*(i+1)):
                    x_coord = i

            for i in range(3):
                if(event.y > self.SQR_SIZE*i and event.y < self.SQR_SIZE*(i+1)):
                    y_coord = i

            #checks if the spot clicked is available
            if(self.board_space[x_coord][y_coord] == 0):

                if(self.player_turn%2 == 0):
                    self.canvas.create_oval(self.SQR_SIZE*x_coord+self.XO_SIZE, self.SQR_SIZE*y_coord+self.XO_SIZE, self.SQR_SIZE*(x_coord+1)-self.XO_SIZE, self.SQR_SIZE*(y_coord+1)-self.XO_SIZE, width=self.XO_SIZE, outline=self.COLOR_O)
                    #print("Player turn=", self.player_turn)
                    self.player_turn += 1
                    self.board_space[x_coord][y_coord] = 1
                else:
                    self.canvas.create_line(self.SQR_SIZE*x_coord+self.XO_SIZE, self.SQR_SIZE*y_coord+self.XO_SIZE, self.SQR_SIZE*(x_coord+1)-self.XO_SIZE, self.SQR_SIZE*(y_coord+1)-self.XO_SIZE, width=self.XO_SIZE, fill=self.COLOR_X)
                    self.canvas.create_line(self.SQR_SIZE*(x_coord+1)-self.XO_SIZE, self.SQR_SIZE*y_coord+self.XO_SIZE, self.SQR_SIZE*x_coord+self.XO_SIZE, self.SQR_SIZE*(y_coord+1)-self.XO_SIZE, width=self.XO_SIZE, fill=self.COLOR_X)
                    #print("Player turn=", self.player_turn)
                    self.player_turn += 1
                    self.board_space[x_coord][y_coord] = 2

            #checks if the game has been won every single click
            self.game_won()
        else:
            #once the game state is finished, the next click will re-draw the board
            self.draw_board()


    #draws the board
    def draw_board(self):

        #sets the game state to when the players are actually playing
        self.game_state = self.GRID_GAME
        self.canvas.delete('all')

        #covering everything up with a white background
        self.canvas.create_rectangle(0,0,self.WINDOW_DIM,self.WINDOW_DIM, fill=self.GRID_COLOR)

        #makes a pretty grid :)
        for i in range(1,3):
            self.canvas.create_line(self.SQR_SIZE*i, 0, self.SQR_SIZE*i, self.WINDOW_DIM, width=self.LINE_SIZE, fill=self.COLOR_L)
            self.canvas.create_line(0, self.SQR_SIZE*i, self.WINDOW_DIM, self.SQR_SIZE*i, width=self.LINE_SIZE, fill=self.COLOR_L)

    #the first screen the player see's
    def title_screen(self):

        #draws the title screen
        self.canvas.create_rectangle(0,0,self.WINDOW_DIM,self.WINDOW_DIM, fill=self.TITLE_COLOR)
        self.canvas.create_rectangle(self.SQR_SIZE-self.TOO_SMALL, self.SQR_SIZE-self.TOO_SMALL, self.WINDOW_DIM-self.SQR_SIZE+self.TOO_SMALL, self.WINDOW_DIM-self.SQR_SIZE+self.TOO_SMALL, fill=self.GRID_COLOR)
        self.canvas.create_text(int(self.WINDOW_DIM/2),int(self.WINDOW_DIM/2),text="[Click to play!]", font=('System', 20))

    def end_screen_x(self):
        #yknow im not even sure why i keep these delete statements in here they dont work for some reason
        self.canvas.delete('all')

        #draws the end screen when player X wins
        self.canvas.create_rectangle(0,0,self.WINDOW_DIM,self.WINDOW_DIM, fill=self.COLOR_X)
        self.canvas.create_rectangle(self.SQR_SIZE-self.TOO_SMALL, self.SQR_SIZE-self.TOO_SMALL, self.WINDOW_DIM-self.SQR_SIZE+self.TOO_SMALL, self.WINDOW_DIM-self.SQR_SIZE+self.TOO_SMALL, fill=self.GRID_COLOR)
        self.canvas.create_text(int(self.WINDOW_DIM/2),int(self.WINDOW_DIM/2),text="[Player 'X' wins!]", font=('System', 20))

    def end_screen_o(self):
        self.canvas.delete('all')

        #draws the end screen when player O wins
        self.canvas.create_rectangle(0,0,self.WINDOW_DIM,self.WINDOW_DIM, fill=self.COLOR_O)
        self.canvas.create_rectangle(self.SQR_SIZE-self.TOO_SMALL, self.SQR_SIZE-self.TOO_SMALL, self.WINDOW_DIM-self.SQR_SIZE+self.TOO_SMALL, self.WINDOW_DIM-self.SQR_SIZE+self.TOO_SMALL, fill=self.GRID_COLOR)
        self.canvas.create_text(int(self.WINDOW_DIM/2),int(self.WINDOW_DIM/2),text="[Player 'O' wins!]", font=('System', 20))

    def end_screen_draw(self):
        self.canvas.delete('all')

        #draws the screen when its a draw
        self.canvas.create_rectangle(0,0,self.WINDOW_DIM,self.WINDOW_DIM, fill=self.COLOR_DRAW)
        self.canvas.create_rectangle(self.SQR_SIZE-self.TOO_SMALL, self.SQR_SIZE-self.TOO_SMALL, self.WINDOW_DIM-self.SQR_SIZE+self.TOO_SMALL, self.WINDOW_DIM-self.SQR_SIZE+self.TOO_SMALL, fill=self.GRID_COLOR)
        self.canvas.create_text(int(self.WINDOW_DIM/2),int(self.WINDOW_DIM/2),text="[Draw!]", font=('System', 20))


root = Window()
root.mainloop()
