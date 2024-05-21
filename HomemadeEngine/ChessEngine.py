import chess
from HomemadeEngine.Evaluation import evaluate_position

nodes = 0

def get_best_move(board, is_white, depth = 3):
    best_move_value = -100000 if is_white else 100000
    alpha_beta = best_move_value
    best_move = None
    global nodes
    nodes = 0

    if is_white:
        for move in board.legal_moves:
            board.push(move)
            val = minimax(board, depth-1, alpha_beta, 100000, not is_white)
            board.pop()
            if (is_white and val > best_move_value) or (not is_white and val < best_move_value):
                best_move_value = val
                alpha_beta = max(alpha_beta, best_move_value)
                best_move = move
    else:
        for move in board.legal_moves:
            board.push(move)
            val = minimax(board, depth-1, -100000, alpha_beta, not is_white)
            board.pop()
            if (is_white and val > best_move_value) or (not is_white and val < best_move_value):
                best_move_value = val
                best_move = move
                alpha_beta = min(alpha_beta, best_move_value)
    print("Nodes for best move call: " + str(nodes))
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


