from random import shuffle
from copy import deepcopy

YELLOW = '\033[1;33;40m'
RED = '\033[1;31;40m'

class Board:
    def __init__(self):
        self.columns = 8
        self.rows = 7
        self.board = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def add_piece(self, column, color):
        """ add a piece belonging to the given player to the specified column """
        piece = 1 if color == "yellow" else 2
        for row in range(self.rows-1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = piece
                return column
        raise ValueError(f"Column {column} is full")

    def move_for_ai(self, col, piece):
        tempBoard = deepcopy(self)
        for row in range(tempBoard.rows-1, -1, -1):
            if tempBoard.board[row][col] == 0:
                tempBoard.board[row][col] = piece
                return tempBoard, row, col

    def check_win(self, color):
        """ check if the given player has won the game """
        # Check for horizontal win
        piece = 1 if color == "yellow" else 2
        for row in range(self.rows):
            for col in range(self.columns-3):
                if self.board[row][col:col+4] == [piece]*4:
                    return True
        # Check for vertical win
        for col in range(self.columns):
            for row in range(self.rows-3):
                if [self.board[row+i][col] for i in range(4)] == [piece]*4:
                    return True
        # Check for diagonal win
        for row in range(self.rows-3):
            for col in range(self.columns-3):
                if self.board[row][col] == piece and self.board[row+1][col+1] == piece and self.board[row+2][col+2] == piece and self.board[row+3][col+3] == piece:
                    return True
                if self.board[row][col+3] == piece and self.board[row+1][col+2] == piece and self.board[row+2][col+1] == piece and self.board[row+3][col] == piece:
                    return True
        return False

    def get_free_cols(self):
        """ gets playable columns at current state """
        free_cols = []
        index = 0
        for col in self.board[0]:
            if col == 0:
                free_cols.append(index)
            index += 1
        shuffle(free_cols)
        return free_cols

    def isValid(self, col):
        """"checks if move is valid"""
        for row in range(self.rows):
            if self.board[row][col] == 0:
                return True
        return False

    def __str__(self):
        """ return a string representation of the board """
        s = ""
        for row in self.board:
            s += "|"
            for col in row:
                if col == 0:
                    s += "  "
                elif col == 1:
                    s += YELLOW + "O "
                else:
                    s += RED + "O "
            s += "|\n"
        s += " - - - - - - - -" + "\n" + " 0 1 2 3 4 5 6 7" + "\n"
        return s