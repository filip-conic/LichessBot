import chess
from HomemadeEngine.Evaluation import evaluate_position, negamax_evaluate_position
from HomemadeEngine.EngineConstants import *

nodes = 0
nodeCount = 1
nodePrinted = True

print_depth_ls = [False for i in range(100)]

def order_moves(board):
    legal_moves = board.legal_moves
    captures = []
    checks = []
    other = []

    for move in legal_moves:
        if board.is_capture(move):
            captures.append(move)
        elif board.gives_check(move):
            checks.append(move)
        else:
            other.append(move)

    ordered_moves = checks + captures + other
    return ordered_moves

# NEGAMAX IMPLEMENTATION
def negamax(board, depth, alpha, beta, use_quiet_search):    
    if depth <= 0 or board.is_game_over():
        if use_quiet_search:
            return negamax_quiescence_search(board, alpha, beta, 1, 10)
        else:
            return negamax_evaluate_position(board)
    
    global nodes
    nodes += 1
    best_move = -1000
    ordered_moves = order_moves(board)

    global nodeCount
    global nodePrinted
    if (nodes > nodeCount * 100000):
        nodePrinted = False
    if not nodePrinted:
        print("Current node num: " + str(nodes))
        nodePrinted = True
        nodeCount += 1


    for move in ordered_moves:
        board.push(move)
        eval = -negamax(board, depth-1, -beta, -alpha, use_quiet_search)
        board.pop()

        best_move = max(best_move, eval)
        alpha = max(alpha, eval)
        if alpha >= beta:
            break
    return best_move

def negamax_get_best_move(board, depth=3, use_quiet_search=True):
        alpha = -1000
        beta = 1000
        color = 1 if board.turn == WHITE else -1

        best_move_val = -100
        best_move = None
        global nodes
        nodes = 0

        ordered_moves = order_moves(board)

        for move in ordered_moves:
            board.push(move)
            eval = -negamax(board, depth-1, alpha, beta, use_quiet_search)
            board.pop()

            if eval > best_move_val:
                best_move_val = eval
                best_move = move
        
        print("Nodes for move search: " + str(nodes))
        return best_move

# Searches all captures
def negamax_quiescence_search(board, alpha, beta, depth, maxDepth):
    if maxDepth <= 0 or board.is_game_over():
        return negamax_evaluate_position(board)

    eval = negamax_evaluate_position(board)
    alpha = max(eval, alpha)

    if(not print_depth_ls[depth]):
        print("Hit Depth " + str(depth) + " in quiet search")
        print_depth_ls[depth] = True

    global nodes
    nodes += 1

    global nodeCount
    global nodePrinted
    if (nodes > nodeCount * 100000):
        nodePrinted = False
    if not nodePrinted:
        print("Current node num: " + str(nodes))
        nodePrinted = True
        nodeCount += 1

    if eval >= beta:
        return beta
    
    ordered_moves = order_moves(board)
    
    for move in ordered_moves:
        if board.is_capture(move) or board.gives_check(move):
            board.push(move)
            eval = -negamax_quiescence_search(board, -beta, -alpha, depth+1, maxDepth-1)
            board.pop()

            alpha = max(alpha, eval)
            if eval >= beta:
                return beta
            
    return alpha
