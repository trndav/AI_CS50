"""
Tic Tac Toe Player
"""

import math
import tictactoe as ttt
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_X = sum(row.count("X") for row in board)
    num_O = sum(row.count("O") for row in board)

    if num_X <= num_O:
        return "X"
    else:
        return "O"
    raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == ttt.EMPTY:
                possible_actions.add((i, j))

    return possible_actions
    raise NotImplementedError

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)  # Make a deep copy 

    i, j = action

    # Validate if the action is a valid action for the board
    if new_board[i][j] != ttt.EMPTY:
        raise Exception("Invalid action: Cell is already occupied")

    # Update the cell with the player's symbol
    new_board[i][j] = player

    return new_board
    raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(ttt.X) == 3:
            return ttt.X
        elif row.count(ttt.O) == 3:
            return ttt.O

    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(ttt.X) == 3:
            return ttt.X
        elif [board[row][col] for row in range(3)].count(ttt.O) == 3:
            return ttt.O

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == ttt.X or board[0][2] == board[1][1] == board[2][0] == ttt.X:
        return ttt.X
    elif board[0][0] == board[1][1] == board[2][2] == ttt.O or board[0][2] == board[1][1] == board[2][0] == ttt.O:
        return ttt.O

    return None  # No winner
    raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    # Check if all cells are filled
    for row in board:
        if ttt.EMPTY in row:
            return False  # Game still in progress
    return True
    raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)

    if winner_player == ttt.X:
        return 1  # X has won, utility is 1
    elif winner_player == ttt.O:
        return -1  # O has won, utility is -1
    else:
        return 0
    raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    player = player(board)

    def max_value(board, alpha, beta, depth):
        if terminal(board) or depth == 0:
            return utility(board)

        v = float("-inf")
        for action in actions(board):
            v = max(v, min_value(result(board, action), alpha, beta, depth - 1))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v

    def min_value(board, alpha, beta, depth):
        if terminal(board) or depth == 0:
            return utility(board)

        v = float("inf")
        for action in actions(board):
            v = min(v, max_value(result(board, action), alpha, beta, depth - 1))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v

    best_move = None
    best_score = float("-inf")

    for action in actions(board):
        score = min_value(result(board, action), float("-inf"), float("inf"), 10)
        if score > best_score:
            best_score = score
            best_move = action

    return best_move
    raise NotImplementedError
