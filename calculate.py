import math

columNum = 8
rowNum = 7

def calculateBoard(board, player, length):

    def horizontal(row, col):
        """checks for possible horizontal win"""
        count = 0
        for colIndex in range(col, columNum):
            if board[row][colIndex] == board[row][col]:
                count += 1
            else:
                break
        if count >= length:
            return 1
        else:
            return 0

    def vertical(row, col):
        """checks for possible vertical win"""
        count = 0
        for rowIndex in range(row, rowNum):
            if board[rowIndex][col] == board[row][col]:
                count += 1
            else:
                break
        if count >= length:
            return 1
        else:
            return 0

    def left_diagonal(row, col):
        """checks for possible diagonal win"""
        count = 0
        colIndex = col
        for rowIndex in range(row, -1, -1):
            if colIndex > rowNum:
                break
            elif board[rowIndex][colIndex] == board[row][col]:
                count += 1
            else:
                break
            colIndex += 1
        if count >= length:
            return 1
        else:
            return 0

    def right_diagonal(row, col):
        """checks for possible diagonal win"""
        count = 0
        colIndex = col
        for rowIndex in range(row, rowNum):
            if colIndex > rowNum:
                break
            elif board[rowIndex][colIndex] == board[row][col]:
                count += 1
            else:
                break
            colIndex += 1
        if count >= length:
            return 1
        else:
            return 0

    point = 0

    for row in range(rowNum):
        for col in range(columNum):
            if board[row][col] == player:
                point += horizontal(row, col)
                point += vertical(row, col)
                point += (right_diagonal(row, col) + left_diagonal(row, col))
    return point


def minimax_point(board, player):
    """calculates the minimax score to decide the best play. It plays and calculates from the current state of the board. 4 piece sequence is the most dangerous so its score will be bigger in our case.
        it also calculates the opponents score to decide its score to calculate what is the best move from this state.
    """
    playerTwo = 2 if player == 1 else 1

    playerScore = calculateBoard(board.board, player, 4) * 99999 + calculateBoard(board.board, player,
                                                                                  3) * 999 + calculateBoard(board.board,
                                                                                                            player,
                                                                                                            2) * 99

    fourPieces = calculateBoard(board.board, playerTwo, 4)
    threePieces = calculateBoard(board.board, playerTwo, 3)
    twoPieces = calculateBoard(board.board, playerTwo, 2)

    playerTwoScore = fourPieces * 99999 + threePieces * 999 + twoPieces * 99

    if fourPieces > 0:
        return -math.inf
    else:
        return playerScore - playerTwoScore


def checkIsWin(board):
    """this will check win for both side and return true or false"""
    if calculateBoard(board.board, 2, 4) >= 1 or calculateBoard(board.board, 1, 4) >= 1:
        return True
    else:
        return False
