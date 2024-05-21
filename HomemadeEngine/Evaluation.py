import chess
from HomemadeEngine.PieceTables import *
from HomemadeEngine.EngineConstants import *

def evaluate_position(board):
    if board.is_checkmate():
        if board.turn == chess.BLACK:
            return 100000
        else: 
            return -100000
    
    if board.is_stalemate():
        return 0
    
    # Basic piece value eval
    piece_value_eval = 0
    for piece in EVAL_PIECES:
        if piece == KING:
            continue
        w_pieces = len(board.pieces(piece, WHITE))
        b_pieces = len(board.pieces(piece, BLACK))
        piece_value_eval += PIECE_VALUES[piece] * (w_pieces - b_pieces)

    # Piece Table Evaluation
    piece_table_eval = 0
    for piece in EVAL_PIECES:
        w_eval = sum([PIECE_TO_TABLE[piece][i]/100 for i in board.pieces(piece, WHITE)])
        b_eval = sum([ -(PIECE_TO_TABLE[piece][chess.square_mirror(i)]/100) for i in board.pieces(piece, BLACK)])
        piece_table_eval += w_eval + b_eval

    final_eval = piece_value_eval + piece_table_eval

    return final_eval