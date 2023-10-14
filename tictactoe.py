"""
Tic Tac Toe Player
"""

import math
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
    count_x = sum(row.count('X') for row in board)
    count_o = sum(row.count('O') for row in board)
    if count_x == count_o:
        return 'X'
    else:
        if count_x == count_o + 1:
            return 'O'
        else:
            return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilities = {(i, j) for i, row in enumerate(board) for j, val in enumerate(row) if val == EMPTY}
    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if action not in actions(new_board):
        print(action)
        print(actions(new_board))
        raise ValueError
    else:
        i, j = action
        new_board[i][j] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    if ((board[0][0] == board[1][1] == board[2][2] and board[1][1] != EMPTY)
        or (board[0][2] == board[1][1] == board[2][0] and board[1][1] != EMPTY)):
        return board[1][1]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    if(sum(row.count(EMPTY) for row in board)==0):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)=='X':
        return 1
    else:
        if winner(board)=='O':
            return -1
    return 0


def minimax_rec(board):
    
    if terminal(board):
        return utility(board)

    if player(board) == 'X':
        best_val = float('-inf')
        for action in actions(board):
            seq_board = result(board, action)
            aux_val = minimax_rec(seq_board)
            if aux_val > best_val:
                best_val = aux_val
                best_action = action
        return best_val
    else:
        worst_val = float('inf')
        for action in actions(board):
            seq_board = result(board, action)
            aux_val = minimax_rec(seq_board)
            if aux_val < worst_val:
                worst_val = aux_val
        return worst_val

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == 'X':
        best_val = float('-inf')
        best_action = None
        for action in actions(board):
            seq_board = result(board, action)
            aux_val = minimax_rec(seq_board)
            if aux_val > best_val:
                best_val = aux_val
                best_action = action
        return best_action
    else:
        worst_val = float('inf')
        worst_action = None
        for action in actions(board):
            seq_board = result(board, action)
            aux_val = minimax_rec(seq_board)
            if aux_val < worst_val:
                worst_val = aux_val
                worst_action = action
        return worst_action

