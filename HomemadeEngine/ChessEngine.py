import chess
from HomemadeEngine.Evaluation import evaluate_position, negamax_evaluate_position
from HomemadeEngine.EngineConstants import *

nodes = 0

# MINIMAX IMPLEMENTATION
def get_best_move(board, is_white, depth = 3):
    best_move_value = -100000 if is_white else 100000
    alpha_beta = best_move_value
    best_move = None
    global nodes
    nodes = 0

    print("Minimax move evaluations")

    if is_white:
        for move in board.legal_moves:
            board.push(move)
            val = minimax(board, depth-1, alpha_beta, 100000, not is_white)

            print(str(move) + " - " + str(val))

            board.pop()
            if (is_white and val > best_move_value) or (not is_white and val < best_move_value):
                best_move_value = val
                alpha_beta = max(alpha_beta, best_move_value)
                best_move = move
    else:
        for move in board.legal_moves:
            board.push(move)
            val = minimax(board, depth-1, -100000, alpha_beta, not is_white)

            print(str(move) + " - " + str(val))

            board.pop()
            if (is_white and val > best_move_value) or (not is_white and val < best_move_value):
                best_move_value = val
                best_move = move
                alpha_beta = min(alpha_beta, best_move_value)
    print("Minimax Best move value: " + str(best_move_value))
    print("Minimax Best Move: " + str(best_move))
    return best_move

# White = Maximizing
# Black = Minimizing
def minimax(board, depth, alpha, beta, is_maximizing):
    if depth <= 0 or board.is_game_over():
        return evaluate_position(board)

    global nodes
    nodes += 1

    # White to play
    if is_maximizing:
        best_move = -100000
        for move in board.legal_moves:
            board.push(move)
            value = minimax(board, depth-1, alpha, beta, not is_maximizing)
            board.pop()
            best_move = max(best_move, value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move

    # Black to play
    else:
        best_move = 100000
        for move in board.legal_moves:
            board.push(move)
            value = minimax(board, depth-1, alpha, beta, not is_maximizing)
            board.pop()
            best_move = min(best_move, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return best_move
    


# NEGAMAX IMPLEMENTATION
def negamax(board, depth, alpha, beta):
    if depth <= 0 or board.is_game_over():
        return negamax_evaluate_position(board)
    
    best_move = -1000

    for move in board.legal_moves:
        board.push(move)
        eval = -negamax(board, depth-1, -beta, -alpha)
        board.pop()

        best_move = max(best_move, eval)
        alpha = max(alpha, eval)
        if alpha >= beta:
            break
    return best_move

def negamax_get_best_move(board, depth=3):
        alpha = -1000
        beta = 1000
        color = 1 if board.turn == WHITE else -1

        best_move_val = -100
        best_move = None

        for move in board.legal_moves:
            board.push(move)
            eval = -negamax(board, 3, alpha, beta)
            board.pop()

            if eval > best_move_val:
                best_move_val = eval
                best_move = move
        
        return best_move
