from board import *
from player import Player
from calculate import *

YELLOW = '\033[1;33;40m'
RED = '\033[1;31;40m'


def start_game():
    """"Starts game loop"""

    while True:
        choice = int(input("\nWelcome to Connect4 \n1.Human vs Human\n2.Human vs AI\n3.AI vs AI\nChoose one: "))
        if choice == 1:
            humanvshuman()
        elif choice == 2:
            humanvsai()
        elif choice == 3:
            aivsai()
        else:
            print("\nChoose between 1-3.\n")
            continue


def humanvshuman():
    """"Human vs human option"""

    player1 = Player("Player 1", "yellow", 1)
    player2 = Player("Player 2", "red", 2)

    board = Board()

    print("\nThe game has started")

    print(board)

    while True:
        """loops until last move"""
        try:
            isPlayed1 = True
            while isPlayed1:
                column = int(input(f"{player1.name} (X), choose a column (0-7): "))
                if 0 <= column < 8:
                    board.add_piece(column, player1.color)
                    print(board)
                    isPlayed1 = False
                else:
                    print("Invalid column, try again")

            if board.check_win(player1.color):
                print(YELLOW + player1.name + " wins!")
                break

            isPlayed2 = True
            while isPlayed2:
                column = int(input(f"{player2.name} (O), choose a column (0-7): "))
                if 0 <= column < 8:
                    board.add_piece(column, player2.color)
                    print(board)
                    isPlayed2 = False
                else:
                    print("Invalid column, try again")

            if board.check_win(player2.color):
                print(RED + player2.name + " wins!")
                break

        except ValueError:
            print("Invalid")


def humanvsai():
    """"human vs ai"""

    player1 = Player("Player 1", "yellow", 1)
    player2 = Player("AI Player", "red", 2)

    board = Board()

    while True:
        """input for ais depth level"""
        difficulty = int(input("Select a difficulty level (1-3): "))

        if difficulty < 1 or difficulty > 5:
            print("Select again.")
        else:
            break

    print("\nThe game has started")

    print(board)

    while True:
        try:
            isPlayed1 = True
            while isPlayed1:
                column = int(input(f"{player1.name}, choose a column (0-7): "))
                if 0 <= column < 8:
                    board.add_piece(column, player1.color)
                    print(board)
                    isPlayed1 = False
                else:
                    print("Invalid column, try again")

            if board.check_win(player1.color):
                print(YELLOW + player1.name + " wins!")
                break

            """"Starts the minimax function"""
            column = minimax_alphabeta(board, difficulty + 2, player2.piece)

            board.add_piece(column, player2.piece)
            print(board)

            print(f"{player2.name}, added a piece to {column}\n")

            if board.check_win(player2.color):
                print(RED + player2.name + " wins!")
                break
        except ValueError:
            print("Invalid")


def aivsai():
    """"ai vs ai game"""

    player1 = Player("AI Player 1", "yellow", 1)
    player2 = Player("AI Player 2", "red", 2)

    board = Board()

    while True:
        """selecting the difficulty level for both sides"""
        difficulty_1 = int(input("Select a difficulty level for AI-1 (1-3): "))

        difficulty_2 = int(input("Select a difficulty level for AI-2 (1-3): "))

        if difficulty_1 < 1 or difficulty_1 > 5 or difficulty_2 < 1 or difficulty_2 > 5:
            print("Select again.")
        else:
            break

    print("\nThe game has started")

    while True:
        column = minimax_alphabeta(board, difficulty_1+2, player1.piece)

        board.add_piece(column, player1.color)
        print(board)

        print(f"{player1.name}, added a piece to {column}\n")

        if board.check_win(player1.color):
            print(YELLOW + player1.name + " wins!")
            break

        column = minimax_alphabeta(board, difficulty_2+2, player2.piece)

        board.add_piece(column, player2.color)
        print(board)

        print(f"{player2.name}, added a piece to {column}\n")

        if board.check_win(player2.color):
            print(RED + player2.name + " wins!")
            break


def minimax_alphabeta(board, diff, player):
    """to know which player is using minimax"""
    other_piece = 2 if player == 1 else 1

    """"gets playable columns"""
    free_cols = board.get_free_cols()

    alpha = -math.inf
    beta = math.inf

    """"best score to decide best move"""
    best_score = alpha
    best_play = free_cols[0]

    for col in free_cols:
        tempBoard = board.move_for_ai(col, player)[0]
        score = minimum_beta(tempBoard, diff - 1, alpha, beta, player, other_piece)

        if score > best_score:
            best_score = score
            best_play = col

    return best_play


def minimum_beta(board, diff, alpha, beta, player1, player2):
    possibleMoves = []

    for col in range(7):
        if board.isValid(col):
            temp = board.move_for_ai(col, player1)[2]
            possibleMoves.append(temp)

    """if difficulty level is over or there are no possible moves or when its over returns the current board and calculates minimax score"""
    if len(possibleMoves) == 0 or checkIsWin(board) or diff == 0:
        return minimax_point(board, player1)

    moves = board.get_free_cols()
    b = beta

    for col in moves:
        score = math.inf

        if alpha < b:
            tempBoard = board.move_for_ai(col, player2)[0]
            score = maximum_alpha(tempBoard, diff - 1, alpha, b, player1, player2)

        if score < b:
            b = score

    return b


def maximum_alpha(board, diff, alpha, beta, player1, player2):
    possibleMoves = []

    for col in range(7):
        if board.isValid(col):
            temp = board.move_for_ai(col, player1)[2]
            possibleMoves.append(temp)

    if len(possibleMoves) == 0 or checkIsWin(board) or diff == 0:
        return minimax_point(board, player1)

    a = alpha

    for move in possibleMoves:
        score = -math.inf
        if a < beta:
            tempBoard = board.move_for_ai(move, player1)[0]
            score = minimum_beta(tempBoard, diff - 1, a, beta, player1, player2)

        if score > a:
            a = score

    return a


if __name__ == '__main__':
    start_game()
